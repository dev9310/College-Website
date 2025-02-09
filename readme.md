# College Event Management System

This is a Django-based web application for managing college events. It allows users to register for events, upload images, and view upcoming events.

## Features

- User registration and OTP verification
- Event registration
- Image upload and watermarking
- View upcoming events

## Prerequisites

- Python 3.x
- Django 5.1.6
- Virtual environment (optional but recommended)

## Setup

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/college-event-management.git
cd college-event-management
```

### 2. Create and Activate a Virtual Environment

# On Windows

python -m venv myenv
.\myenv\Scripts\activate

# On macOS/Linux

python3 -m venv myenv
source myenv/bin/activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Set Up Environment Variables

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=465
EMAIL_USE_SSL=True
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password
DEFAULT_FROM_EMAIL=your_email@example.com

```sh

```
