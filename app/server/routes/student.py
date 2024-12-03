from fastapi import APIRouter, Body, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from server.db.student import (
    add_student,
    get_student,
    get_students,
    delete_student,
    update_student,
)
from server.models.student import StudentSchema, UpdateStudentModel, ErrorResponseModel

router = APIRouter()


@router.post("/")
async def add_student_data(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    if new_student:
        return JSONResponse(content=new_student, status_code=201)
    else:
        return ErrorResponseModel(500, "something went wrong")


@router.get("/")
async def fetch_students(country: str = Query(None), age: int = Query(None)):
    filters = {}
    if country:
        filters["address.country"] = country
    if age is not None:
        filters["age"] = {"$gte": age}

    students = await get_students(filters)
    return {"data": students}


@router.get("/{id}")
async def fetch_student_data(id):
    student = await get_student(id)
    if student:
        return student
    return ErrorResponseModel(404, "Student doesn't exist.")


@router.patch("/{id}")
async def update_student_data(id: str, req: dict = Body(...)):
    valid_fields = {"name", "age", "address"}
    # Filter the request data to include only the valid fields (exclude any extra fields)
    req_data = {k: v for k, v in req.items() if k in valid_fields and v is not None}
    updated_student = await update_student(id, req_data)
    if updated_student:
        return JSONResponse(content={}, status_code=204)
    return ErrorResponseModel(
        404,
        "There was an error updating the student data.",
    )


@router.delete("/{id}")
async def delete_student_data(id: str):
    deleted_student = await delete_student(id)
    if deleted_student:
        return JSONResponse(content={}, status_code=200)

    return ErrorResponseModel(404, "Student with id {0} doesn't exist".format(id))
