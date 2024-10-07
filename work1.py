import pandas as pd

# Загрузка данных из CSV-файла в DataFrame
file_path = 'World-happiness-report-2024.csv'
df = pd.read_csv(file_path)

# Вывод первых 5 строк
print("Первые 5 строк данных:")
print(df.head())

# Вывод информации о данных
print("\nИнформация о данных:")
print(df.info())

# Статистическое описание данных
print("\nСтатистическое описание данных:")
print(df.describe())
