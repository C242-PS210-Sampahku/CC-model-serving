# Flask ML Model Serving Application

This is a Flask-based application designed to serve a our machine learning model. The application provides a RESTful API to interact with the model for making predictions.

## Requirements

- Python 3.10 or later
- Dependencies listed in `requirements.txt`

## Installation 

1. Clone the repository:
   ```bash
   git clone https://github.com/C242-PS210-Sampahku/CC-model-serving.git
   cd CC-model-serving
2. Install Depedency
   ```bash
   pip install -r requirements.txt
3. Run app
   ```bash
   python -m flask run --host=0.0.0.0 --port=5000


# Flask TensorFlow Application with Docker

demonstrates how to containerize and run a Flask application serving a TensorFlow model using Docker.

---

## Prerequisites

Make sure you have the following installed:
1. **Docker**: Download and install from [Docker's official website](https://www.docker.com/).  
2. **(Optional) Docker Compose**: If you plan to use Docker Compose.

---

## How to Run with Docker

1. Build the Docker Image
   Run the following command to build the Docker image:
   ```bash
   docker build -t flask-tensorflow-app .
2. Run docker container
   ```bash
   docker run -d -p 5000:5000 --name flask-container flask-tensorflow-app
3. Verify the Container is Running
   ```bash
   docker ps
4. View logs
   ```bash
   docker logs flask-container
5. Stop contaier
   ```bash
   docker logs flask-container



