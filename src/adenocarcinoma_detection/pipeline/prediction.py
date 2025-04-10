
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self):
        ## load model
        
        model = load_model(os.path.join("artifacts","training", "model.h5"))
        # model = load_model(os.path.join("model", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image  /= 255. 
        
        test_image = np.expand_dims(test_image, axis = 0)
        
        
        
        output= model.predict(test_image)
        result = np.argmax(output, axis=1)
        
        print(output)
        
        print(result)
        if result[0] == 0:
            prediction = 'adenocarcinoma'
            return [{ "image" : prediction}]
        elif result[0] == 1:
            prediction = 'large.cell.carcinoma'
            return [{ "image" : prediction}]
        elif result[0] == 2:
            prediction = 'normal'
            return [{ "image" : prediction}]
        elif result[0] == 3:
            prediction = 'squamous.cell.carcinoma'
            return [{ "image" : prediction}]

