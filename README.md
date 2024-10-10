
# Player Service Flask with Traditional AI Model

This repository contains a Python Flask application for player service generation, running on port 8000, alongside a traditional AI model that runs on port 5000.

## Features

- **Flask Web Service**: A RESTful API running on port 8000 to interact with player services.
- **Traditional AI Model**: An AI service running on port 5000 for player generation and related functionality.

## Prerequisites

Ensure you have the following installed:
- Python 3.x
- Flask
- Gitpod account (if running in Gitpod workspace)

## Repository Structure

```bash
.
app
├── app.py # Main Flask app runs on port 8000
    requirements.txt         # Python dependencies
model
 ├── a4a_model
      ├── server.py   # Traditional AI model service (runs on port 5000)
└── README.md                # Documentation
```

## How to Run the App in Gitpod

### Step 1: Open the Project in Gitpod

You can open this repository directly in Gitpod by clicking the button below:

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/gitpod-demo/player-service-flask-trad-ai)

Alternatively, you can manually open Gitpod by navigating to your Gitpod workspace dashboard and entering the repository URL: `https://github.com/gitpod-demo/player-service-flask-trad-ai`.

### Step 2: Running the Flask App and AI Model

You need to run both the Flask app (on port 8000) and the AI model (on port 5000) simultaneously.

#### Running the Flask App (Port 8000)

In the first terminal, run the following command to start the Flask app:

```bash
cd app
python app.py
```

This will start the Flask app on port 8000. 

#### Running the Traditional AI Model (Port 5000)

The workspace should start with the AI model already running on port 5000.

```bash
cd model
cd a4a_model
python server.py
```

This will start the AI model on port 5000.

### Step 4: Exposing Ports in Gitpod

In Gitpod, you'll need to expose the ports so you can access the services from your browser.

1. **Expose the Flask App (Port 8000)**:
    In the terminal, run:
    
    ```bash
    gp ports expose 8000
    ```

2. **Expose the AI Model (Port 5000)**:
    In the terminal, run:
    
    ```bash
    gp ports expose 5000
    ```

Gitpod will provide URLs to access both services externally.

### Step 5: Making API Calls

Once both services are running, you can interact with them using `curl` or Postman. Here's an example `curl` request to the `/team/generate` endpoint:

```bash
curl -H "Content-Type: application/json" -X POST -d '{"seed_id":"abbotji01","team_size":10}' http://127.0.0.1:8000/team/generate
```

## API Endpoints

### Flask App (Port 8000)

#### `/team/generate` (POST)
- **Description**: Generate a player team using the AI model.
- **Request Body**: JSON payload with `seed_id` and `team_size`.
- **Response**: JSON response with team generation information.

Example request:

```bash
curl -H "Content-Type: application/json" -X POST -d '{"seed_id":"abbotji01","team_size":10}' http://localhost:8000/team/generate
```
