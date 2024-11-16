import requests

def get_ollama_response(prompt, server_ip, model):
    url = f"http://{server_ip}:11434/api/generate"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False  # Add this line
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        json_obj = response.json()
        generated_text = json_obj.get('response', '')
        return generated_text.strip()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    server_ip = 'homews.home.local'  # Replace with your server IP or hostname
    model_name = 'llama3'            # Replace with your model name
    while True:
        user_input = input("Enter your prompt (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        reply = get_ollama_response(user_input, server_ip, model=model_name)
        if reply:
            print("Ollama:", reply)
        else:
            print("No response received.")