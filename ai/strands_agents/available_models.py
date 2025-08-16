import os
import json

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

model_attributes = json.load(open(f"{script_dir}/models.json"))
model_summaries = model_attributes["modelSummaries"]
models = [f"{model['providerName']} - {model['modelName']}" for model in model_summaries]
print(models)