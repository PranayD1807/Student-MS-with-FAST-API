# Base Url: https://student-ms-with-fast-api.onrender.com/api

## Endpoints:
- POST /students : API to create a student in the system.
- GET /students : API to find a list of students. You can apply filters on this API by passing the query parameters as listed below.
  - country : To apply filter of country. If not given or empty, this filter should be applied.
  - age : Only records which have age greater than equal to the provided age should be present in the result. If not given or empty, this filter should be applied.
- GET /students/{id} : API to fetch data of a single user
- PATCH /students/{id} : API to update the student's properties based on information provided. Not mandatory that all information would be sent in PATCH, only what fields are sent should be updated in the Database.
- DELETE /students/{id} : API to delete user from the system. 

## ENV
MONGODB_URL = Connection String of MONGO_DB Database
