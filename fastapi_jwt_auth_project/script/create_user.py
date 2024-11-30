from app.database import user_collection
from app.utils import hash_password

def create_user(email: str, password: str, full_name: str):
    user = {
        "email": email,
        "password": hash_password(password),
        "full_name": full_name,
        "is_active": True,
        "roles": ["user"],
    }
    user_collection.insert_one(user)
    print(f"User {email} created successfully!")

if __name__ == "__main__":
    create_user("admin@example.com", "adminpassword", "Admin User")
