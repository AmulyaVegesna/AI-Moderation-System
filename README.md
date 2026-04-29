# 🧠 AI Social Media Moderation System

🚀 A full-stack AI application that detects toxic content in real-time, assigns severity scores, and automates moderation decisions — inspired by modern social media platforms.

---

## 🌐 Live Demo

🔗 **Frontend (Vercel):**
👉 ai-moderation-system-nine.vercel.app

🔗 **Backend API (Render):**
👉 https://ai-service-kkl5.onrender.com

---

## ✨ Highlights

* ⚡ Real-time text moderation
* 🧠 ML-based toxicity detection
* 📊 Severity scoring (0–100%)
* 🚫 Automated moderation (Block / Allow)
* 🗄️ Persistent storage with MongoDB Atlas
* 📋 Admin dashboard for monitoring posts
* ☁️ Fully deployed cloud architecture

---

## 🏗️ Architecture

```id="fw6rq8"
User → React Frontend (Vercel)
        ↓
Flask Backend API (Render)
        ↓
ML Model (TF-IDF + Logistic Regression)
        ↓
MongoDB Atlas (Cloud Database)
```

---

## 🧠 How It Works

1. User enters text in the UI
2. Frontend sends request to Flask API
3. Backend processes text using ML model
4. Model predicts toxicity and generates a score
5. Backend assigns:

   * Category (Toxic / Safe)
   * Action (Block / Allow)
6. Data is stored in MongoDB
7. Dashboard displays moderation history

---

## 📊 Example Output

```json id="85j21c"
{
  "text": "you are stupid",
  "score": 59,
  "category": "toxic",
  "action": "Block"
}
```

---

## 🧰 Tech Stack

### Frontend

* React.js
* Axios

### Backend

* Flask (Python)
* Flask-CORS

### Machine Learning

* Scikit-learn
* TF-IDF Vectorizer
* Logistic Regression

### Database

* MongoDB Atlas

### Deployment

* Vercel (Frontend)
* Render (Backend)

---

## 🧠 Model Details

* Text is transformed using **TF-IDF vectorization**
* Classified using **Logistic Regression**
* Probability converted into **severity score (%)**

⚠️ Note:
This model is a lightweight prototype. The architecture supports scaling to advanced NLP models like BERT.

---

## 📁 Project Structure

```id="vtz6tp"
AI-Moderation-System/
│
├── frontend/        # React app
├── ai-service/      # Flask backend + ML model
├── model.pkl        # Trained ML model
├── vectorizer.pkl   # TF-IDF vectorizer
└── README.md
```

---

## 🔌 API Endpoints

### POST `/analyze`

Analyze text

### GET `/posts`

Retrieve all moderated posts

### DELETE `/delete/<text>`

Delete a post

---

## 🚀 Local Setup

### Clone repository

```bash id="t6n5sa"
git clone https://github.com/your-username/AI-Moderation-System.git
cd AI-Moderation-System
```

### Backend

```bash id="1hm6o1"
cd ai-service
pip install -r requirements.txt
python app.py
```

### Frontend

```bash id="64njr1"
cd frontend
npm install
npm start
```

---

## 📈 Future Enhancements

* 🤖 Integrate Transformer models (BERT, HuggingFace)
* 📊 Advanced analytics dashboard
* 🔄 Auto-refresh + live updates
* 🗑️ Delete moderation entries from UI
* 🔍 Multi-label classification (hate, spam, abuse)
* 🔐 Authentication system

---

## 💡 What I Learned

* Integrating ML models into full-stack applications
* Designing REST APIs for real-time systems
* Deploying scalable apps using cloud services
* Managing state and async calls in React
* Handling cross-origin requests (CORS)

---

## 👩‍💻 Author

**Amulya Vegesna**

---

## ⭐ Support

If you found this project interesting, consider giving it a ⭐ on GitHub!
