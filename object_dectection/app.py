import numpy as np
import time
from PIL import Image
import streamlit as st 
import cv2
import numpy as np
MODEL = "./model/MobileNetSSD_deploy.caffemodel"
PROTOTXT = "./model/MobileNetSSD_deploy.prototxt.txt"

def process_image(image):
    blob = cv2.dnn.blobFromImage(
        cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5
    )
    net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)
    net.setInput(blob)
    detections = net.forward()
    return detections

def annotate_image(
        image, detections, confidence_threshold=0.5
    ):
    
    # loop over the detections
    (h, w) = image.shape[:2]
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        
        if confidence > confidence_threshold:
            # extract the index of the class label from the 'detections',
            # then compute the (x, y)-coordinates of the bounding box for
            # the object
            _ = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (start_x, start_y, end_x, end_y) = box.astype("int")
            cv2.rectangle(image, (start_x, start_y), (end_x, end_y), 70, 2)
    
    return image

def main():
    
    st.title("Object Dectection for Images")
    file = st.file_uploader('Upload Image', type = ['jpg','png','jpeg'])
    
    if st.button("Dectect") and file is not None:
        with st.spinner('Uploading image...'):
            time.sleep(3)
        st.success('Image uploaded successfully!')
        st.image(file, caption = "Uploaded Image")
        
        st.text("Processing image...")
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
        
        image = Image.open(file)
        image = np.array(image)
        detections = process_image(image)
        processed_image = annotate_image(image, detections)
        st.image(processed_image, caption="Processed Image")
        st.balloons()
        
if __name__ == "__main__":
    main()