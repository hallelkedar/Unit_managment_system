import os
import json

file_name = 'soldiers.json'

if not os.path.exists(file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        data = []
        json.dump(data, f, indent=2)

