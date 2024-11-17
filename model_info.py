import requests
import json

def get_model_info(model_name):
    request_payload = {
        "action": "modelNamesAndIds",
        "version": 6
    }
    response = requests.post('http://localhost:8765', json=request_payload)
    result = response.json()
    models = result.get('result', {})
    model_id = models.get(model_name)

    if model_id:
        request_payload = {
            "action": "modelFieldNames",
            "version": 6,
            "params": {
                "modelName": model_name
            }
        }
        response = requests.post('http://localhost:8765', json=request_payload)
        fields = response.json().get('result', [])

        request_payload = {
            "action": "modelTemplates",
            "version": 6,
            "params": {
                "modelName": model_name
            }
        }
        response = requests.post('http://localhost:8765', json=request_payload)
        templates = response.json().get('result', {})

        return {
            "model_id": model_id,
            "fields": fields,
            "templates": templates
        }
    else:
        return None

model_name = "Basic"  # Replace with the name of your model
model_info = get_model_info(model_name)

if model_info:
    print(f"Model ID for '{model_name}': {model_info['model_id']}")
    print(f"Fields: {model_info['fields']}")
    print(f"Templates: {json.dumps(model_info['templates'], indent=2)}")
else:
    print(f"Model '{model_name}' not found.")
