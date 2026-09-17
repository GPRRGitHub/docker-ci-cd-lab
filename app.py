from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <body style='font-family:Arial;text-align:center;margin-top:80px'>
        <h1>🚀 Production CI/CD</h1>
        <h2>GitHub Actions + Docker + EC2</h2>
        <p>Successfully deployed automatically!</p>
      </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status":"healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)