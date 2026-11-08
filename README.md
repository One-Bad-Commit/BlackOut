# ☠️ BLACK-OUT
### `HTTP LOAD TESTING • STRESS ANALYSIS • NETWORK PERFORMANCE`

<p align="center">
  <img src="https://img.shields.io/badge/PROJECT-BLACK--OUT-000000?style=for-the-badge&logo=github&logoColor=white" />
  <img src="https://img.shields.io/badge/PYTHON-3.x-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/PLATFORM-LINUX%20%7C%20WINDOWS-lightgrey?style=for-the-badge" />
  <img src="https://img.shields.io/badge/USAGE-AUTHORIZED%20TESTING-green?style=for-the-badge" />
</p>

> **SYSTEM STATUS: ONLINE**
>
> *"Every system has a breaking point. Understanding its limits is the first step toward securing it."*

---

## ⚡ OVERVIEW

**BLACK-OUT** is a Python-based HTTP load-testing utility designed for controlled network performance experiments and authorized infrastructure testing.

Powered by multithreading and configurable request execution, BLACK-OUT allows security researchers, developers, and infrastructure administrators to observe how an HTTP endpoint responds under varying request loads.

Its interactive terminal interface provides configurable testing parameters, HTTP method selection, optional request throttling, and basic response statistics.

### 🧬 CORE CAPABILITIES

| Feature | Description |
|---|---|
| Multithreading | Concurrent HTTP request execution |
| GET Requests | HTTP GET request testing |
| POST Requests | HTTP POST request testing with custom payloads |
| Configurable Threads | Define concurrent worker count |
| Duration Control | Specify test duration in seconds |
| RPS Throttling | Optional per-worker request delay |
| Response Tracking | Track HTTP response codes |
| Success / Failure Stats | Basic request result statistics |
| Interactive CLI | Menu-driven terminal interface |
| Spike Mode | Two-stage burst-style testing |

---

## 🖥️ TESTING MODES

BLACK-OUT provides four selectable testing profiles.

**01 — LOAD TEST**

Execute concurrent HTTP requests against an authorized endpoint to observe its response under a configured workload.

**02 — STRESS TEST**

Run a higher-concurrency workload to examine application behavior under increased request pressure.

**03 — SPIKE TEST**

Execute a two-stage burst-style workload, initially using double the configured concurrency, followed by the configured concurrency.

**04 — SOAK TEST**

Run a sustained request workload for a specified duration to observe response behavior over time.

**Implementation note:** These profiles currently share the same underlying execution engine, except for Spike Mode. Load, Stress, and Soak do not yet implement distinct workload patterns.

---

## ⚙️ REQUIREMENTS

Before launching BLACK-OUT, ensure your environment has:

- Python 3.8 or newer
- pip package manager
- Internet or network connectivity to your authorized test endpoint
- Permission to perform testing against the target infrastructure

---

## 🚀 INSTALLATION

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Black-Out.git
```

### 2. Navigate to the project directory

```bash
cd Black-Out
```

### 3. Install dependencies

```bash
python3 -m pip install requests
```

### 4. Launch BLACK-OUT

```bash
python3 Black-Out.py
```

**Linux users:** If you use a virtual environment, activate it before installing dependencies.

---

## 🎮 USAGE GUIDE

Once launched, BLACK-OUT displays an interactive terminal menu:

```text
Select Attack Type:

  1) Load Attack
  2) Stress Attack
  3) Spike Attack
  4) Soak Attack
  5) Exit

Enter choice:
```

### Configuration parameters

The program prompts you for the following information:

| Parameter | Description |
|---|---|
| Target URL | Authorized HTTP endpoint |
| Concurrency | Number of worker threads |
| Duration | Test duration in seconds |
| HTTP Method | GET or POST |
| POST Payload | Optional form-style request body |
| Throttle RPS | Optional per-worker request delay |

### Example configuration

```text
Enter choice: 1

Target URL: http://127.0.0.1:8080
Concurrency (threads): 5
Duration (seconds): 10
HTTP Method (GET/POST) [default: GET]: GET
Throttle RPS (Requests/sec) [optional]: 1
```

The program executes the workload and displays the resulting statistics.

### POST request example

```text
HTTP Method (GET/POST) [default: GET]: POST

Payload for POST:
username=test&status=active
```

The payload is passed as the HTTP request body.

### Example output

```text
Test complete:

Total Requests:  100
Successes:       95
Failures:        5
Status codes:    {200: 95, 500: 5}
```

*Illustrative output only. Actual results depend on the target and network conditions.*

---

## 📊 HOW IT WORKS

BLACK-OUT follows a multithreaded request execution workflow:

```text
       ┌──────────────────────┐
       │    BLACK-OUT CLI     │
       └──────────┬───────────┘
                  │
       ┌──────────▼───────────┐
       │  Testing Parameters  │
       │ URL / Threads / Time │
       └──────────┬───────────┘
                  │
       ┌──────────▼───────────┐
       │     Task Queue       │
       └──────────┬───────────┘
                  │
          ┌───────▼───────┐
          │ Worker Threads│
          └───────┬───────┘
                  │
       ┌──────────▼───────────┐
       │   HTTP GET / POST    │
       └──────────┬───────────┘
                  │
       ┌──────────▼───────────┐
       │ Response Collection │
       └──────────┬───────────┘
                  │
       ┌──────────▼───────────┐
       │  Terminal Statistics│
       └─────────────────────┘
```

---

## 🛡️ SECURITY & LEGAL DISCLAIMER

**BLACK-OUT IS INTENDED STRICTLY FOR AUTHORIZED TESTING AND EDUCATIONAL PURPOSES.**

This project is provided as an experimental HTTP load-testing utility for legitimate security research, controlled laboratory environments, and infrastructure performance evaluation.

By using this software, you acknowledge and agree that:

1. You must own the target infrastructure or possess explicit authorization from its owner before conducting any testing.
2. You must comply with applicable cybersecurity laws, regulations, contractual obligations, and acceptable-use policies.
3. You must not use this software to disrupt services, overload third-party infrastructure, interfere with business operations, or conduct unauthorized denial-of-service activities.
4. Testing should be performed within approved traffic limits and agreed testing windows.
5. You are solely responsible for the configuration, execution, and consequences of using this software.

**The developer assumes no responsibility or liability for misuse, unauthorized activity, service interruptions, infrastructure damage, or legal consequences arising from the use of this project.**

This disclaimer does not grant permission to test any system.

### Important technical limitation

The current implementation does not enforce target allowlisting, a global request-rate ceiling, or a hard maximum concurrency limit. Its optional RPS setting applies a delay independently to each worker, not a global rate limit.

Use an isolated lab or an explicitly authorized test environment. Do not assume that selecting a low RPS value guarantees safe aggregate traffic.

---

## 🔬 PROJECT STATUS

**Development Stage:** Experimental

BLACK-OUT is an evolving project. Its current implementation provides basic HTTP workload generation and terminal statistics.

Potential future improvements:

- [ ] Live terminal monitoring
- [ ] Global request-rate enforcement
- [ ] Target allowlisting
- [ ] Maximum concurrency safeguards
- [ ] Detailed latency measurements
- [ ] Response-time percentiles
- [ ] Exportable test reports
- [ ] Improved workload profiles
- [ ] Configuration file support

---

## 👨‍💻 CONTRIBUTIONS

Contributions, suggestions, bug reports, and improvements are welcome.

If you would like to contribute:

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Submit a pull request.

Please ensure contributions maintain the project's authorized-testing focus.

---

## 📜 LICENSE

Specify a license in the repository before distributing this project.

Unless a license is explicitly provided, all rights remain with the copyright holder. No permission to redistribute, modify, or commercially exploit the software should be assumed.

---

<p align="center">

### ☠️ BLACK-OUT

**CONTROL THE LOAD. UNDERSTAND THE LIMITS. SECURE THE SYSTEM.**

*Built for controlled experiments. Designed for security awareness.*

</p>
