import pandas as pd
import json

# Открываем файл вручную
with open("events.json", "r") as f:
    data = json.load(f)

# Достаём список событий
events = data["events"]

# Превращаем в DataFrame
df = pd.DataFrame(events)

print("Первые 5 строк:")
print(df.head())

print("\nИнформация о таблице:")
print(df.info())

print("\nРаспределение событий по типам:")
signature_counts = df["signature"].value_counts()
print(signature_counts)
