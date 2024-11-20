# Virtual-Dressing-Room-Using-OpenCV
## **Overview**  
The Virtual Dressing Room is an innovative application that allows users to try on virtual clothes using a webcam or camera. This project leverages OpenCV for image processing to detect the upper body and overlay virtual clothing in real-time.

---

## **Features**  
- **Real-Time Virtual Dressing**: Enables users to try on clothes virtually via a live video feed.  
- **Upper Body Detection**: Utilizes Haar Cascade Classifier for face and body part detection.  
- **Customizable Clothing Options**: Easily add new clothing images to the system.  

---

## **Requirements**  
To run the project, ensure you have the following installed:  
- **Python 3**  
- **OpenCV 4.1 or later**  
- **Haar Cascade File**: `haarcascade_frontalface_alt.xml` (included in the `data/haarcascades` folder).  
- Clothing images (e.g., `tshirt_1.png`)  

---

## **File Structure**  
```
Virtual Dressing Room/
│
├── data/
│   ├── haarcascades/
│   │   └── haarcascade_frontalface_alt.xml
│
├── img/
│   ├── tshirt_1.png
│
├── detection.py
├── main.py
└── README.md
```
---

## **Methodology**  
1. The webcam captures live video of the user.  
2. The Haar Cascade Classifier detects the user's face to position the upper body.  
3. The selected clothing image is resized and overlaid on the user's body in the video stream.  
4. The system handles background removal for seamless integration.

---

## **Customization**  
- To add more clothing options:  
  - Place the image files (e.g., `shirt_2.png`) in the `img/` folder.  
  - Update the file path in `detection.py`.  

---

## **Results**  
The project successfully overlays virtual clothing onto the user in real-time with high accuracy and smooth performance.

---

## **Future Enhancements**  
- Add support for multiple clothing options via a user interface.  
- Improve accuracy with advanced detection models like DNN-based frameworks.  
- Incorporate multi-angle clothing overlays for better realism.

---
