#!/usr/bin/env python3
import threading, time, sys, queue, requests, random, signal

# Configuration
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X)",
    "curl/7.68.0"
]
HEADERS_LIST = [
    {"Connection": "keep-alive"},
    {"Connection": "close"}
]

lock = threading.Lock()
stop_event = threading.Event()

def worker(task_queue, stats, payload=None, method='GET', rps_limit=None):
    while not stop_event.is_set():
        try:
            job = task_queue.get(timeout=1)
        except queue.Empty:
            continue
        if job is None:
            break
        url, end_time = job
        headers = random.choice(HEADERS_LIST)
        headers['User-Agent'] = random.choice(USER_AGENTS)

        try:
            if method == 'POST':
                r = requests.post(url, data=payload, headers=headers, timeout=5)
            else:
                r = requests.get(url, headers=headers, timeout=5)

            with lock:
                stats['requests'] += 1
                stats['codes'][r.status_code] = stats['codes'].get(r.status_code, 0) + 1
                if r.status_code == 200:
                    stats['success'] += 1
                else:
                    stats['fail'] += 1

        except Exception as e:
            with lock:
                stats['fail'] += 1
                stats['requests'] += 1

        finally:
            if time.time() < end_time:
                task_queue.put((url, end_time))
            task_queue.task_done()
            if rps_limit:
                time.sleep(1 / rps_limit)

def run_test(url, concurrency, duration, method='GET', payload=None, rps_limit=None):
    task_queue = queue.Queue()
    stats = {'requests': 0, 'success': 0, 'fail': 0, 'codes': {}}
    end_time = time.time() + duration

    for _ in range(concurrency):
        task_queue.put((url, end_time))

    threads = []
    for _ in range(concurrency):
        t = threading.Thread(target=worker, args=(task_queue, stats, payload, method, rps_limit))
        t.start()
        threads.append(t)

    try:
        while time.time() < end_time:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user")
        stop_event.set()

    for _ in threads:
        task_queue.put(None)
    for t in threads:
        t.join()

    print("\nTest complete:")
    print(f"  Total Requests: {stats['requests']}")
    print(f"  Successes:      {stats['success']}")
    print(f"  Failures:       {stats['fail']}")
    print("  Status codes:   ", stats['codes'])

def console():
    menu = """
    Select Attack Type:
      1) Load Attack
      2) Stress Attack
      3) Spike Attack
      4) Soak Attack
      5) Exit
    """
    while True:
        print(menu)
        choice = input("Enter choice: ").strip()
        if choice == '5':
            print("Exiting.")
            break
        url = input("Target URL: ").strip()
        conc = int(input("Concurrency (threads): ").strip())
        dur = int(input("Duration (seconds): ").strip())
        method = input("HTTP Method (GET/POST) [default: GET]: ").strip().upper() or "GET"
        payload = None
        if method == "POST":
            payload = input("Payload for POST (key1=val1&key2=val2): ").strip()
        rps_input = input("Throttle RPS (Requests/sec) [optional]: ").strip()
        rps_limit = float(rps_input) if rps_input else None

        if choice == '3':
            print("Running Spike Test: 2 bursts")
            run_test(url, conc * 2, dur // 2, method, payload, rps_limit)
            run_test(url, conc, dur // 2, method, payload, rps_limit)
        else:
            run_test(url, conc, dur, method, payload, rps_limit)

        input("\nPress Enter to continue...")

if __name__ == '__main__':
    console()
