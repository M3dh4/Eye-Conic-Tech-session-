# Eye-Conic-Tech-session-

A collection of fun computer vision scripts and meme images.  
**Dependencies:**  
- Python 3  
- [OpenCV](https://pypi.org/project/opencv-python/) (`pip install opencv-python`)  
- [MediaPipe](https://pypi.org/project/mediapipe/) (`pip install mediapipe`)  
- [Ultralytics YOLO](https://pypi.org/project/ultralytics/) (`pip install ultralytics`) (for YOLO script)

---

## Files & What They Do

| File Name                | What it Does                                                                 | Extra Dependencies      |
|--------------------------|------------------------------------------------------------------------------|------------------------|
| **draw_with_hands.py**   | Draws on the webcam feed using your finger (hand tracking).                  | mediapipe, opencv      |
| **drawing_with_code.py** | Shows a live webcam feed with a smiley face/emoji drawn on it.               | opencv                 |
| **face_coolers_1.py**    | Puts pixel sunglasses (“deal with it” style) on your face using webcam.      | mediapipe, opencv, numpy |
| **face_detect_demo.py**  | Similar to above, overlays sunglasses on your face via face mesh detection.  | mediapipe, opencv, numpy |
| **image_loader.py**      | Loads and displays an image in a popup window.                               | opencv                 |
| **livevideo_loader.py**  | Opens your webcam and shows the live video feed.                             | opencv                 |
| **yolo_object_detection.py** | Runs YOLO object detection on your webcam feed and draws boxes/labels.   | ultralytics, opencv    |

---

## Images

- **Testing_-removebg-preview.jpg**: The “deal with it” sunglasses overlay used in the face scripts.
- **2.jpg**: Meme image with cats, just for fun.

---

## How to Run

1. Install dependencies:
    ```bash
    pip install opencv-python mediapipe ultralytics numpy
    ```
2. Run any script you want:
    ```bash
    python draw_with_hands.py
    ```
    (Or replace with the script name you want.)

