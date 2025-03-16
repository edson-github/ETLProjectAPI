import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# post ChatGPT

url = 'https://api.openai.com/v1/chat/completions'

openai_api_key = os.getenv("OPENAI_API_KEY")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "What is the capital of France?"}],
}

try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()  # Raise an exception for HTTP errors
    
    response_data = response.json()
    if 'choices' in response_data and len(response_data['choices']) > 0:
        data = response_data['choices'][0]['message']['content']
        print(data)
    else:
        print("Unexpected API response format:")
        print(json.dumps(response_data, indent=2))
except requests.exceptions.RequestException as e:
    print(f"API request error: {e}")
except json.JSONDecodeError:
    print("Failed to parse API response as JSON")
except Exception as e:
    print(f"Error: {e}")
    print("Response content:", response.text)
