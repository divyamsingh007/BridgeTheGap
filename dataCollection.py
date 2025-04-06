import cv2
import mediapipe as mp
import numpy as np
import os

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Define base dataset folder
dataset_folder = "ISL_Gesture_Dataset"
os.makedirs(dataset_folder, exist_ok=True)

# Open webcam (0 for default camera, try 1 if not working)
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

    # Convert frame to RGB for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    x_min, y_min = frame.shape[1], frame.shape[0]
    x_max, y_max = 0, 0

    # Detect hands
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for landmark in hand_landmarks.landmark:
                x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])
                x_min, y_min = min(x_min, x), min(y_min, y)
                x_max, y_max = max(x_max, x), max(y_max, y)

            # Draw landmarks on frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Expand bounding box with margin
    margin = 20
    x_min, y_min = max(0, x_min - margin), max(0, y_min - margin)
    x_max, y_max = min(frame.shape[1], x_max + margin), min(frame.shape[0], y_max + margin)

    # Crop the region containing both hands
    hand_crop = frame[y_min:y_max, x_min:x_max]

    if hand_crop.shape[0] > 0 and hand_crop.shape[1] > 0:
        # Create a white background (224x224)
        final_image = np.ones((224, 224, 3), dtype=np.uint8) * 255  # White background

        # Resize the hand image while keeping the aspect ratio
        hand_h, hand_w = hand_crop.shape[:2]
        aspect_ratio = hand_w / hand_h

        if aspect_ratio > 1:  # Wider image
            new_w = 224
            new_h = int(224 / aspect_ratio)
        else:  # Taller image
            new_h = 224
            new_w = int(224 * aspect_ratio)

        hand_crop_resized = cv2.resize(hand_crop, (new_w, new_h), interpolation=cv2.INTER_AREA)

        # Paste the resized hand image onto the center of the white background
        y_offset = (224 - new_h) // 2
        x_offset = (224 - new_w) // 2
        final_image[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = hand_crop_resized

        # Show the processed image
        cv2.imshow("Processed Gesture", final_image)

    # Display the live camera feed
    cv2.imshow("Indian Sign Language Capture", frame)

    # Listen for key inputs
    key = cv2.waitKey(1) & 0xFF  # Ensure proper key detection

    if 65 <= key <= 90 or 97 <= key <= 122:  # If a letter key (A-Z, a-z) is pressed
        gesture_label = chr(key).upper()  # Convert to uppercase
        gesture_folder = os.path.join(dataset_folder, gesture_label)

        # Ensure the folder exists
        os.makedirs(gesture_folder, exist_ok=True)

        if final_image is not None:
            img_count = len(os.listdir(gesture_folder))  # Unique naming
            img_name = os.path.join(gesture_folder, f"gesture_{img_count}.jpg")
            cv2.imwrite(img_name, final_image)
            print(f"✅ Saved: {img_name} (224x224) for gesture {gesture_label}")
        else:
            print(f"⚠️ No valid hand detected for gesture {gesture_label}. Try again.")

    # Exit on 'ESC' key
    elif key == 27:
        break

# Release camera & close windows
camera.release()
cv2.destroyAllWindows()
