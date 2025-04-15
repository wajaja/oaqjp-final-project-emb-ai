# Import the Flask class from the flask module
from flask import Flask
from emotion_detection import emotion_detector

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector():
    text_to_analyze = request.args.get('text')
    if not text_to_analyze:
        return jsonify({"error": "Please provide text to analyze"}), 400
    
    try:
        analysis = emotion_detector(text_to_analyze)
        emotions = analysis['emotion_predictions'][0]['emotion']
        
        # Format the response
        response = {
            "anger": emotions['anger'],
            "disgust": emotions['disgust'],
            "fear": emotions['fear'],
            "joy": emotions['joy'],
            "sadness": emotions['sadness'],
            "dominant_emotion": max(emotions.items(), key=lambda x: x[1])[0]
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
        
@app.errorhandler(400)
def api_not_found(error):
    # This function is a custom error handler for 404 Not Found errors
    # It is triggered whenever a 404 error occurs within the Flask application
    return {"message": "None"}, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
