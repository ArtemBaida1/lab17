import pandas as pd
import json

months = [
    "Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень",
    "Липень", "Серпень", "Вересень", "Жовтень", "Листопад", "Грудень"
]

slabs = []
print("Введіть кількість бетонних плит, виготовлених за кожен місяць:")
for month in months:
    count = int(input(f"{month}: "))
    slabs.append(count)

series = pd.Series(slabs, index=months)

with open('beton.json', 'w', encoding='utf-8') as file:
    series.to_json(file, force_ascii=False)

print("Дані успішно збережені у файл beton.json")
