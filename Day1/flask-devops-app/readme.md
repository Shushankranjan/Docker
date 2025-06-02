What I Built
The Application

    A Flask web server that responds with "Hello, World!" on port 5000.

    Health check endpoint available at /health.

The Container

    A Docker image containing Python, Flask, and the application.

    Portable and consistent environment that runs the app identically everywhere.

Key Components

    app.py — Flask web application code.

    Dockerfile — Instructions to build the Docker container.

Commands Used

docker build -t flask-devops-app .
docker run -p 5000:5000 flask-devops-app

Modifications Tried

    Change output message
    In app.py:

return "Shushank – 27 May 2025 – Dockerized"

Add a /health route

@app.route('/health')
def health():
    return { "status": "ok" }

Change Python version in Dockerfile to 3.10, then rebuild and rerun.

Run the app on port 8080 instead of 5000.
