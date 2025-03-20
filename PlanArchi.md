## 📐 Project Architecture

```
Frontend (React/HTML)
        ⇅
Node.js Backend (Express)
        ⇅
Python ML Engine (OpenCV + MediaPipe + Model)
        ⇅
Text-to-Speech (gTTS/pyttsx3)
```

---

## 📅 14-Day Development Plan

### Week 1 – Core Foundation + Dataset + ML Model

| Day | Focus | Tasks |
|------|--------|----------------------------|
| Day 1 | Project Blueprint | Setup architecture, GitHub, folder structure |
| Day 2 | Python Basics | Learn Python, OpenCV, MediaPipe |
| Day 3 | Dataset Collection | Capture hand gesture data A-Z |
| Day 4 | Model Training | Train gesture classifier (KNN/SVM/MLP) |
| Day 5 | Node.js Backend | Learn Express.js, setup server routes |
| Day 6 | Python-Node Integration | Bridge Python ML script to Node using `child_process` |
| Day 7 | Buffer/Debug | Finalize working flow end-to-end |

### Week 2 – Frontend, TTS, Final Polish

| Day | Focus | Tasks |
|------|--------|----------------------------|
| Day 8 | Text-to-Speech | Integrate gTTS or pyttsx3 |
| Day 9 | Frontend | Design UI using HTML/CSS or React |
| Day 10 | Frontend-Backend Link | Connect frontend to Express API |
| Day 11 | String Builder Logic | Create buffer string system |
| Day 12 | Testing | Cross-platform testing, bug fixing |
| Day 13 | Deployment | Optional: Deploy backend (Render/Glitch) |
| Day 14 | Final Prep | Demo video, pitch deck, final rehearsals |

---

## 📁 Folder Structure

```
sign-to-speech/
├── backend/ (Node.js)
│   ├── routes/
│   ├── controllers/
│   ├── ml-invoke.js (calls Python)
│   └── server.js
├── frontend/
│   ├── index.html / React files
│   └── style.css / assets
├── ml-engine/
│   ├── model.pkl
│   ├── predict.py
│   └── speak.py
└── dataset/
    └── A-Z CSVs
```

---
