import cv2
import os
import time

# USER ID INPUT
user_id = input("Enter User ID: ")

# Dataset folder
dataset_path = r"C:\Users\hp\PycharmProjects\saralvote\dataset"
os.makedirs(dataset_path, exist_ok=True)

# Initialize camera
cap = cv2.VideoCapture(0)

# Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Timing for countdown
start_time = None
captured = False

# Parameters
box_size = 250  # center guide box size
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
start_x = frame_width // 2 - box_size // 2
start_y = frame_height // 2 - box_size // 2

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera not detected!")
        break

    frame = cv2.flip(frame, 1)  # mirror

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Draw center guide box
    cv2.rectangle(frame, (start_x, start_y), (start_x + box_size, start_y + box_size), (255, 0, 0), 2)

    for (x, y, w, h) in faces:
        # Draw detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Check if face is inside center box
        if x > start_x and y > start_y and (x + w) < (start_x + box_size) and (y + h) < (start_y + box_size):

            if start_time is None:
                start_time = time.time()

            elapsed = int(time.time() - start_time)
            remaining = 4 - elapsed

            if remaining > 0:
                cv2.putText(frame, f"Stay Still {remaining}s",
                            (30, 50),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 0, 255), 2)
            else:
                if not captured:
                    # Crop only face area with a small margin
                    margin = 20
                    x1 = max(x - margin, 0)
                    y1 = max(y - margin, 0)
                    x2 = min(x + w + margin, frame.shape[1])
                    y2 = min(y + h + margin, frame.shape[0])
                    face_img = frame[y1:y2, x1:x2]

                    # Resize face to 224x224 (DeepFace preferred)
                    face_img = cv2.resize(face_img, (224, 224))

                    # Save face image
                    file_name = os.path.join(dataset_path, f"{user_id}.jpg")
                    cv2.imwrite(file_name, face_img)

                    print(f"Face Captured Successfully: {file_name}")
                    captured = True

    cv2.imshow("Face Capture", frame)

    key = cv2.waitKey(1)
    if captured or key == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
