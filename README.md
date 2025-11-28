# Law-N Signal Simulator (`law-n-signal-sim`)

Time-stepped **network signal simulator** for **Law-N**.

This repo generates synthetic `network.routes` data that matches the shape used by **N-SQL** (see `law-n-sql-core`). It models:

- **Towers** (IDs, G-layer mix, base latency)
- **Devices** (IDs, preferred G-layer)
- **Routes** between devices and towers
- Time-varying **latency** and **signal_quality**

You can:

- Run it from the **CLI** and stream snapshots
- Import it as a **Python library** and connect it to other Law-N components

---

## 🚀 Quickstart

### Requirements

- Python **3.10+**
- No external dependencies

### Install (local dev)

```bash
git clone https://github.com/PEACEBINFLOW/law-n-signal-sim/tree/main

cd law-n-signal-sim
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .
