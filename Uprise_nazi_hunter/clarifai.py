from clarifai import rest
from clarifai.rest import ClarifaiApp

app = ClarifaiApp("M0ytZ-ulTpWGpY9zCtZHea-VPJQRe4I4onV_5tAe", "WVDAYcncI5DozDkEJUiMFgNRoFgaWjQyJqrCS1wm")

model = app.models.get("general-v1.3")

model.predict_by_url(url='http://www.so-rummet.se/sites/default/files/nu_och_da/nazisternas-hakkors.gif')