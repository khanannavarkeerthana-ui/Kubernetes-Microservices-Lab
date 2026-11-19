from flask import Flask
import urllib.request

app = Flask(__name__)
CATALOG_URL = "http://catalog-service:5000/products"

@app.route("/")
def home():
    return '''
    <html>
      <head><title>Product Management Application</title></head>
      <body>
        <h1>Product Management Application</h1>
        <p>Frontend microservice is running.</p>
        <a href="/products">View Products</a>
      </body>
    </html>
    '''

@app.route("/products")
def products():
    try:
        with urllib.request.urlopen(CATALOG_URL, timeout=5) as response:
            return response.read(), response.status, {
                "Content-Type": response.headers.get("Content-Type", "application/json")
            }
    except Exception as error:
        return {"error": "Catalog service unavailable", "details": str(error)}, 503

@app.route("/health")
def health():
    return {"status": "healthy", "service": "frontend"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
