import json
import urllib.request

def call_local_ai(prompt_text):
    url = "http://localhost:11434/api/generate"
    body = {"model": "phi3", "prompt": prompt_text, "stream": False}
    
    req = urllib.request.Request(
        url, 
        data=json.dumps(body).encode('utf-8'), 
        headers={'Content-Type': 'application/json'}
    )
    
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode('utf-8'))['response']

print("--- Connecting to ASUS TUF AI System Engine... ---")
output = call_local_ai("Write a 1-sentence motivation slogan for a beginner AI engineer.")
print("\nAI Response:\n", output)
