
# Open Data ETL - Lisbon Weather Analysis

## Project Overview

This project demonstrates a simple ETL workflow
using Python, Pandas, and the Open-Meteo API.

The goal is to collect historical weather data
for Lisbon, Portugal, transform it, and save
the cleaned dataset as a CSV file.

## Data Source

Open-Meteo Historical Weather API:

https://open-meteo.com/en/docs/historical-weather-api

Location: Lisbon, Portugal

Period: January 1, 2025 - December 31, 2025

## ETL Process

### 1. Extract
- Retrieve historical weather data using the Open-Meteo API.
- Receive data in JSON format.

### 2. Transform
- Convert JSON data into a Pandas DataFrame.
- Rename columns.
- Convert dates to datetime format.
- Remove missing values.
- Calculate daily temperature range.
- Create a rainy day indicator.
- Sort data by date.

### 3. Load
- Save the processed dataset to:
  data/processed/output.csv

## Technologies

- Python
- Pandas
- Requests
- Open-Meteo API

## How to Run

1. Clone this repository.
2. Install dependencies:

   pip install -r requirements.txt

3. Run the ETL script:

   python -m src.main

## Output

The processed CSV contains:
- Date
- Maximum temperature
- Minimum temperature
- Precipitation
- Maximum wind speed
- Temperature range
- Rainy day indicator

## Example Output

| date       | temp_max | temp_min | precipitation | wind_speed_max | temperature_range | is_rainy_day |
|------------|----------|----------|---------------|----------------|-------------------|--------------|
| 2025-01-01 | 12.9     | 6.6      | 0.0           | 15.4           | 6.3               | False        |
| 2025-01-02 | 15.0     | 5.8      | 0.0           | 10.0           | 9.2               | False        |
| 2025-01-03 | 16.1     | 8.6      | 1.7           | 12.4           | 7.5               | True         |
| 2025-01-04 | 17.4     | 10.8     | 1.3           | 21.4           | 6.6               | True         |


## Project Structure

```text
open-data-etl-weather/
│
├── data/
│   ├── raw/
│   └── processed/
│       └── output.csv
│
├── src/
│   └── main.py
│
├── README.md
├── requirements.txt
└── .gitignore
```