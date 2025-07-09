# CaptureMomentsAWSProject
# 📸 Capture Moments - AWS Powered Photographer Booking System

A cloud-based **Photographer Booking System** developed using **Flask**, **AWS EC2**, and **DynamoDB**. This project was built as part of the **SmartBridge Guided Project Program** in collaboration with **SmartInternz**.

---

## 🧑‍💻 Developed By:

- **Name**: Poojitha Kanipakam  
- **Roll Number**: 22AK1A05A6  
- **Internship Provider**: SmartBridge & Smart Internz 
- **Project Name**: Capture Moments - AWS Powered Photographer Booking System

---

## 📌 Project Objective

At *Capture Moments Photography*, the manual booking process was inefficient and prone to errors, resulting in scheduling conflicts and customer dissatisfaction.

This project solves that by providing:
- An online platform to **book photographers**
- A system to manage appointments using **AWS cloud services**
- A seamless **Flask-based backend** with **DynamoDB** integration

---

## ⚙️ Tech Stack

| Layer        | Technology Used         |
|--------------|--------------------------|
| Frontend     | HTML, CSS, JavaScript    |
| Backend      | Python Flask             |
| Database     | AWS DynamoDB             |
| Hosting      | AWS EC2, IAM Roles       |
| Tools Used   | Git, GitHub, VS Code     |
| Docs         | Word, PDF, Google Drive  |

---

## 🗂️ Folder Structure

<pre>
CaptureMomentsAWSProject/
│
├── Capture Moments(Local Deployment)/    # Local testing version of the app
│   ├── static/                           # CSS, JS, image files
│   ├── templates/                        # HTML templates (Jinja2)
│   └── app.py                            # Flask app entry point
│
├── Capture Moments/                      # Main cloud-deployed version
│   ├── static/                           # Cloud version static files
│   ├── templates/                        # Cloud version HTML templates
│   └── awsint.py                         # AWS-integrated Flask app
│
├── Videos/                               # Demonstration and tutorial videos
│
├── Document(CaptureMoments).docx         # Project documentation (ER, flow, etc.)
│
├── Google drive link                     # Plain text link to project drive
│
└── README.md                             # Project description file
  </pre>
  
---

## 🧩 Features

- ✅ User-friendly web interface
- ✅ Photographer appointment booking
- ✅ AWS DynamoDB integration
- ✅ Hosted on AWS EC2
- ✅ Secure IAM role setup
- ✅ Modular code for easy deployment

---

## 📊 Architecture

- Flask handles HTTP requests and logic
- AWS DynamoDB stores booking records
- IAM provides secure access control
- EC2 instance hosts the live application

---

## 🔄 Project Flow

1. **User** visits the booking website
2. **Flask App** handles frontend & backend
3. **Booking data** stored in **DynamoDB**
4. **Admins/Photographers** check bookings from backend
5. **Confirmation** sent to user via UI
