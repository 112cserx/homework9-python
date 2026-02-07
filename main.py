import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns

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

# Настройка стиля (чтобы красиво выглядело)
sns.set(style="whitegrid")

# Размер графика
plt.figure(figsize=(12, 6))

# Построение графика
sns.countplot(data=df, x="signature", order=df["signature"].value_counts().index)

# Заголовок и подписи
plt.title("Распределение типов событий информационной безопасности")
plt.xlabel("Тип события")
plt.ylabel("Количество")

# Поворот подписей (иначе они не влезут)
plt.xticks(rotation=90)

# Чтобы всё аккуратно уместилось
plt.tight_layout()

# Показать график
plt.show()
