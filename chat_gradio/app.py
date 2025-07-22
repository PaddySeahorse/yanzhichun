from flask import Flask, request, jsonify
from optimum.onnxruntime import ORTModelForCausalLM
from transformers import AutoTokenizer
import torch

app = Flask(__name__)
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = ORTModelForCausalLM.from_pretrained(model_name, export=True)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    history = data.get('history', [])
    
    prompt = "你是一个亲切的中文生活助手，回答简洁、实用。\n"
    for user_msg, bot_msg in history:
        prompt += f"User: {user_msg}\nAssistant: {bot_msg}\n"
    prompt += f"User: {message}\nAssistant: "
    
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs.input_ids, max_length=512, num_return_sequences=1, temperature=0.7)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    response = response[len(prompt):].strip()
    
    return jsonify({'response': response, 'history': history + [[message, response]]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # Render 默认端口