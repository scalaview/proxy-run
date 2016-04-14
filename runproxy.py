from flask import Flask, request
app = Flask(__name__)

@app.route("/run")
def proxy():
    filename = request.args.get('filename')
    if filename is None:
      filename = "./demo.py"
    variables = {}
    execfile(filename, variables )
    return "ok"

if __name__ == "__main__":
    app.run(debug=True)