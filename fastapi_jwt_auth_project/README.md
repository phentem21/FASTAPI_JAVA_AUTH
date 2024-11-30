# FastAPI JWT Authentication System

## Features
- User authentication with JWT (Login, Logout).
- Secure user CRUD endpoints.
- Password hashing and verification.

## Requirements
- Python 3.9+
- MongoDB Atlas or Local MongoDB instance.

## Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Setup environment variables in `.env` file.

## Run Application
```bash
uvicorn app.main:app --reload
```

## Points Covered
- Login and Logout endpoints.
- Secure CRUD endpoints.
- Scalable code structure.
