from application import app


@app.route("/")
@app.route("/index")
def index():
    return "<h1>Hello, You Beautiful Earth! version 2</h1>"
