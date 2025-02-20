import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json',
}
history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)
    data = {
        "model": "llama2",
        "prompt": final_prompt,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        data = response.json()
        actual_response = data["response"]
        return actual_response
    else:
        return f"Error: {response.text}"

interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=2, placeholder="Enter your prompt"),
    outputs="text"
)

interface.launch()
