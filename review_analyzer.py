import json
import urllib.request

def analyze_customer_review_advanced(review_text):
    url = "http://localhost:11434/api/generate"
    
    # Naya strict 5-step requirement format
    system_instruction = (
        "Analyze the following customer review and provide an output strictly designated for math matrix format:\n"
        "1. Sentiment: [Positive/Negative/Neutral]\n"
        "2. Main Issue/Topic: [2-3 word descriptor]\n"
        "3. Improvement Suggestion: [1-2 sentence constructive feedback]\n"
        "4. Related Feature: [Mention a specific phone feature that could enhance the user experience]\n"
        "5. Customer Service Contact: [Provide a generic contact number and email for support]"
    )
    
    full_prompt = f"{system_instruction}\n\nCustomer Review: \"{review_text}\""
    
    body = {
        "model": "phi3",
        "prompt": full_prompt,
        "stream": False
    }
    
    req = urllib.request.Request(
        url, 
        data=json.dumps(body).encode('utf-8'), 
        headers={'Content-Type': 'application/json'}
    )
    
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode('utf-8'))['response']

# --- LOGIC EXECUTION BLOCK ---
print("--- Starting Advanced AI Customer Review Analyzer System ---")

# Naya mixed complex review jo terminal ne diya tha
sample_complex_review = (
    "While the camera quality is superb with its 48MP sensor and night mode, "
    "the phone often overheats after prolonged use, which is quite concerning."
)

print(f"\nProcessing Complex Review: {sample_complex_review}\n")
print("AI is deeply analyzing the constraints...")

# Final Execution
advanced_result = analyze_customer_review_advanced(sample_complex_review)

print("\n--- ADVANCED ANALYZER OUTPUT RESULTS ---")
print(advanced_result)
