import pandas as pd
import json

with open('c:\\lab17\\boys.json', 'r', encoding='utf-8') as file:
    boys_data = json.load(file)

boys_series = pd.Series(boys_data)
boys_series = pd.to_datetime(boys_series)
boys_dict = boys_series.to_dict()

with open('c:\\lab17\\dtm.json', 'w', encoding='utf-8') as file:
    json.dump(boys_dict, file, default=str, ensure_ascii=False, indent=1)

print("Успішно записано у dtm.json")
