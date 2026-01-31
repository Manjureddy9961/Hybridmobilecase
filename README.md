# ⚡ EnergyNest - Hybrid Self-Charging Mobile Case

**EnergyNest** is a cutting-edge mobile accessory project designed to extend battery life indefinitely using a hybrid energy harvesting system. It combines four distinct energy sources—**Solar, Piezoelectric, Acoustic, and Thermoelectric**—into a sleek, smart phone case.

![EnergyNest Banner](static/img/mockup.png)

## 🚀 Key Features

### 🔋 4-Layer Hybrid Energy System
1.  **Solar Layer**: Flexible Perovskite cells harvest indoor and outdoor light.
2.  **Piezoelectric Layer**: Converts vibrations and movement (walking/tapping) into power.
3.  **Acoustic Harvester**: Turns ambient sound (concerts, traffic) into energy.
4.  **Thermoelectric Generator**: Scavenges waste heat from the phone processor.

### 🧠 Smart Features
*   **AI Power Management**: Intelligent PMIC optimizes charging input from all sources.
*   **Live Analytics**: Monitor energy generation, CO₂ reduction, and Green Score in real-time.
*   **IoT Connectivity**: Syncs data to the cloud for cross-device monitoring.
*   **Sustainability Dashboard**: Gamified eco-metrics (e.g., "Level 5 Eco-Warrior").

### 🤖 AI Assistant (EnergyBot)
*   **Smart Local Mode**: Instantly answers questions about Price, Compatibility, and Tech without an API key.
*   **Gemini Power**: Integrated with **Google Gemini API** for advanced conversational capabilities.

## 🛠️ Technology Stack
*   **Backend**: Django (Python)
*   **Frontend**: HTML5, CSS3 (Glassmorphism Design), JavaScript
*   **AI Integration**: Google Generative AI (Gemini Pro)
*   **Visualization**: Chart.js for real-time energy graphs

## 📦 Installation & Setup

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Manjureddy9961/Hybridmobilecase.git
    cd Hybridmobilecase
    ```

2.  **Install Dependencies**
    ```bash
    pip install django google-generativeai
    ```

3.  **Run Migrations**
    ```bash
    python manage.py migrate
    ```

4.  **Run the Server**
    ```bash
    python manage.py runserver
    ```
    Visit `http://127.0.0.1:8000/` to view the application.

## 🔑 AI Chatbot Setup
To enable the advanced AI chatbot features:
1.  Get a generic API Key from Google AI Studio.
2.  Open `core/views.py`.
3.  Replace `YOUR_API_KEY_HERE` with your actual API key.

## 📄 License
This project is for educational and hackathon purposes.
