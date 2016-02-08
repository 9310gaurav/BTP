import json
json_data = open('catalog_dict.json')
catalog = json.load(json_data)
json_data.close()
json_data1 = open('inv_catalog_dict.json')
inv_catalog = json.load(json_data1)