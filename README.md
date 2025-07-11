# Teegarden Project API Infra

The **Teegarden Project** is composed of multiple connected components.

## Components

- **Teegarden-Project-API-Infra**  
  This repository. It contains all the infrastructure deployment code and the business logic related to reinforcement learning (RL) training, data persistence, and serving the AI model.

- **Teegarden-Project-GameClient**  
  The Unity game that sends and retrieves data from the API.

- **Teegarden-Project-Intellicombat-RL-Trainer**  
  A Python project focused exclusively on reinforcement learning and data simulation.

In essence, the **API** acts as a shell for the RL Trainer (since it pulls the code from *Intellicombat-RL-Trainer* and runs it internally). The **GameClient** is the consumer of the trained model and API services.

## Usage

To deploy the API locally:

```bash
docker compose build --no-cache
docker compose up -d --build
