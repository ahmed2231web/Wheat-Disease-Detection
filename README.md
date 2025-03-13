# 🌾 AgroConnect - AI-Powered Wheat Disease Detection

<div align="center">

![AgroConnect Banner](frontend/assets/images/diseases/00041.jpg)

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Made with Django](https://img.shields.io/badge/Made%20with-Django-092E20?logo=django)](https://www.djangoproject.com/)
[![Powered by Google Gemini](https://img.shields.io/badge/Powered%20by-Google%20Gemini-4285F4?logo=google)](https://deepmind.google/technologies/gemini/)

</div>

## 🚀 Overview

AgroConnect is a cutting-edge web application that empowers farmers to identify and manage wheat diseases using advanced AI technology. By combining deep learning for image analysis with Google's Gemini AI for intelligent chat interactions, AgroConnect provides a comprehensive solution for wheat disease detection and management.

## ✨ Features

### 🔍 Disease Detection
- **Instant Analysis**: Upload a photo and get immediate disease detection results
- **High Accuracy**: Powered by state-of-the-art deep learning models
- **Visual Feedback**: Clear visualization of detected diseases

### 🤖 AI Assistant
- **Smart Chat**: Interactive conversations about detected diseases
- **Expert Advice**: Get detailed treatment recommendations
- **Powered by Gemini**: Leveraging Google's advanced AI for accurate responses

### 💫 User Experience
- **Intuitive Interface**: Clean, modern design for easy navigation
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Real-time Results**: Instant feedback and analysis

## 🛠️ Technology Stack

### Frontend
- HTML5, CSS3, JavaScript
- Bootstrap 5 for responsive design
- Axios for API communication
- Font Awesome icons

### Backend
- Django REST Framework
- TensorFlow/PyTorch for disease detection
- Google Gemini API for chatbot
- SQLite for lightweight data storage

## 📂 Project Structure
```
AgroConnect/
├── backend/                 # Django backend
│   ├── disease_detection/   # Disease detection app
│   ├── agroconnect/        # Main Django project
│   └── manage.py           # Django management script
│
├── frontend/               # Frontend files
│   ├── assets/            # Static assets
│   │   ├── css/          # CSS files
│   │   ├── js/           # JavaScript files
│   │   └── images/       # Image assets
│   ├── pages/            # HTML pages
│   └── index.html        # Main landing page
│
└── README.md              # Project documentation
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Git
- Web browser (Chrome/Firefox/Safari)

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ahmed2231web/AgroConnect.git
   cd AgroConnect
   ```

2. **Set Up Python Environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   source venv/bin/activate  # Linux/Mac
   venv\\Scripts\\activate   # Windows
   
   # Install dependencies
   pip install -r backend/requirements.txt
   ```

3. **Configure Environment Variables**
   ```bash
   # Copy example environment file
   cp backend/.env.example backend/.env
   
   # Edit .env file and add your Gemini API key
   # GEMINI_API_KEY=your_api_key_here
   ```

4. **Start the Application**
   ```bash
   # Start Django backend server
   python backend/manage.py runserver
   
   # Open frontend/index.html in your web browser
   ```

## 🌟 Key Features in Action

### 1. Upload & Detect 📸
- Take or upload a photo of your wheat plant
- Get instant disease detection results
- View confidence scores and affected areas

### 2. AI Chat Assistant 🤖
- Ask questions about detected diseases
- Get treatment recommendations
- Learn prevention strategies

### 3. Disease Information 📚
- Access detailed disease descriptions
- View common symptoms
- Get management strategies

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- Google Gemini API for powering the intelligent chat system
- The agricultural research community for disease datasets
- Open source community for various tools and libraries

## 📬 Contact

For questions or feedback, please reach out to:
- 📧 Email: codefiles47@gmail.com

---

<div align="center">

### Made with ❤️ by the AgroConnect Team

[⭐ Star us on GitHub]([https://github.com/ahmed2231web/AgroConnect](https://github.com/ahmed2231web/Wheat-Disease-Detection.git)) | [📧 Contact Us](mailto:codefiles47@gmail.com)

</div>
