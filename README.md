# Repository for final project

Shell

import sys
sys.path.append('/Users/me/projects/myapp')

python3.11



from emotion_detection import emotion_detector

import json

result = emotion_detector("I love this new technology.")
print(json.dumps(result, indent=2))
