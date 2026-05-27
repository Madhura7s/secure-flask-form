# Secure Flask Registration System

A secure user registration and authentication system built using Python Flask with cybersecurity-focused validation and authentication practices.

---

# Project Overview

This project demonstrates how to build a secure web form and authentication system using:

- Python
- Flask
- SQLite
- bcrypt
- HTML
- Linux CLI workflow
- Git & GitHub

The project focuses on secure backend engineering concepts including:

- input validation
- password hashing
- SQL injection prevention
- authentication
- session handling
- secure database interaction

---

# Features

## User Registration

Users can:
- register securely
- validate inputs
- store credentials safely

---

## User Login

Authenticated users can:
- login securely
- access protected dashboard
- logout safely

---

# Security Features

## Input Validation

Validation is implemented for:
- Name
- Email
- Student ID
- Password

---

## Password Hashing

Passwords are hashed using:

- bcrypt

Plain-text passwords are never stored.

---

## SQL Injection Protection

Parameterized queries are used:

```python
cursor.execute(
    "SELECT * FROM users WHERE email = ?",
    (email,)
)
```

This prevents SQL injection attacks.

---

## Session-Based Authentication

Flask sessions are used to:
- maintain authenticated state
- protect restricted routes

---

## Duplicate Email Prevention

SQLite UNIQUE constraint prevents duplicate account registration.

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend language |
| Flask | Web framework |
| SQLite | Database |
| bcrypt | Password hashing |
| HTML | Frontend |
| Git | Version control |
| GitHub | Remote repository |
| Linux CLI | Development workflow |

---

# Project Structure

```bash
secure_form_project/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   └── login.html
│
├── static/
│
└── users.db
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Madhura7s/secure-flask-form.git
```

---

## Move Into Project

```bash
cd secure-flask-form
```

---

## Create Virtual Environment

```bash
python3 -m venv venv
```

---

## Activate Virtual Environment

### Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running The Application

```bash
python3 app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

# Authentication Flow

```text
User Input
↓
Validation
↓
Password Hashing
↓
Database Storage
↓
Login Authentication
↓
Session Creation
↓
Protected Dashboard Access
```

---

# Security Threats Addressed

| Threat | Protection |
|---|---|
| SQL Injection | Parameterized queries |
| Weak Passwords | Regex validation |
| Credential Theft | bcrypt hashing |
| Unauthorized Access | Session validation |
| Duplicate Accounts | UNIQUE constraints |
| Invalid Input | Regex filtering |

---

# Future Improvements

Planned security enhancements:

- CSRF protection
- Rate limiting
- HTTPS
- Secure cookies
- Docker support
- Admin panel
- Logging & monitoring
- Role-based access control
- JWT authentication

---

# Learning Objectives

This project was built to practice:

- secure backend development
- cybersecurity thinking
- Linux-based development workflow
- authentication systems
- secure database interaction
- Git & GitHub workflow

---

# Author

Madhura Suryawanshi

Cybersecurity & Secure Development Enthusiast
