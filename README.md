SMART HEALTH AND WELLNESS MONITORING SYSTEM 
📌 Project Overview

The Smart Health and Wellness Monitoring System is designed to track real-time health metrics. It provides personalized insights, visual analytics, alerts, and goal tracking to help users manage their health more effectively. An admin panel is included for efficient system and user management.

🚀 Features

✅ User Authentication – Secure login & registration
✅ Real-Time Data Collection – Syncs data from wearable devices (heart rate, steps, calories, etc.)
✅ Data Analysis – Provides personalized insights based on user health metrics
✅ Goal Tracking – Helps users set and monitor fitness/health goals
✅ Dashboard Visualization – Interactive charts & reports for better understanding
✅ Admin Panel – Manage users, monitor data, and generate reports

🏗️ System Architecture

Frontend: React.js (Dashboard UI & User interaction)

Backend: Django (REST API & Business logic)

Database: MySQL (User and health data storage)


⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/janani03m/smart-health-monitoring.git
cd smart-health-monitoring

2️⃣ Backend Setup (Django + MySQL)
cd backend
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

3️⃣ Frontend Setup (React)
cd frontend
npm install
npm start

📊 Sample Dashboard

Real-time health tracking (Heart rate, calories, activity)

Graphical insights (Line charts, bar charts, progress rings)

Admin overview of users

🔔 Future Enhancements

Integration with AI/ML models for predictive health insights

Mobile app support (React Native / Flutter)

Support for additional wearable APIs (Fitbit, Apple Watch, Google Fit)

Personalized diet & workout recommendations


📜 License

This project is licensed under the MIT License – feel free to use, modify, and distribute.
