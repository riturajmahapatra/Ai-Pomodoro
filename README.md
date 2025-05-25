# Ai-Pomodoro

ChatGPT FaceDetection --Start(facedetector.py)

- [ ] pip install opencv-python
- [ ] Haar Cascade Classifiers: A machine learning-based approach for object detection, particularly effective for identifying faces and eyes in images.
      CascadeClassifier & XML file is a pre-trained model. It knows how to spot patterns (like eyes, nose, mouth) using a technique called Haar Cascades.VideoCapture(0) 1. cv2.VideoCapture(0) opens your built-in webcam.2. If you plug in a USB webcam, it would be 1 or 2, etc.

cap.read() has 2 things 1. ret --- boolean ---(Did the camera work?) 2. frame --- the actual image of the camera

if the capture doent happen then

**_ Why we use grayscale? Why grayscale? _**

- [ ] Why grayscale?
      It only detects in gray and white
      Color images are 3D (Red, Green, Blue)
      Grayscale is simpler (just brightness)
      Haar Cascades were trained on grayscale images, not color
      Grayscale is also faster to process — less data

detectMultiScale(gray, 1.3, 5) --- MultiScale detects objects of different sizes in the input image and returns rectangles positioned on the faces.

// https://www.researchgate.net/publication/228412946_LAB_MANUAL-2D1427_Image_Based_Recognition_and_Classification

- [ ] -- Face Detection vs. Face Recognition --
      Face Detection : Only locates human faces in images or videos.
      Face Recognition : Verifies a person from a digital image or video frame.

- [ ] -- Viola-Jones Algorithm ---
      Haar-like Features: Simple rectangular features that encode the presence of edges or changes in texture.
      Integral Images: A data structure for rapid feature computation.
      AdaBoost: A machine learning algorithm that selects a small number of critical features and combines them into a strong classifier.
      Attentional Cascade: A series of increasingly complex classifiers applied sequentially to quickly discard non-face regions.

cap.release() this releases the camera otherwise webcam might stay "locked" and not be available to other apps.
