from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from typing import List

app = FastAPI()

# Данные
cars = [
    {"id": 1, "make": "Toyota", "model": "Corolla", "year": 2020},
    {"id": 2, "make": "Honda", "model": "Civic", "year": 2021},
    {"id": 3, "make": "Ford", "model": "Focus", "year": 2019},
    # Добавьте больше машин, если требуется
]

users = [
    {"id": 1, "name": "John Doe", "email": "john.doe@example.com", "age": 30},
    {"id": 2, "name": "Jane Smith", "email": "jane.smith@example.com", "age": 25},
    # Добавьте больше пользователей, если требуется
]

# Роуты
@app.get("/cars")
def get_cars(page: int = 1, limit: int = 10):
    start = (page - 1) * limit
    end = start + limit
    return {"cars": cars[start:end]}

@app.get("/cars/{id}")
def get_car_by_id(id: int):
    car = next((car for car in cars if car["id"] == id), None)
    if not car:
        raise HTTPException(status_code=404, detail="Not found")
    return car

@app.get("/users", response_class=HTMLResponse)
def get_users():
    html = "<h1>Users</h1><ul>"
    for user in users:
        html += f'<li><a href="/users/{user["id"]}">{user["name"]}</a></li>'
    html += "</ul>"
    return html

@app.get("/users/{id}", response_class=HTMLResponse)
def get_user_by_id(id: int):
    user = next((user for user in users if user["id"] == id), None)
    if not user:
        raise HTTPException(status_code=404, detail="Not found")
    html = f"""
    <h1>{user['name']}</h1>
    <p>Email: {user['email']}</p>
    <p>Age: {user['age']}</p>
    """
    return html

@app.get("/users/pagination", response_class=HTMLResponse)
def get_users_pagination(page: int = 1, limit: int = 10):
    start = (page - 1) * limit
    end = start + limit
    paginated_users = users[start:end]

    html = "<h1>Users</h1><ul>"
    for user in paginated_users:
        html += f'<li><a href="/users/{user["id"]}">{user["name"]}</a></li>'
    html += "</ul>"

    # Пагинация
    html += f"""
    <div>
        <a href="/users/pagination?page={page-1 if page > 1 else 1}&limit={limit}">Previous</a>
        <a href="/users/pagination?page={page+1}&limit={limit}">Next</a>
    </div>
    """
    return html
