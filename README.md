# Define the content for README.md
readme_content = """
# FastAPI JWT Authentication System

## **Features**
- User authentication using JWT (Login, Logout).
- Secure CRUD endpoints for users.
- Password hashing and secure token generation.
- Script to create predefined users.
- Scalable code structure for future extensions.

---

## **Installation Steps**

### **1. Clone the Repository**
Download or clone the repository to your local machine:
```bash
git clone <repository-url>
cd fastapi_jwt_auth
```

### **2. Set Up a Python Virtual Environment**
Create and activate a virtual environment to manage dependencies:
```bash
python -m venv env
source env/bin/activate  # On Windows: .\\env\\Scripts\\activate
```

### **3. Install Dependencies**
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### **4. Configure the Environment Variables**
Create a `.env` file in the project root and configure the following:
```env
DATABASE_URL="your_mongodb_atlas_connection_string"
SECRET_KEY="your_secret_key"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
Replace `your_mongodb_atlas_connection_string` and `your_secret_key` with your actual MongoDB Atlas connection string and a strong secret key.

---

## **Running the Application**

### **1. Start the Server**
Run the FastAPI application locally:
```bash
uvicorn app.main:app --reload
```
The server will start at `http://127.0.0.1:8000`.

### **2. Access the API Documentation**
Visit the interactive API documentation at:
- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

---

## **Creating a User**

### **Using the Script**
To create a user in the database, run the provided script:
```bash
python script/create_user.py
```
This script creates a user with the details specified in the `create_user.py` file.

---

## **Points Covered**

### **Must-Have**
1. Login and logout endpoints.
2. Secure endpoints for user CRUD operations.
3. Readable and modular code.
4. No use of ODM libraries like Beanie or ODMantic.
5. A script to create a predefined user.

### **Good to Have**
1. Predefined models for `User`, `Token`, etc., with Pydantic.
2. Scalability in code structure.
3. Use of an online database (MongoDB Atlas).

### **Added Bonus**
1. Support for RBAC (Role-Based Access Control) can be extended in future versions.
"""

# Path for README.md
readme_path = os.path.join(base_path, "README.md")

# Write the README.md file
with open(readme_path, "w") as readme_file:
    readme_file.write(readme_content)

readme_path
