
import requests
import pandas as pd
from pathlib import Path

# 1. EXTRACT — получение данных из API

url = "https://archive-api.open-meteo.com/v1/archive"

params = {
    "latitude": 38.7223,
    "longitude": -9.1393,
    "start_date": "2025-01-01",
    "end_date": "2025-12-31",
    "daily": [
        "temperature_2m_max",
        "temperature_2m_min",
        "precipitation_sum",
        "wind_speed_10m_max"
    ],
    "timezone": "Europe/Lisbon"
}

response = requests.get(url, params=params, timeout=30)

response.raise_for_status()

data = response.json()

print("Data successfully extracted!")


# 2. TRANSFORM — преобразование данных

# Превращаем JSON в DataFrame
df = pd.DataFrame(data["daily"])

# Переименовываем столбцы
df = df.rename(columns={
    "time": "date",
    "temperature_2m_max": "temp_max",
    "temperature_2m_min": "temp_min",
    "precipitation_sum": "precipitation",
    "wind_speed_10m_max": "wind_speed_max"
})

# Преобразуем дату в формат datetime
df["date"] = pd.to_datetime(df["date"])

# Удаляем строки с отсутствующими значениями
df = df.dropna()

# Создаём новый столбец:
# разница между максимальной и минимальной температурой
df["temperature_range"] = (df["temp_max"] - df["temp_min"]).round(2)

# Создаём признак дождливого дня
df["is_rainy_day"] = df["precipitation"] > 0

# Сортируем данные по дате
df = df.sort_values(by="date")

print("Data successfully transformed!")


# 3. LOAD — сохранение результата

output_path = Path("data/processed/output.csv")

output_path.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(output_path, index=False)

print(f"Data successfully saved to {output_path}")

# Проверяем результат
print(df.head())
print(f"Total rows: {len(df)}")
print(f"Total columns: {len(df.columns)}")