# packaging-model
This repository serves the educational purpose for learning how to package an ML model.

Here, we will use an ONNX model and package it within a container that serves a Flask app that performs the prediction. We will use the [RoBERTa-SequenceClassification](https://github.com/onnx/models/tree/main/text/machine_comprehension/roberta) ONNX model, which is very well documented.

Useful Information

- How to get [AZURE CREDENTIALS](https://techcommunity.microsoft.com/t5/educator-developer-blog/how-to-login-to-azure-with-github-actions/ba-p/3573050) 
- How to [login](https://github.com/docker/login-action) to any container registry on github actions
- How to get [DOCKER HUB ACCESS TOKEN](https://docs.docker.com/security/for-developers/access-tokens/)