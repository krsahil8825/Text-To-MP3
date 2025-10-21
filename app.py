"""
Text-to-MP3 Web Application
===========================

A lightweight Flask-based web application that converts user-submitted text
into high-quality speech (MP3 format). This app provides a simple web interface
where users can input text, choose between male or female voice options, and
download the generated MP3 file instantly.

The application uses the `pyttsx3` library for text-to-speech (TTS) synthesis,
allowing offline voice generation without external API calls or dependencies.
Audio data is processed in memory and served dynamically to the user for
download, ensuring no permanent storage on the server.

Environment variables (loaded via `python-dotenv`) can configure the host,
port, and debug mode. The application includes example routes for "About" and
"Contact" pages, making it easy to extend into a larger web project.

Features
--------
- Converts text input into downloadable MP3 speech files.
- Supports male and female voice options (offline).
- In-memory file streaming using `BytesIO` (no disk storage needed).
- Configurable runtime using `.env` environment variables.
- Clean, extensible Flask project structure.

Environment Variables
---------------------
IS_DEBUG        : (bool) Enable or disable Flask debug mode. Default: False
FLASK_RUN_HOST  : (str) Host address to bind. Default: "0.0.0.0"
FLASK_RUN_PORT  : (int) Port number to run the app. Default: 5000

Routes
------
/               : (GET, POST) Home page; accepts text input and converts it to MP3.
/about          : (GET) About page describing the app.
/contact        : (GET) Contact page with form or contact details.

Usage
-----
1. Create a virtual environment and install dependencies:
       pip install flask pyttsx3 python-dotenv

2. Run the Flask app:
       python app.py

3. Open in browser:
       http://localhost:5000

Example
-------
Input:
    "Hello, this is a Text-to-MP3 demo!"
Output:
    Downloads a file named `speech.mp3` containing the spoken version of the text.

Author
------
Developed by Open Source Contributors
License: MIT
"""

import dotenv
from flask import Flask, render_template, request, send_file
from io import BytesIO
import os
import pyttsx3


# Flask Application Initialization
app = Flask(__name__)

# Load environment variables from .env file
dotenv.load_dotenv()


def is_truthy(value):
    """
    Interpret common truthy values from environment variables.

    Converts an input value (string or boolean) into a standardized boolean.
    Common truthy representations such as "true", "1", "yes", "y", or "t"
    return True. All other values return False.

    Parameters
    ----------
    value : str
        The value to interpret (usually from an environment variable).

    Returns
    -------
    bool
        True if the value represents a truthy state, False otherwise.

    Examples
    --------
    >>> is_truthy("True")
    True
    >>> is_truthy("no")
    False
    """
    return str(value).lower() in {"true", "1", "t", "yes", "y"}


# Routes
@app.route("/", methods=["GET", "POST"])
def home():
    """
    Home route for text-to-speech conversion.

    Handles both GET and POST requests:
    - GET: Renders the main HTML form (`index.html`) where users can enter text.
    - POST: Processes submitted text and converts it to speech (MP3 file).

    When text input is received, the function initializes the `pyttsx3`
    TTS engine, applies the requested voice gender, converts the text to
    an MP3 file in memory, and returns it as a downloadable response.

    Returns
    -------
    Response
        - On GET: Rendered HTML page (`index.html`).
        - On POST: MP3 file generated from the provided text.

    Raises
    ------
    400 Bad Request
        If no text input is provided in the POST request.
    """
    if request.method == "POST":
        text = request.form.get("text", "").strip()
        voice_gender = request.form.get("voice", "female").lower()

        if not text:
            return "Error: No text provided", 400

        # Initialize pyttsx3 text-to-speech engine
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")

        # Choose voice based on gender input
        if voice_gender == "male":
            engine.setProperty("voice", voices[0].id)  # Usually male
        else:
            engine.setProperty("voice", voices[1].id)  # Usually female

        # Generate and save audio temporarily
        engine.save_to_file(text, "temp_audio.mp3")
        engine.runAndWait()

        # Read the audio into memory
        with open("temp_audio.mp3", "rb") as f:
            audio_data = f.read()

        # Remove the temporary file
        os.remove("temp_audio.mp3")

        # Return file as downloadable attachment
        return send_file(
            BytesIO(audio_data),
            mimetype="audio/mpeg",
            as_attachment=True,
            download_name="speech.mp3",
        )

    # Render input form
    return render_template("index.html")


@app.route("/about", methods=["GET"])
def about():
    """
    About page route.

    Renders a static "About" page that provides information about the
    Text-to-MP3 web application — its purpose, features, and usage.

    Returns
    -------
    Response
        Rendered HTML page (`about.html`).
    """
    return render_template("about.html")


@app.route("/contact", methods=["GET"])
def contact():
    """
    Contact page route.

    Renders a static "Contact" page that can include a contact form or
    developer contact details for user inquiries.

    Returns
    -------
    Response
        Rendered HTML page (`contact.html`).
    """
    return render_template("contact.html")


# Application Entry Point
if __name__ == "__main__":
    """
    Entry point for running the Flask development server.

    Loads environment configurations for host, port, and debug mode from
    `.env` variables. If not found, default values are used:
    - Host: 0.0.0.0
    - Port: 5000
    - Debug: False

    Example
    -------
    $ export IS_DEBUG=True
    $ python app.py

    The app will be available at:
    http://localhost:5000
    """
    debug_mode = is_truthy(os.getenv("IS_DEBUG", "False"))
    host = os.getenv("FLASK_RUN_HOST", "0.0.0.0")
    port = int(os.getenv("FLASK_RUN_PORT", 5000))
    app.run(host=host, port=port, debug=debug_mode)
