# BridgeTheGap

# 🤟 Sign to Speech - AI-Based Assistive Communication Tool

## 📘 Project Overview
A real-time AI-powered system that recognizes **hand gestures from sign language** and converts them into **text and speech**, enabling seamless communication for individuals with speech and hearing impairments. The project specifically aims to cater to **Indian Sign Language (ISL)** recognition and bridge the accessibility gap in India.

---

## 🎯 Problem Statement
People with speech or hearing disabilities face constant communication barriers, especially in non-inclusive environments. Current solutions are limited, expensive, human-dependent, or not tailored to Indian Sign Language. Our solution offers an **affordable, real-time, and AI-driven sign-to-speech converter** to make communication smoother, faster, and more inclusive.

---

## 🚀 Goals & Objectives
- Enable **gesture-based communication** using computer vision.
- Convert **signs to text and then into audible speech**.
- Make it **real-time, lightweight, and deployable** on web/mobile platforms.
- Focus on **Indian Sign Language (ISL)** for regional relevance.

---

## 🧠 System Architecture
```
1. Input (Camera Feed)
        ↓
2. Hand Landmark Detection (MediaPipe/OpenCV)
        ↓
3. Gesture Classification Model (ML/DL)
        ↓
4. Text Mapping (Word/Sentence Construction)
        ↓
5. Text-to-Speech Output (gTTS / Google Cloud TTS)
        ↓
6. Audio Output (Speaker/Headphone)
```

---

## 🧩 Module-Wise Breakdown

### 🔸 Module 1: Input System
- Capture real-time camera feed using JS/OpenCV.
- Preprocess frames for recognition.

### 🔸 Module 2: Gesture Recognition
- Use **MediaPipe Hands** to detect 21 hand landmarks.
- Extract coordinates and features for classification.

### 🔸 Module 3: Sign Classification
- Train a model (CNN or CNN-LSTM) to classify gestures.
- Use **ISL datasets or custom collected dataset**.

### 🔸 Module 4: Text Mapping & Sentence Construction
- Collect a sequence of signs and form structured sentences using **basic NLP logic**.

### 🔸 Module 5: Text-to-Speech Converter
- Use **gTTS** or **Google TTS API** to convert text to audio output.

### 🔸 Module 6: Output Interface
- Display recognized text on screen.
- Play speech via audio output.
- Provide user controls (start/stop, clear, etc.)

---

## ⚙️ Tech Stack

| Category              | Tools/Frameworks                     | Purpose                                       |
|-----------------------|--------------------------------------|-----------------------------------------------|
| **Frontend**          | HTML, CSS, JavaScript, React         | UI interface, camera input, real-time feedback|
| **Vision Processing** | OpenCV, MediaPipe Hands              | Frame capture, landmark detection             |
| **ML/DL Framework**   | TensorFlow, Keras, PyTorch           | Training gesture recognition models           |
| **Text-to-Speech**    | gTTS, Google Cloud TTS               | Voice conversion of recognized text           |
| **Backend (optional)**| Flask / Node.js                      | Serve models and APIs                         |
| **Deployment**        | Streamlit, Web App (Flask or React)  | Hosting and demo                              |

---

## 👥 Team Role Distribution

| Team Member         | Role                                         |
|---------------------|-----------------------------------------------|
| Divyam (Team Leader)| System architecture, integration, pitch      |
| Member 1            | Frontend design + camera input integration    |
| Member 2            | Gesture recognition pipeline (MediaPipe/OpenCV)|
| Member 3            | Model training and dataset processing         |
| Member 4            | Text-to-speech & output system integration    |

---

## 📊 Dataset
- **Indian Sign Language (ISL) Fingerspelling Dataset**
- Option to build a **custom gesture dataset** using webcam
- Possible augmentation for accuracy improvement

---

## 📦 Tools & Libraries
- MediaPipe Hands / Pose
- OpenCV
- TensorFlow/Keras or PyTorch
- gTTS / Google Cloud TTS
- Streamlit / Flask / React (based on implementation needs)

---

## 🌱 Future Enhancements
- Reverse system: **Speech to Sign using avatars**
- Multilingual speech output (Hindi, Tamil, etc.)
- Facial expression analysis for emotion detection
- Mobile app version
- Context-aware NLP for intelligent responses
- Integration with assistive IoT devices (e.g., smart boards, alerts)

---

## 🏆 Unique Value Proposition
- **Tailored for Indian Sign Language**
- **Lightweight & Real-Time**
- **Low-cost, accessible solution**
- Can be integrated into schools, hospitals, banks, railway stations, etc.

---

## 📂 License
This project is developed for educational and assistive purposes. Contributions are not welcome yet!
All rights and reserves goes to Team Cyber Spartans.
