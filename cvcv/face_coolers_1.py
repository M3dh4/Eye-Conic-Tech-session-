import cv2
import mediapipe as mp
import numpy as np

overlay_img = cv2.imread("Eye-Conic-Tech-session-/cvcv/Testing_-removebg-preview.png", cv2.IMREAD_UNCHANGED)

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True)

cap = cv2.VideoCapture(1) 

def overlay_transparent(background, overlay, x, y, overlay_size=None):
    if overlay_size:
        overlay = cv2.resize(overlay, overlay_size)

    h, w = overlay.shape[0], overlay.shape[1]

    if x + w > background.shape[1] or y + h > background.shape[0] or x < 0 or y < 0:
        return background

    overlay_rgb = overlay[..., :3]
    mask = overlay[..., 3:] / 255.0

    roi = background[y:y+h, x:x+w]
    background[y:y+h, x:x+w] = (roi * (1 - mask) + overlay_rgb * mask).astype(np.uint8)
    return background

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            h, w, _ = frame.shape

            # Get landmarks for both eye corners
            left_eye = face_landmarks.landmark[33]
            right_eye = face_landmarks.landmark[263]

            x1 = int(left_eye.x * w)
            y1 = int(left_eye.y * h)
            x2 = int(right_eye.x * w)
            y2 = int(right_eye.y * h)

            # Compute center between eyes
            eye_center_x = int((x1 + x2) / 2)
            eye_center_y = int((y1 + y2) / 2)

            # Width between eyes
            glasses_width = int(1.5 * abs(x2 - x1))
            glasses_height = int(glasses_width * overlay_img.shape[0] / overlay_img.shape[1])

            # Top-left coordinates for overlay
            x = eye_center_x - glasses_width // 2
            y = eye_center_y - glasses_height // 2

            # Overlay coolers
            frame = overlay_transparent(frame, overlay_img, x, y, (glasses_width, glasses_height))
    else:
        cv2.putText(frame, "No face detected", (30, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Coolers Cam 😎", frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()
