import json

with open("../api_response.txt") as f:
    api_result = json.load(f)
api_result["api_data"]["api_list"][0]["api_title"] = "Create destroyer squadron"
print(api_result["api_data"]["api_list"][0]["api_title"])
with open("../api_response.txt", "w") as f:
    json.dump(api_result, f)
