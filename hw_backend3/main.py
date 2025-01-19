from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# For demonstration, we'll keep cars in a simple Python list
# In a real app, you'd probably use a database
cars_db = [
    {"name": "BMW 7 Series", "year": 2021},
    {"name": "BMW M5", "year": 2022},
    {"name": "BMW 6 Series", "year": 2020},
    {"name": "BMW M3", "year": 2019},
    {"name": "BMW 7 Series", "year": 2018},
    {"name": "BMW X1", "year": 2018},
    {"name": "Audi A4", "year": 2020},
    {"name": "Audi Q7", "year": 2021},
    {"name": "Toyota Camry", "year": 2019},
    {"name": "Toyota Corolla", "year": 2020},
]

@app.get("/cars/search", response_class=HTMLResponse)
def search_cars(request: Request, car_name: str = ""):
    """
    GET /cars/search
    If car_name is provided, filter cars that contain or start with that string.
    Display the results in 'templates/cars/search.html'
    """
    # Filter logic (case-insensitive)
    car_name_lower = car_name.lower()
    filtered_cars = [car for car in cars_db if car_name_lower in car["name"].lower()]

    return templates.TemplateResponse("cars/search.html", {
        "request": request,
        "cars": filtered_cars,
        "search_query": car_name
    })

@app.get("/cars/new", response_class=HTMLResponse)
def new_car_form(request: Request):
    """
    GET /cars/new
    Return a form for creating a new car
    """
    return templates.TemplateResponse("cars/new.html", {
        "request": request
    })

@app.post("/cars/new")
def add_car(name: str = Form(...), year: int = Form(...)):
    """
    POST /cars/new
    Save the new car to the 'cars_db' and redirect to /cars/search
    (or any endpoint you prefer)
    """
    new_car_entry = {"name": name, "year": year}
    cars_db.append(new_car_entry)

    # After saving the car, redirect to /cars/search (show all by default)
    return RedirectResponse(url="/cars/search", status_code=303)

# OPTIONAL: A route to list all cars if you want to see them without searching
@app.get("/cars", response_class=HTMLResponse)
def list_cars(request: Request):
    return templates.TemplateResponse("cars/search.html", {
        "request": request,
        "cars": cars_db,
        "search_query": ""
    })

if __name__ == "__main__":
    # This 'if' block is only needed if you run 'python main.py' directly.
    # Usually you'd use: uvicorn main:app --reload
    uvicorn.run(app, host="127.0.0.1", port=8000)

