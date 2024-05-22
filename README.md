# kuberay_tests

## Docker deployment

Run the following bash commands to deploy the ML model in a Docker container.

- Build the image: ```docker buildx build --tag 'lw_translator' .```
- Run the image: ```docker run -it -p 8000:8000 'lw_translator'```

## Kubernetes deployment

Run the following bash commands to deploy the ML model in a Kubernetes cluster.

- Install the kuberay-operator: ```helm install kuberay-operator kuberay/kuberay-operator --version 1.1.0```
- Deploy the ML model: ```kubectl apply -f ray-service.translator.yaml```
