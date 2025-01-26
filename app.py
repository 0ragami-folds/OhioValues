from flask import Flask, render_template
from waitress import serve

app = Flask(__name__, static_folder="dist/static", template_folder="dist", static_url_path="/static")

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    return render_template("index.html")

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)
