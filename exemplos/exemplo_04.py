import requests
import json

# post ChatGPT

url = 'https://api.openai.com/v1/chat/completions'

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer XXXX"

}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "What is the capital of France?"}],
}

response = requests.post(url, headers=headers, data=json.dumps(data))
data = response.json()['choices'][0]['message']['content']
print(data)
