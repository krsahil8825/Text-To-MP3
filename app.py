import os
from flask import Flask, render_template, send_file
import dotenv


# Flask App Initialization
app = Flask(__name__)

# Load environment variables (from .env)
dotenv.load_dotenv()


def is_truthy(value: str) -> bool:
    """Helper to interpret common truthy environment variable values."""
    return str(value).lower() in {"true", "1", "t", "yes", "y"}


# Route
@app.route("/", methods=["GET"])
def home() -> str:
    """
    Home page for the QR code generator.
    """
    return render_template("index.html")


# Application Entry Point
if __name__ == "__main__":
    debug_mode = is_truthy(os.getenv("IS_DEBUG", "False"))
    host = os.getenv("FLASK_RUN_HOST", "0.0.0.0")
    port = int(os.getenv("FLASK_RUN_PORT", 5000))

    app.run(host=host, port=port, debug=debug_mode)
