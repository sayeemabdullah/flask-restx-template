from project import mongo
import uuid
from datetime import datetime

mongodb = mongo.db
admin = mongodb['admins']


def get_admin_by_email(email):
    return admin.find_one({"email": email})


def get_admin_count_by_email(email):
    return admin.count_documents({"email": email})


def add_admin(name, email, mobile, password):
    return admin.insert_one({
        "user_id": str(uuid.uuid4()),
        "name": name,
        "email": email,
        "mobile": mobile,
        "password": password,
        "user_type": "admin",
        "created_at": datetime.now(),
    })
