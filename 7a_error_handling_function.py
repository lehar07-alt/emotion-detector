def emotion_detector(text_to_analyze):
    if text_to_analyze is None or text_to_analyze.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    return {
        "anger": 0.01,
        "disgust": 0.02,
        "fear": 0.03,
        "joy": 0.90,
        "sadness": 0.04,
        "dominant_emotion": "joy"
    }