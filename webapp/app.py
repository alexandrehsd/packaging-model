from flask import Flask, request, jsonify
import torch
import numpy as np
from transformers import RobertaTokenizer
import onnxruntime


app = Flask(__name__)  # creates the Flask application
tokenizer = RobertaTokenizer.from_pretrained("roberta-base")  # defines tokenizer
session = onnxruntime.InferenceSession(  # initializer ONNX runtime session
    "./models/roberta-sequence-classification-9.onnx")


# Flask route to enable live inferencing
@app.route("/predict", methods=["POST"])
def predict():
    input_ids = torch.tensor(
        tokenizer.encode(request.json[0], add_special_tokens=True)
    ).unsqueeze(0)
    
    if input_ids.requires_grad:
        inputs = {session.get_inputs()[0].name: input_ids.detach().cpu().numpy()}
    else:
        inputs = {session.get_inputs()[0].name: input_ids.cpu().numpy()}
    
    out = session.run(None, inputs)
    
    result = np.argmax(out)
    
    return jsonify({"positive": bool(result)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

