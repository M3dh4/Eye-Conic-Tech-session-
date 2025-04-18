import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
canvas = None

prev_x, prev_y = 0, 0
drawing = False

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    if canvas is None:
        canvas = np.zeros_like(frame)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            lm_list = []
            h, w, _ = frame.shape

            for id, lm in enumerate(hand_landmarks.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((cx, cy))

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            index_tip_y = lm_list[8][1]
            index_mcp_y = lm_list[5][1]

            if index_tip_y < index_mcp_y:
                if not drawing:
                    prev_x, prev_y = lm_list[8]
                    drawing = True
                curr_x, curr_y = lm_list[8]
                cv2.line(canvas, (prev_x, prev_y), (curr_x, curr_y), (0, 0, 255), 4)
                prev_x, prev_y = curr_x, curr_y
            else:
                drawing = False

    frame = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)
    cv2.putText(frame, "Point to draw: Index up = DRAW", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

    cv2.imshow("One Finger Draw Mode", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
