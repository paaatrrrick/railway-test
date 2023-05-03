from flask import Flask
from flask import request
import os
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import text
from pathlib import Path


app = Flask(__name__)

print('This is a test!!!!!!!')

@app.route('/')
def hello():
    print('we have been hit')
    return 'Hello, World!'

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

@app.route('/api/textClassification', methods=['POST'])
def facial_landmarks():
    print(request.get_json())
    myPath = Path("./src/models/bert_text_classifier.tflite")
    INPUT_TEXT = request.get_json()['data']
    base_options = python.BaseOptions(model_asset_path=myPath)
    options = text.TextClassifierOptions(base_options=base_options)

    classifier = text.TextClassifier.create_from_options(options)
    classification_result = classifier.classify(INPUT_TEXT)

    # STEP 4: Process the classification result. In this case, print out the most likely category.
    top_category = classification_result.classifications[0].categories[0]
    print(f'{top_category.category_name} ({top_category.score:.2f})')
    return {"name": top_category.category_name, "score": top_category.score}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))