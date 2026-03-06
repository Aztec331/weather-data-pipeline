# 🌦️ Weather Data ETL Pipeline using Snowflake

## 📌 Project Overview

This project demonstrates an end-to-end **Data Engineering ETL pipeline** that collects live weather data from an external API, transforms it into a structured format, and loads it into a Snowflake cloud data warehouse for analysis.

It showcases real-world data engineering practices such as data ingestion, transformation, warehouse loading, and layered data architecture.

---

## 🏗️ Architecture

```
Weather API
    ↓
Extract (Python)
    ↓
Raw Layer — JSON
    ↓
Transform (Pandas)
    ↓
Clean Layer — CSV
    ↓
Load (Snowflake Connector)
    ↓
Snowflake Data Warehouse
```

---

## ⚙️ Tech Stack

* **Python** — Pipeline scripting
* **Pandas** — Data transformation
* **Requests** — API data extraction
* **Snowflake** — Cloud data warehouse
* **SQL** — Data modeling & querying

---

## 📂 Project Structure

```
weather-data-pipeline/
│
├── extract_weather.py        # Extract data from Weather API
├── transform_weather.py      # Transform raw JSON to structured CSV
├── load_to_snowflake.py      # Load clean data into Snowflake
├── config.py                 # API keys & Snowflake credentials (ignored in git)
├── requirements.txt          # Python dependencies
├── .gitignore                # Prevents secrets & cache files from uploading
├── README.md                 # Project documentation
│
└── data/
    ├── raw_weather.json      # Raw data layer
    └── clean_weather.csv     # Clean data layer
```

---

## 🔄 ETL Pipeline Steps

### 1️⃣ Extract

* Fetches real-time weather data from a public API
* Stores unprocessed response as raw JSON

**Output:** `data/raw_weather.json`

---

### 2️⃣ Transform

* Parses JSON fields
* Selects relevant attributes
* Converts to tabular format using Pandas

**Output:** `data/clean_weather.csv`

---

### 3️⃣ Load

* Connects securely to Snowflake
* Inserts structured records into warehouse table

**Destination Table:** `WEATHER_DB.PUBLIC.WEATHER_DATA`

---

## 🗄️ Snowflake Table Schema

| Column      | Type      |
| ----------- | --------- |
| city        | STRING    |
| country     | STRING    |
| temperature | FLOAT     |
| feels_like  | FLOAT     |
| humidity    | INTEGER   |
| pressure    | INTEGER   |
| wind_speed  | FLOAT     |
| cloudiness  | INTEGER   |
| weather     | STRING    |
| loaded_at   | TIMESTAMP |

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Add credentials

Update `config.py` with:

* Weather API key
* Snowflake account details

### 3. Run pipeline

```bash
python extract_weather.py
python transform_weather.py
python load_to_snowflake.py
```

### 4. Verify in Snowflake

```sql
SELECT * FROM WEATHER_DATA;
```

---

## ✅ Data Engineering Concepts Demonstrated

* API Data Ingestion
* Raw vs Clean Data Layers
* Data Transformation
* Data Warehouse Modeling
* Cloud Data Loading
* End-to-End ETL Pipeline Design

---

## 🚀 Possible Enhancements

* Schedule automated runs (hourly/daily)
* Store historical weather records
* Ingest multiple cities
* Add pipeline logging
* Build BI dashboard on Snowflake

---

## 📄 Resume Description

**Weather Data ETL Pipeline using Snowflake**
Built an end-to-end ETL pipeline to ingest live weather API data, transform raw JSON into structured datasets using Python and Pandas, and load data into a Snowflake cloud data warehouse for analytics.

---

## 👨‍💻 Author

Aditya Babar
