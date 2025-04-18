import cv2

cap = cv2.VideoCapture(1) 

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    center_x, center_y = 320, 240
    face_radius = 100

    cv2.circle(frame, (center_x, center_y), face_radius, (0, 255, 255), -1)  
    cv2.circle(frame, (center_x - 35, center_y - 30), 15, (0, 0, 0), -1)  
    cv2.circle(frame, (center_x + 35, center_y - 30), 15, (0, 0, 0), -1)  

    cv2.ellipse(frame, (center_x, center_y + 20), (40, 20), 0, 0, 180, (0, 0, 0), 4)

    cv2.circle(frame, (center_x - 60, center_y + 10), 10, (147, 20, 255), -1)
    cv2.circle(frame, (center_x + 60, center_y + 10), 10, (147, 20, 255), -1)

    cv2.putText(frame, "Smile! You're on cam 😊", (30, 50),
                cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("Emoji Cam 🎥", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
