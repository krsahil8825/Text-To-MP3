import dotenv
from flask import Flask, render_template, request, send_file
from io import BytesIO
import os
import pyttsx3

# Flask App Initialization
app = Flask(__name__)

# Load environment variables
dotenv.load_dotenv()


def is_truthy(value: str):
    """Helper to interpret common truthy environment variable values."""
    return str(value).lower() in {"true", "1", "t", "yes", "y"}


@app.route("/", methods=["GET", "POST"])
def home():
    """
    Home route for text-to-speech conversion.
    GET -> Renders index.html
    POST -> Converts input text to speech and returns MP3 for download
    """
    if request.method == "POST":
        text = request.form.get("text", "").strip()
        voice_gender = request.form.get("voice", "female").lower()

        if not text:
            return "Error: No text provided", 400

        # Initialize pyttsx3 engine
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")

        # Set voice based on user input (default: female)
        if voice_gender == "male":
            engine.setProperty("voice", voices[0].id)  # usually male
        else:
            engine.setProperty("voice", voices[1].id)  # usually female

        # Use BytesIO to store the audio output
        audio_stream = BytesIO()
        engine.save_to_file(text, "temp_audio.mp3")
        engine.runAndWait()

        # Read back as bytes and delete the temp file
        with open("temp_audio.mp3", "rb") as f:
            audio_data = f.read()

        os.remove("temp_audio.mp3")

        # Send file as downloadable MP3 without saving permanently
        return send_file(
            BytesIO(audio_data),
            mimetype="audio/mpeg",
            as_attachment=True,
            download_name="speech.mp3",
        )

    return render_template("index.html")


@app.route("/about", methods=["GET"])
def about():
    """About route providing information about the application."""
    return render_template("about.html")


@app.route("/contact", methods=["GET"])
def contact():
    """Contact route providing a contact form."""
    return render_template("contact.html")


# Application Entry Point
if __name__ == "__main__":
    debug_mode = is_truthy(os.getenv("IS_DEBUG", "False"))
    host = os.getenv("FLASK_RUN_HOST", "0.0.0.0")
    port = int(os.getenv("FLASK_RUN_PORT", 5000))
    app.run(host=host, port=port, debug=debug_mode)
