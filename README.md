# Text-to-MP3

A lightweight Flask web application that converts user-entered text into MP3 audio using an offline text-to-speech engine.
Easily convert any text to natural-sounding speech — no external APIs or internet connection required.

## Features

-   **Offline Text-to-Speech (TTS):** Uses `pyttsx3` for high-quality voice synthesis.
-   **Voice Options:** Choose between male and female voices.
-   **Instant Download:** Generates and downloads the speech as an `.mp3` file instantly.
-   **Completely Offline:** Works securely without internet or third-party APIs.
-   **Extensible Codebase:** Built with Flask — easy to extend or integrate with other projects.

## Installation & Setup

Follow these steps to set up and run the project:

### 1. Clone the Repository

```bash
git clone https://github.com/krsahil8825/text-to-mp3.git
```

### 2. Navigate into the Project Directory

```bash
cd text-to-mp3
```

### 3. Create and Activate a Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
```

Activate it:

-   **On macOS/Linux**

    ```bash
    source venv/bin/activate
    ```

-   **On Windows**

    ```bash
    venv\Scripts\activate
    ```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root directory and add the following:

```bash
# Example configuration
IS_DEBUG=True
FLASK_RUN_HOST=0.0.0.0
FLASK_RUN_PORT=5000
```

### 6. Run the Application

You can run the app using either **Waitress** (for production) or Flask (for development).

#### Option 1: Using Waitress (Recommended for Production)

```bash
waitress-serve --listen=0.0.0.0:8000 app:app
```

After starting the app, open your browser and go to:
**[http://localhost:8000](http://localhost:8000)**

#### Option 2: Using Flask (For Development)

```bash
python app.py
```

After starting the app, open your browser and go to:
**[http://localhost:5000](http://localhost:5000)**

## Project Structure

```
text-to-mp3/
├── app.py               # Main Flask application
├── templates/
│   ├── index.html       # Home page
│   ├── about.html       # About page
│   └── contact.html     # Contact page
├── static/              # CSS, JS, and static assets
├── requirements.txt     # List of dependencies
├── .env.example         # Example environment variables
└── README.md            # Project documentation
```

## Environment Variables

| Variable Name    | Type | Default | Description                           |
| ---------------- | ---- | ------- | ------------------------------------- |
| `IS_DEBUG`       | bool | False   | Enables or disables Flask debug mode. |
| `FLASK_RUN_HOST` | str  | 0.0.0.0 | Host address for the Flask server.    |
| `FLASK_RUN_PORT` | int  | 5000    | Port number for the Flask server.     |

## Example Usage

**Input:**

```
Hello, I’m using the Text-to-MP3 app by Kumar Sahil!
```

**Output:**
Downloads a file named `speech.mp3` containing the spoken version of the text.

## Tech Stack

-   **Python 3.9+**
-   **Flask** — Web framework
-   **pyttsx3** — Offline text-to-speech engine
-   **python-dotenv** — Environment variable management
-   **Waitress** — WSGI server for production deployment

## Contributing

Contributions, issues, and feature requests are welcome.
To contribute, fork the repository and submit a pull request.

```bash
git checkout -b feature/my-feature
git commit -m "Add my feature"
git push origin feature/my-feature
```

Please ensure your code follows **PEP 8** guidelines and includes clear docstrings.

## License

This project is licensed under the **MIT License**.
See the [LICENSE](LICENSE) file for full details.

## Author

[**GitHub: Kumar Sahil**](https://github.com/krsahil8825)

## Acknowledgements

-   [Flask](https://flask.palletsprojects.com/) — Lightweight web framework
-   [pyttsx3](https://pyttsx3.readthedocs.io/) — Offline text-to-speech library for Python
-   [Waitress](https://docs.pylonsproject.org/projects/waitress/) — Production-ready WSGI server

> “Turn your words into sound — Text-to-MP3 brings your text to life.”

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.