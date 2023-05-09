from flask import Flask, request, jsonify
import os
from pathlib import Path
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import text
from mediapipe.tasks.python import vision

app = Flask(__name__)


BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
VisionRunningMode = mp.tasks.vision.RunningMode


@app.route('/')
def hello():
    print('HIITTT!!!!')
    print('----------')
    return 'Hello, World!'


#add a route that handles an image upload
@app.route('/api/handLandmarksRecognition', methods=['POST'])
def gestureRecognition():
    print('hit')
    print('1----------')
    print(request);
    print('2----------')
    print(request.files)
    print('3----------')
    print(request.json_module)
    print('4----------')
    if 'image' not in request.files:
        print('this error :/')
        return jsonify({'error': 'No image provided'}), 400
    print('this is the request')
    for f in request.files:
        print('loop')
        print(f)
    file = request.files['image']
    print('herer')
    print(file)
    return 'done123'


# mp_face_detection = mp.solutions.face_detection
# mp_drawing = mp.solutions.drawing_utils

# @app.route('/api/textClassification', methods=['POST'])
# def facial_landmarks():
#     print(request.get_json())
#     myPath = Path("./src/models/bert_text_classifier.tflite")
#     INPUT_TEXT = request.get_json()['data']
#     base_options = python.BaseOptions(model_asset_path=myPath)
#     options = text.TextClassifierOptions(base_options=base_options)

#     classifier = text.TextClassifier.create_from_options(options)
#     classification_result = classifier.classify(INPUT_TEXT)

#     # STEP 4: Process the classification result. In this case, print out the most likely category.
#     top_category = classification_result.classifications[0].categories[0]
#     print(f'{top_category.category_name} ({top_category.score:.2f})')
#     return {"name": top_category.category_name, "score": top_category.score}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))