"""Flask server for emotion detection using Watson NLP API."""
from flask import Flask, request
import requests

app = Flask(__name__)

WATSON_URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
    "Content-Type": "application/json"
}

def format_emotion_response(emotions):
    """Format emotion scores into readable text."""
    dominant = max(emotions.items(), key=lambda x: x[1])[0]
    return (
        "For the given statement, the system response is:\n"
        f"• Anger: {emotions['anger']:.3f}\n"
        f"• Disgust: {emotions['disgust']:.3f}\n"
        f"• Fear: {emotions['fear']:.3f}\n"
        f"• Joy: {emotions['joy']:.3f}\n"
        f"• Sadness: {emotions['sadness']:.3f}\n"
        f"\nThe dominant emotion is {dominant}."
    )

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector():
    """Analyze text for emotions and return results."""
    text_to_analyse = request.args.get('text')
    if not text_to_analyse:
        return "Error: Please provide text to analyze", 400
    
    try:
        payload = {"raw_document": {"text": text_to_analyse}}
        response = requests.post(WATSON_URL, headers=HEADERS, json=payload, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Debug: Print full response
        print("API Response:", data)
            
        emotions = data['emotionPredictions'][0]['emotion']
        return format_emotion_response(emotions), 200
        
    except requests.exceptions.RequestException as err:
        return f"Error: Failed to connect to emotion service - {str(err)}", 500
    except (KeyError, IndexError) as err:
        return f"Error: Malformed API response - {str(err)}", 500
    except Exception as err:
        return f"Unexpected error: {str(err)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
