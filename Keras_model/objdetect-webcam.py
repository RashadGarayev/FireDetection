
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import cv2
import numpy as np
import sys
from keras.preprocessing import image

danger = ['fire','smoke']
def detect(frame):
    models = load_model('model/firesmoke_model.h5')
    roi = cv2.resize(frame, (150, 150))
    roi = roi.astype('float')/255.0
    roi = img_to_array(roi)
    roi = np.expand_dims(roi, axis=0)
    preds = models.predict(roi)[0]
    probability = np.argmax(preds)
    label = danger[probability]
    
    if label ==0:
		
    
        cv2.putText(frame, 'fire', (0, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 0), 1)
    elif label ==1:
        cv2.putText(frame, 'smoke', (0, 40),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 0), 1)
		
   
    return frame



video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    canvas = detect(frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
