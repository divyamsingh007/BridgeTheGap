import cv2
import mediapipe as mp
import numpy as np
import os
from tensorflow.keras.models import load_model

# Load model and labels
model = load_model("my_last_model.h5")
with open("my_labels.txt", "r") as f:
    labels = [line.strip() for line in f.readlines()]

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.9)
mp_drawing = mp.solutions.drawing_utils

# Optional save folder
dataset_folder = "ISL_Gesture_Dataset"
os.makedirs(dataset_folder, exist_ok=True)

# Open webcam
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("⚠️ Camera not detected! Try restarting or check permissions.")
    exit()

print("📸 Press a letter key (A-Z) to capture & save the gesture. Press 'ESC' to exit.")

while True:
    ret, frame = camera.read()
    if not ret:
        print("⚠️ Camera error! Exiting.")
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    x_min, y_min = frame.shape[1], frame.shape[0]
    x_max, y_max = 0, 0
    predicted_label = None
    confidence = 0

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for landmark in hand_landmarks.landmark:
                x = int(landmark.x * frame.shape[1])
                y = int(landmark.y * frame.shape[0])
                x_min = min(x_min, x)
                y_min = min(y_min, y)
                x_max = max(x_max, x)
                y_max = max(y_max, y)

            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Add margin
        margin = 20
        x_min, y_min = max(0, x_min - margin), max(0, y_min - margin)
        x_max, y_max = min(frame.shape[1], x_max + margin), min(frame.shape[0], y_max + margin)

        hand_crop = frame[y_min:y_max, x_min:x_max]

        if hand_crop.size > 0:
            # Resize to 64x64 RGB for model
            resized_rgb = cv2.resize(hand_crop, (64, 64), interpolation=cv2.INTER_AREA)

            # Show processed image
            cv2.imshow("Processed Gesture", resized_rgb)

            # Prediction preprocessing
            input_image = resized_rgb.astype('float32') / 255.0
            input_image = np.expand_dims(input_image, axis=0)  # Shape: (1, 64, 64, 3)

            try:
                predictions = model.predict(input_image)
                predicted_index = np.argmax(predictions)
                predicted_label = labels[predicted_index]
                confidence = predictions[0][predicted_index]

                # Show prediction on original frame
                cv2.putText(frame, f"{predicted_label} ({confidence*100:.1f}%)",
                            (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 255, 0), 2, cv2.LINE_AA)
            except Exception as e:
                print("❌ Prediction error:", e)

    # Show webcam output
    cv2.imshow("Indian Sign Language Capture", frame)

    key = cv2.waitKey(1) & 0xFF

    if 65 <= key <= 90 or 97 <= key <= 122:
        gesture_label = chr(key).upper()
        gesture_folder = os.path.join(dataset_folder, gesture_label)
        os.makedirs(gesture_folder, exist_ok=True)

        if 'resized_rgb' in locals():
            img_count = len(os.listdir(gesture_folder))
            img_name = os.path.join(gesture_folder, f"gesture_{img_count}.jpg")
            cv2.imwrite(img_name, resized_rgb)
            print(f"✅ Saved: {img_name} (64x64 RGB) for gesture {gesture_label}")
        else:
            print(f"⚠️ No valid hand detected for gesture {gesture_label}. Try again.")

    elif key == 27:  # ESC
        break

# Clean up
camera.release()
cv2.destroyAllWindows()
