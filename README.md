# Text to MP3

A simple Flask application that converts text input into MP3 audio files using a text-to-speech engine.

## Features

-   Convert text to speech and download as MP3
-   Simple web interface for inputting text

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/krsahil8825/Text-To-MP3.git
    ```

2. Navigate to the project directory:

    ```bash
     cd Text-To-MP3
    ```

3. Create and activate a virtual environment (optional but recommended):

    ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required dependencies:

    ```bash
     pip install -r requirements.txt
    ```

5. Create a `.env` file in the root directory and add any necessary environment variables.

    ```.env
    # Example environment variable
    IS_DEBUG=True
    ```

6. Run the application:
    ```bash
     waitress-serve --listen=0.0.0.0:8000 app:app
    ```
