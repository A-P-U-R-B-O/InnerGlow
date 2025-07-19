# 🌟 InnerGlow

**Your virtual mental health assistant, powered by Gemini AI**

---

InnerGlow is a modern, open-source web app designed to support your mental wellbeing. With conversational support, mood tracking, and secure journaling, InnerGlow is a safe space to reflect, grow, and glow from within.

![InnerGlow Screenshot](demo-screenshot.png)

## ✨ Features

- **Conversational AI:** Chat with InnerGlow about your feelings, thoughts, and challenges.
- **Mood Tracking:** Log your mood daily and visualize your emotional journey.
- **Secure Journaling:** Write and reflect in a private journal.
- **Context-Aware Insights:** Get gentle, personalized tips and encouragement.
- **Beautiful Interface:** Thoughtful design, calming colors, and responsive layout.
- **Fast & Modern Stack:** Powered by FastAPI (Python) and React (JS).

---

## 🚀 Quick Start

### 1. **Clone the repo**

```bash
git clone https://github.com/A-P-U-R-B-O/innerglow.git
cd innerglow
```

### 2. **Backend Setup (FastAPI)**

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

### 3. **Frontend Setup (React)**

```bash
cd ../frontend
npm install
npm start
```
The app runs locally at `http://localhost:3000` (frontend) and `http://localhost:8000` (backend).

> **Tip:** The frontend expects the API at `REACT_APP_API_URL`, defaulting to `http://localhost:8000`.  
> For cloud deploys, set this in your environment.

---

## 🌐 Deployment

This app is ready for [Render](https://render.com) or similar platforms!

See [`render.yaml`](./render.yaml) for cloud deployment.

---

## 🖼️ Screenshots

![Chat with InnerGlow](screenshots/chat.png)
![Mood Tracker](screenshots/mood.png)
![Journal](screenshots/journal.png)

---

## 🛠️ Tech Stack

- **Frontend:** React 18, CSS (Inter font, responsive design)
- **Backend:** FastAPI, Uvicorn, Pydantic
- **API:** Modular REST endpoints (`assistant`, `mood`, `journal`, etc.)
- **Cloud:** Render.yaml for instant deploy

---

## 🧑‍💻 Development

- **Backend:** See [`backend/main.py`](backend/main.py)
- **Frontend:** See [`frontend/src/`](frontend/src/)
- **Env:** Use `.env` for secrets and config

### Folder Structure

```
innerglow/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── ...
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── ChatBox.jsx
│   │   ├── AssistantInfo.jsx
│   │   ├── api.js
│   │   ├── styles.css
│   │   └── ...
│   ├── public/
│   │   └── index.html
│   ├── package.json
│   └── ...
├── render.yaml
├── README.md
└── ...
```

---

## 💡 Philosophy

> **InnerGlow is not a substitute for professional medical advice or crisis support.**  
> It’s a gentle space for support, reflection, and personal growth.

---

## 📝 License

MIT

---

## 👨‍🎨 Author

Made with care by [A-P-U-R-B-O](https://github.com/A-P-U-R-B-O)

---

## 🤝 Contributing

Pull requests and ideas are welcome!  
See [issues](https://github.com/A-P-U-R-B-O/innerglow/issues) for features and bugs.

---

## ⭐️ Give Yourself Permission to Glow

Enjoy InnerGlow!  
Feel free to share feedback, star the repo, and help others shine.
