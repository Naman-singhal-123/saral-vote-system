# 🗳️ Saral Vote – Face Detection & Verification System

## 📌 Project Overview

Saral Vote is a smart virtual voting system that uses **Face Detection and Face Verification** to ensure that each voter can vote only once.
The system captures a user's face using a webcam and compares it with the stored dataset to verify identity before allowing voting.

This project is built using **Python, OpenCV, and DeepFace** and aims to demonstrate how biometric authentication can improve voting security.

---

## 🚀 Features

* 🎥 Real-time face detection using webcam
* 🧠 AI-based face verification using DeepFace
* 📂 Dataset-based identity matching
* 🔐 Prevents unauthorized voting
* ⚡ Simple and fast verification system

---

## 🛠️ Technologies Used

* **Python**
* **OpenCV**
* **DeepFace**
* **NumPy**

---

## 📂 Project Structure

```
saralvote/
│
├── dataset/
│   ├── user1.jpg
│   ├── user2.jpg
│   └── user3.jpg
│
├── face_detection.py
├── capture.jpg
└── README.md
```

---

## ⚙️ Installation

1️⃣ Clone the repository

```
git clone https://github.com/yourusername/saralvote.git
```

2️⃣ Move into the project directory

```
cd saralvote
```

3️⃣ Install required libraries

```
pip install opencv-python
pip install deepface
```

---

## ▶️ How to Run

Run the Python file:

```
python face_detection.py
```

Press **C** to capture the face and verify with the dataset.

Press **ESC** to exit.

---

## 🔄 Working Flow

```
Start Camera
      ↓
Capture Face
      ↓
Compare with Dataset
      ↓
Match Found → Verified
No Match → Access Denied
```

---

## 🔮 Future Improvements

* Integration with **database for voter records**
* **Face recognition instead of verification**
* **Web-based voting interface**
* **One person one vote security system**

---

## 👨‍💻 Author

**Naman Singhal**

* BCA Student (Computer Science)
* Python & Data Science Enthusiast

---

## ⭐ Support

If you like this project, please consider giving it a **star ⭐ on GitHub**.
