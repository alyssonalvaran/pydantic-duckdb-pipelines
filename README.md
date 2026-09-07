# Data-Engineered Analytics: Building Schema-Driven Event Pipelines in Python

Software applications often emit event logs as flexible, unstructured JSON payloads. While this speeds up initial feature development, it creates a massive gap when downstream analytics systems require rigid, predictable tables. 

This workshop repository provides a hands-on, self-contained project for building local data pipelines using **Python**, **Pydantic**, and **DuckDB**. You will learn how to bridge the disconnect by ingesting synthetic JSON payloads, enforcing strict schemas, validating data early, and querying the standardized output using SQL, all with zero infrastructure overhead.

## What You Will Learn

* **Schema Enforcement:** Use Pydantic to validate messy, unstructured JSON event payloads and catch data contract violations early.
* **Local Data Warehousing:** Leverage DuckDB to store, transform, and query structured event data locally without managing heavy database servers or Docker containers.
* **Pipeline Architecture:** Build a clean, modular Python script that takes raw logs, normalizes them, and loads them into an analytical query engine.

---

## Prerequisites

* **Python 3.10+** installed on your machine.
* A basic understanding of Python (dictionaries, classes/dataclasses, and functions).
* Familiarity with basic SQL queries (`SELECT`, `GROUP BY`, `JOIN`).

---

## Project Structure

```text
pydantic-duckdb-pipelines/
├── data/
│   └── raw_events.json        # Generated synthetic JSON event payloads
├── models/
│   └── events.py              # Pydantic schemas for event validation
├── generate_data.py           # Script to generate realistic mock data with Faker
├── pipeline.py                # Main ingestion and transformation script
├── requirements.txt           # Project dependencies
└── README.md
```

## Getting Started

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

### 4. Generate Synthetic Data

Run the generator script to populate your data/directory with realistic mock event logs. This script intentionally injects a controlled error rate to test the pipeline's validation logic:

```bash
python generate_data.py
```

### 5. Run the Pipeline

Execute the main script to process the generated JSON logs, drop malformed records, and load the clean data into DuckDB for analytics:

```bash
python pipeline.py
```

---

## Workshop Outline

This hands-on session is structured into four progressive modules, designed to take participants from messy input data to query-ready analytics:

* **Module 1: The Problem with Unstructured JSON**
  * Understanding the friction between flexible application logs and rigid analytical data requirements.
  * Examining sample raw payloads and identifying common data drift and corruption issues.

* **Module 2: Schema Enforcement with Pydantic**
  * Introduction to data contracts and validation in Python.
  * Writing Pydantic models to enforce strict types, field constraints, and custom validators.
  * Handling validation errors gracefully without breaking the ingestion pipeline.

* **Module 3: Building the Local Pipeline**
  * Designing a modular Python script to read, validate, and transform raw JSON logs.
  * Preparing normalized data structures ready for analytical storage.

* **Module 4: Analytics with DuckDB**
  * Loading validated records into an embedded DuckDB instance with zero infrastructure overhead.
  * Writing analytical SQL queries to extract insights, aggregate metrics, and inspect pipeline performance.

## Next Steps

Finished the core workshop? Here are a few ways you can extend the project and take your skills further:

* **Automate with Cron or Airflow:** Turn the static python script into a scheduled pipeline that runs hourly or daily against a live event stream.
* **Add Parquet Exports:** Modify the DuckDB load step to export your validated data into partitioned Apache Parquet files for cold storage or integration with other tools (like Pandas or Polars).
* **Implement Error Dead-Letter Queues:** Instead of dropping or crashing on invalid Pydantic payloads, route failing records into a separate `error_log.json` file for debugging and schema evolution tracking.
* **Scale to MotherDuck:** Swap your local DuckDB file connection for a MotherDuck cloud connection to see how local analytics code transitions to a hybrid cloud environment.
* **Build a Visualization:** Connect your DuckDB analytical queries to a lightweight dashboarding tool like Streamlit or Grafana to visualize user signups and plan breakdowns.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/alyssonalvaran/pydantic-duckdb-pipelines/blob/main/LICENSE) file for details.
