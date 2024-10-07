import pandas as pd

# Загрузка данных из CSV-файла в DataFrame
file_path = 'dz.csv'
df = pd.read_csv(file_path)

# Вычисление средней зарплаты по каждому городу
average_salary_by_city = df.groupby('City')['Salary'].mean()

# Вывод результата
print("Средняя зарплата по каждому городу:")
print(average_salary_by_city)
