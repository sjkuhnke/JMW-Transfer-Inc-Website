# JMW Transfer Inc. Website

A custom full-stack business website developed for **JMW Transfer Inc.**, built entirely from the ground up using Django. This project demonstrates full ownership across design, development, deployment, and ongoing maintenance.

## 🚚 Overview

This professional web application serves as the online presence for JMW Transfer Inc., a transportation and logistics company. It provides visitors with essential business information and offers prospective drivers a seamless job application experience.

### 🌟 Key Features

- **Dynamic Homepage**
  - Image slideshow highlighting services
  - SEO-optimized service descriptions
  - Mobile-friendly layout

- **Job Application System**
  - Fully digital and mobile-responsive
  - Grouped form sections with real-time validation
  - Conditional fields and calendar widgets
  - E-signature input support
  - Auto-filled PDF generation on submission
  - Company receives completed PDF via email

- **Contact Form**
  - Google reCAPTCHA v2 protection
  - Validation feedback
  - Emails submitted messages to the business

- **About Page**
  - Company values and history
  - Embedded Facebook timeline

- **User Experience Enhancements**
  - JavaScript interactivity (form transitions, animations)
  - Accessibility-conscious design
  - Social media integration

- **Deployment & Maintenance**
  - Deployed on Heroku
  - Environment variable management for all secrets
  - Continuous updates and bug fixes

## ⚙️ Tech Stack

- **Backend**: Python, Django 5
- **Frontend**: HTML5, CSS3, JavaScript (vanilla)
- **Forms**: Django Forms, JavaScript validation
- **PDF Generation**: ReportLab, PyPDF2
- **Email**: Django's Email Backend + Amazon SES (via `boto3`)
- **Deployment**: Gunicorn, Heroku, GitHub
- **Security**: Google reCAPTCHA, `.env` configuration
- **Other**: Pillow (image handling), python-dotenv, custom logging to S3

## 📄 License

This project is proprietary and built for JMW Transfer Inc. Please do not reuse or redistribute code without permission.

## 📬 Contact

Developed by **Shae Kuhnke**  
For inquiries or freelance opportunities, please contact me through my [website](https://www.shaekuhnke.com).
