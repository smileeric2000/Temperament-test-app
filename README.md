# 🧠 Temperament Test – Streamlit App

Welcome to the **Temperament Test App** built with Streamlit! This app allows users to assess their temperament based on a short, structured questionnaire. The results provide insight into their dominant personality traits, along with helpful tips.

---

## 📌 App Features & Structure

### 1️⃣ Intro Page
- A welcoming introduction that explains what the temperament test is about.
- Briefly describes the purpose: to help users better understand themselves.

### 2️⃣ Questionnaire
- A series of **20 multiple-choice questions**.
- Each question is designed to assess tendencies across the four classical temperaments:
  - **Sanguine**
  - **Choleric**
  - **Melancholic**
  - **Phlegmatic**
- Users answer via **radio buttons** or **select options**.

### 3️⃣ Score Processing
- Behind the scenes, each answer is mapped to one or more temperaments.
- The app **tallies the scores** and determines which temperament(s) dominate.

### 4️⃣ Result Display
- The user's **dominant temperament** is displayed.
- Includes a **brief personality description** tailored to their result.
- May also provide additional context if multiple temperaments are close in score.

### 5️⃣ (Optional) Downloadable Report
- Users can optionally download:
  - A **PDF or text report** summarizing their answers and result.
  - **Tips or recommendations** based on their temperament.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Streamlit

### Installation

```bash
pip install streamlit
