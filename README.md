# 🚰 AquaGuardian AI

> **An AI-Powered Multi-Agent Water Quality Analysis System built with Google Gemini and Streamlit**

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red)
![Google Gemini](https://img.shields.io/badge/Google-Gemini_AI-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📖 Overview

AquaGuardian AI is an intelligent Multi-Agent AI system that analyzes drinking water quality using key physicochemical parameters. The application evaluates water safety, calculates a health score, predicts risk levels, determines whether the water is safe to drink, generates AI-powered explanations using Google Gemini, provides recommendations, tracks historical analyses, and creates downloadable PDF reports.

This project demonstrates how multiple AI agents collaborate to solve a real-world public health problem through intelligent reasoning and automation.

---

# ❓ Problem Statement

Millions of people consume water without knowing whether it is safe to drink. Laboratory reports often contain technical values that are difficult for non-experts to interpret.

AquaGuardian AI bridges this gap by transforming raw water quality measurements into easy-to-understand health scores, AI explanations, recommendations, visualizations, and professional reports.

---

# 💡 Solution

The system accepts important water quality parameters, analyzes them using a Multi-Agent architecture, and produces:

- Water Quality Score
- Water Grade
- Risk Assessment
- Safe/Unsafe Decision
- AI-generated Explanation
- Personalized Recommendations
- Water Quality History
- Interactive Visualizations
- Professional PDF Report

---

# ✨ Key Features

- 🤖 Multi-Agent AI Workflow
- 🧠 Google Gemini AI Integration
- 💧 Water Quality Analysis
- 📊 Water Quality Score
- 🏆 Automatic Grade Generation
- ⚠️ Risk Prediction
- ✅ Safe / Unsafe Decision
- 📋 AI Recommendations
- 📈 Water Quality History
- 📉 Score Trend Visualization
- 📄 Downloadable PDF Report
- 🌐 Interactive Streamlit Dashboard

---

# 🧪 Water Parameters Analysed

The system evaluates the following parameters:

- pH
- Total Dissolved Solids (TDS)
- Total Hardness
- Fluoride
- Iron
- Nitrate
- Residual Chlorine
- Conductivity
- Turbidity
- Calcium
- Magnesium
- Potassium
- Sodium

---

# 🤖 Multi-Agent Architecture

The project is built using multiple specialized AI agents working together.

- Data Ingestion Agent
- Analysis Agent
- Score Agent
- Risk Agent
- Decision Agent
- Recommendation Agent
- Explanation Agent (Gemini AI)
- History Agent
- Report Agent
- Visualization Agent
- Parameter Visualization Agent
- Final Summary Agent

Each agent performs a dedicated task, making the system modular, scalable, and easier to maintain.

---

# 🛠 Technology Stack

- Python
- Streamlit
- Google Gemini API
- Pandas
- NumPy
- Matplotlib
- ReportLab
- Python-dotenv

---

# 📂 Project Structure

```text
AquaGuardian-AI
│
├── app.py
├── workflow.py
├── config.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── analysis_agent.py
├── decision_agent.py
├── explanation_agent.py
├── recommendation_agent.py
├── report_agent.py
├── history_agent.py
├── visualization_agent.py
├── score_agent.py
└── ...
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/aquaguardian-ai.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

# 📊 Output

The application generates:

- Water Quality Score
- Grade
- Risk Level
- Safe / Unsafe Decision
- AI Explanation
- Personalized Recommendations
- Water Quality History
- Interactive Charts
- Professional PDF Report

---

# 🔮 Future Scope

- IoT Water Sensor Integration
- Real-Time Water Monitoring
- Mobile Application
- Cloud Deployment
- Smart City Integration
- Government Water Monitoring
- Machine Learning-based Prediction
- Water Quality Alerts

---

# 👩‍💻 Author

**Akanksha Sharma**

Developed as part of the **Kaggle AI Agents: Intensive Vibe Coding Capstone Project** using Google Gemini and a Multi-Agent AI architecture.

---

⭐ If you found this project useful, consider giving it a star!
