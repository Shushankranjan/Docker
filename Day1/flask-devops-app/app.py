from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Shushank - 2 June 2025"

@app.route('/health')
def health():
    return {"status": "healthy", "message": "App is running"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)