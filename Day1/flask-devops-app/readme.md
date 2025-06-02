*What I built*

 The Application:

    Flask web server that responds "Hello, World!" on port 5000
    Health check endpoint at /health

The Container:

    Docker image containing Python + Flask + our app
    Portable package that runs the same everywhere

Key Components:
    app.py → Web application code
    Dockerfile → Container build instructions 
----------------------------------------------------

*Commands used*
 docker build -t flask-devops-app .
 docker run -p 5000:5000 flask-devops-app

----------------------------------------------------

*Modifications tried*
1.Change output message
     	In app.py:
return "Shushank – 27 May 2025 – Dockerized"
	
2.Add a /health route
	@app.route('/health')
def health():
    return { "status": "ok" }

3.Change Python version in Dockerfile to 3.10, rebuild, rerun.

4.Run app on port 8080 instead of 5000 
