from fastapi import FastAPI, Query, Response, status, Request
from fastapi.responses import JSONResponse, HTMLResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

cars = [
    {"id": 1, "name": "Toyota Camry", "year": "2019"},
    {"id": 2, "name": "Toyota Corolla", "year": "2020"},
    {"id": 3, "name": "Honda Civic", "year": "2021"},
    {"id": 4, "name": "Honda Accord", "year": "2018"},
    {"id": 5, "name": "Ford Fiesta", "year": "2021"},
    {"id": 6, "name": "Ford Focus", "year": "2017"},
    {"id": 7, "name": "BMW X5", "year": "2022"},
    {"id": 8, "name": "BMW 3 Series", "year": "2019"},
    {"id": 9, "name": "Audi A4", "year": "2020"},
    {"id": 10, "name": "Audi Q7", "year": "2018"},
    {"id": 11, "name": "Toyota RAV4", "year": "2023"},
    {"id": 12, "name": "Ford Mustang", "year": "2022"}
]

users = [
    {"id": 1, "email": "test1@test.com", "first_name": "Aibek", "last_name": "Bekturov", "username": "deadly_knight95"},
    {"id": 2, "email": "test2@test.com", "first_name": "Dana", "last_name": "Zharkyn", "username": "dana_zhar"},
    {"id": 3, "email": "test3@test.com", "first_name": "Bota", "last_name": "Eset", "username": "be_123"},
    {"id": 4, "email": "test4@test.com", "first_name": "Azamat", "last_name": "Khan", "username": "azamat_k"},
    {"id": 5, "email": "test5@test.com", "first_name": "Ivan", "last_name": "Petrov", "username": "ivan_p"},
    {"id": 6, "email": "test6@test.com", "first_name": "Elena", "last_name": "Kim", "username": "elena_kim"},
    {"id": 7, "email": "test7@test.com", "first_name": "Mary", "last_name": "Jones", "username": "mary_j"},
    {"id": 8, "email": "test8@test.com", "first_name": "John", "last_name": "Smith", "username": "john_smith"},
    {"id": 9, "email": "test9@test.com", "first_name": "Linda", "last_name": "Taylor", "username": "lindat"},
    {"id": 10, "email": "test10@test.com", "first_name": "Max", "last_name": "Well", "username": "max_well"},
    {"id": 11, "email": "test11@test.com", "first_name": "Anara", "last_name": "Zheks", "username": "anara_zheks"},
    {"id": 12, "email": "test12@test.com", "first_name": "Mike", "last_name": "Wilson", "username": "mike_wil"}
]

@app.get("/cars")
def get_cars(page: int = 1, limit: int = 10):
    start_index = (page - 1) * limit
    end_index = start_index + limit
    data = cars[start_index:end_index]
    return JSONResponse(content=data)

@app.get("/cars/{id}")
def get_car(id: int):
    for c in cars:
        if c["id"] == id:
            return JSONResponse(content=c)
    return Response(content="Not found", status_code=status.HTTP_404_NOT_FOUND)

@app.get("/users", response_class=HTMLResponse)
def get_users(request: Request, page: int = 1, limit: int = 10):
    start_index = (page - 1) * limit
    end_index = start_index + limit
    data = users[start_index:end_index]
    total = len(users)
    return templates.TemplateResponse("users/list.html", {"request": request, "users": data, "page": page, "limit": limit, "total": total})

@app.get("/users/{id}", response_class=HTMLResponse)
def get_user(request: Request, id: int):
    for u in users:
        if u["id"] == id:
            return templates.TemplateResponse("users/detail.html", {"request": request, "user": u})
    return Response(content="Not found", status_code=status.HTTP_404_NOT_FOUND)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

