import base64
from flask import Flask, request
from PIL import Image
from io import BytesIO
from imageai.Detection import ObjectDetection
import os, json

app = Flask(__name__)
counter = 0
detector = None

#Function to load model
def loadmodel():
    global detector
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath("/notebook/fruit-detection/resnet50_coco_best_v2.0.1.h5")
    # Default mode is "normal"
    detector.loadModel() #detection_speed="fast"
    return detector

@app.route('/detection', methods=['POST'])
def dectect():
    # Request
    data = request.get_json(force=True)
    # Content of the image, Base64 format
    picture = data["image"]
    # This is input image name
    inputname = '/notebook/flask_app/upload/' + data["name"] + '.jpg'
    # This is for the response
    outputname = '/notebook/flask_app/output/' + data["name"] + '.jpg'
    # Decoding from Base64
    im = Image.open(BytesIO(base64.b64decode(picture)))
    # Save input image into JPEG format
    im.save(inputname, 'JPEG')
    print(inputname)
    print(outputname)
    
    # Detect and save the result as image
    global counter
    global detector 
    # To check if the model is loaded, if not, call loadmodel()
    # Otherwise, use the global object
    if detector == None:
        detector = loadmodel()
    detections = detector.detectObjectsFromImage(input_image=inputname, output_image_path=outputname)
    counter += 1
    
    detectionlist = []
    for eachObject in detections:
        dict={}        
        dict["name"] = eachObject["name"]
        dict["percentage_probability"] = eachObject["percentage_probability"]
        detectionlist.append(dict)
    print(detectionlist)
        
    with open(outputname, "rb") as img_file:
        imageString = base64.b64encode(img_file.read())
        
    outputdata = {}
    outputdata['image'] = str(imageString, 'utf-8')
    outputdata['content'] = detectionlist
    #print(outputdata)
    result = json.dumps(outputdata)
    return result

@app.route('/', methods=['GET','POST'])
@app.route('/test', methods=['GET','POST'])
def test():
    return "OK"

if __name__ == '__main__':
    #global detector
    #detector = loadmodel()
    app.run(host='0.0.0.0')
