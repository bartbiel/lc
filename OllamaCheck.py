import requests

try:
    response = requests.get("http://localhost:11434/api/tags")
    print(response.json())  # Should return a list of models if Ollama is running
except requests.exceptions.ConnectionError:
    print("Ollama is not running! Start it with 'ollama serve'.")
