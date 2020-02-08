from app import app


@app.route('/greet')
def index():
    return "Hello, World!"