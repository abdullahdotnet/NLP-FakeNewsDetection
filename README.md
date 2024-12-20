# Fake News Detection System

This project is a complete solution for detecting fake news using machine learning. It includes a trained model, a Flask API, a user interface for predictions, and a MySQL database for logging all requests. The entire project is dockerized for seamless deployment.

---

## Features

- **Machine Learning Model:** Trained using a dataset to classify news as real or fake.
- **Flask API:** Serves predictions via an endpoint.
- **Web Interface:** A simple UI for users to input news and view predictions.
- **Database Logging:** Tracks all predictions in a MySQL database.
- **Dockerized:** Easy deployment using `docker-compose`.

---

## Requirements

- Docker
- Docker Compose

---

## Quick Start

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. Run the application:
   ```bash
   docker-compose up
   ```

3. Access the application:
   - **Web Interface:** [http://localhost:5000](http://localhost:5000)
   - **API Endpoint:** [http://localhost:5000/predict](http://localhost:5000/predict)

---

## Project Structure

- **`notebooks/`**: Contains the notebook used to train the model.
- **`model/`**: Stores the pickled model (`model.pkl`).
- **`api/`**: Flask API for serving predictions.
- **`ui/`**: HTML and CSS for the user interface.
- **`db/`**: Database schema and MySQL configuration.
- **`docker-compose.yml`**: Orchestrates the services.
- **`Dockerfile`**: Configures the Docker image.

---

## API Usage

### Endpoint: `/predict`

- **Method:** POST
- **Payload:**
  ```json
  {
    "news": "Enter the news article text here"
  }
  ```
- **Response:**
  ```json
  {
    "prediction": "real" or "fake"
  }
  ```

---

## Database

- **Tracks Requests:** Logs predictions with timestamps.
- **Database:** MySQL
- **Schema:**
  - `id`: Auto-increment primary key
  - `news`: Text of the news article
  - `prediction`: Predicted label (real/fake)
  - `timestamp`: Time of the request

---

## Deployment

This project is fully containerized. To deploy:
- Clone the repo.
- Run `docker-compose up`.

---


