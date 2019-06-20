# food-detection
Food detection and recipe prediction

This is our study project to detect food, fruit from the image and predict the possible calories from those detected fruits, meals.

Our next target is to detect/predict the ingredients and possible recipe from any meal picture.

GitHub:
https://github.com/zithiat/food-detection

Notebook site:
http://35.232.18.220:8888/notebooks/fruit-detection/fruit-detection.ipynb

API
URL:
  http://35.232.18.220:5000/detection

Method: 
  POST

Header: 
  Content-Type:application/json

Request JSON body:
  {
	"image": "Content in Base64 format",
	"name": "Image name"
  }
  
Response JSON body:
  {
    "image": "Content in Base64 format",
    "name": "Image name"
    "content": "Array of the predicted classes and probability percentage"
    [
      {
        "name": "predicted class",
        "percentage_probability": float
      }
    ]
  }
