from bson.objectid import ObjectId
from fastapi import HTTPException
from server.db.connection import client
from typing import Dict, Any

# we will need to import client from connection.py
database = client.students
student_collection = database.get_collection("students")


def student_helper(student) -> dict:
    return {
        "name": student.get("name", ""),
        "age": student.get("age", 0),
        "address": {
            "city": student.get("address", {}).get("city", ""),
            "country": student.get("address", {}).get("country", ""),
        },
    }


async def add_student(student_data: Dict[str, Any]) -> Dict[str, Any]:
    student = await student_collection.insert_one(student_data)
    new_student = await student_collection.find_one({"_id": student.inserted_id})
    return {"id": str(new_student["_id"])}


async def get_students(filters: dict = None):
    filters = filters or {}
    students = []
    async for student in student_collection.find(filters):
        students.append(
            {
                "name": student.get("name", ""),
                "age": student.get("age", 0),
            }
        )
    return students


async def get_student(id: str) -> dict:
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        return student_helper(student)


async def update_student(id: str, data: dict):
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        updated_student = await student_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_student:
            return True
        return False
    return False


async def delete_student(id: str):
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        await student_collection.delete_one({"_id": ObjectId(id)})
        return True
    return False
