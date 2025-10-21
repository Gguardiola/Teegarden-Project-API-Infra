# Teegarden Project API Infra

The **Teegarden Project** is composed of multiple connected components.

## Components

- **Teegarden-Project-API-Infra**  
  This repository. It contains all the deployment infrastructure (pipelines, config maps, environment variables, etc). Also pushes and builds the ai-training-microservice to the Docker Hub registry including the Intellicombat-RL-Trainer repo within the image.

- **Teegarden-Project-GameClient**  
  The Unity game that sends and retrieves data from the API. https://github.com/Gguardiola/Teegarden-Project-GameClient

- **Teegarden-Project-Intellicombat-RL-Trainer**  
  A Python project focused exclusively on reinforcement learning and data simulation. Included inside the ai-training-microservice image that is deployed through the API-Infra repo. https://github.com/Gguardiola/Teegarden-Project-Intellicombat-RL-Trainer

In essence, the **API** acts as a shell for the RL Trainer (since it pulls the code from *Intellicombat-RL-Trainer* and runs it internally). The **GameClient** is the consumer of the trained model and API services.

## Usage

To deploy the API locally:

```bash
docker compose build --no-cache
docker compose up -d --build
```
To deploy the API locally using kubectl:

```bash
  docker login
  kubectl apply -k .k8s
```
To deploy the API to the production Kubernetes cluster:

- Run the build and push to registry pipeline (Github Actions)
- Run the deployment pipeline.

- Check locally using the kubeconfig file:

```bash

kubectl --kubeconfig=C:\Users\Gabriel\.kube\teegarden.yaml get pods -A   

```

Kubeconfig file can be obtained through the DigitalOcean control panel.
