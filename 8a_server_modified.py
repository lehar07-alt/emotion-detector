"""Flask server for emotion detection."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render home page."""
    result = None
    text_to_analyze = request.args.get("textToAnalyze")

    if text_to_analyze is not None:
        response = emotion_detector(text_to_analyze)

        if response["dominant_emotion"] is None:
            result = "Invalid text! Please try again!"
        else:
            result = (
                "For the given statement, the system response is "
                f"'anger': {response['anger']}, "
                f"'disgust': {response['disgust']}, "
                f"'fear': {response['fear']}, "
                f"'joy': {response['joy']}, "
                f"'sadness': {response['sadness']}. "
                f"The dominant emotion is "
                f"{response['dominant_emotion']}."
            )

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)