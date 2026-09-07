# Data-Engineered Analytics: Building Schema-Driven Event Pipelines in Python

Software applications often emit event logs as flexible, unstructured JSON payloads. While this speeds up initial feature development, it creates a massive gap when downstream analytics systems require rigid, predictable tables. 

This workshop repository provides a hands-on, self-contained project for building local data pipelines using **Python**, **Pydantic**, and **DuckDB**. You will learn how to bridge the disconnect by ingesting synthetic JSON payloads, enforcing strict schemas, validating data early, and querying the standardized output using SQL, all with zero infrastructure overhead.

## 🚀 What You Will Learn

* **Schema Enforcement:** Use Pydantic to validate messy, unstructured JSON event payloads and catch data contract violations early.
* **Local Data Warehousing:** Leverage DuckDB to store, transform, and query structured event data locally without managing heavy database servers or Docker containers.
* **Pipeline Architecture:** Build a clean, modular Python script that takes raw logs, normalizes them, and loads them into an analytical query engine.

---

## 🛠️ Prerequisites

* **Python 3.10+** installed on your machine.
* A basic understanding of Python (dictionaries, classes/dataclasses, and functions).
* Familiarity with basic SQL queries (`SELECT`, `GROUP BY`, `JOIN`).

---

## 📂 Project Structure

```text
pydantic-duckdb-pipelines/
├── data/
│   └── raw_events.json        # Synthetic JSON event payloads
├── models/
│   └── events.py              # Pydantic schemas for event validation
├── pipeline.py                # Main ingestion and transformation script
├── requirements.txt           # Project dependencies
└── README.md
```

## ⚙️ Quick Start

### 1. Clone the Repository

```bash
git clone [https://github.com/alyssonalvaran/pydantic-duckdb-pipelines](https://github.com/alyssonalvaran/pydantic-duckdb-pipelines)
cd pydantic-duckdb-pipelines
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Pipeline

Execute the main script to process the raw JSON logs and load them into DuckDB:

```bash
python pipeline.py
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/alyssonalvaran/pydantic-duckdb-pipelines/blob/main/LICENSE) file for details.
