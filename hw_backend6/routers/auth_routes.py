from fastapi import APIRouter, Form, Request, Response, status
from fastapi.responses import PlainTextResponse, RedirectResponse, HTMLResponse
from db import get_connection
from models import User
from auth import create_access_token, verify_token
from passlib.hash import bcrypt
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()

def create_user(email, full_name, password_hash):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (email, full_name, password_hash) VALUES (%s, %s, %s)", (email, full_name, password_hash))
    conn.commit()
    cur.close()
    conn.close()

def get_user_by_email(email):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, email, full_name, password_hash, photo_url FROM users WHERE email=%s", (email,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row:
        return User(row["id"], row["email"], row["full_name"], row["password_hash"], row["photo_url"])

def get_user_by_id(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, email, full_name, password_hash, photo_url FROM users WHERE id=%s", (user_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row:
        return User(row["id"], row["email"], row["full_name"], row["password_hash"], row["photo_url"])

@router.get("/signup", response_class=HTMLResponse)
def get_signup_form(request: Request):
    return templates.TemplateResponse("auth/signup.html", {"request": request})

@router.post("/signup")
def post_signup(email: str = Form(...), full_name: str = Form(...), password: str = Form(...)):
    user = get_user_by_email(email)
    if user:
        return PlainTextResponse("Email already exists", status_code=400)
    hashed = bcrypt.hash(password)
    create_user(email, full_name, hashed)
    return RedirectResponse(url="/login", status_code=303)

@router.get("/login", response_class=HTMLResponse)
def get_login_form(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})

@router.post("/login")
def post_login(response: Response, email: str = Form(...), password: str = Form(...)):
    user = get_user_by_email(email)
    if not user:
        return PlainTextResponse("Invalid credentials", status_code=401)
    if not user.verify_password(password):
        return PlainTextResponse("Invalid credentials", status_code=401)
    token = create_access_token({"sub": str(user.id)})
    r = RedirectResponse(url="/profile", status_code=303)
    r.set_cookie(key="jwt_token", value=token, httponly=True)
    return r

@router.get("/profile", response_class=HTMLResponse)
def get_profile(request: Request):
    token = request.cookies.get("jwt_token")
    if not token:
        return PlainTextResponse("Not authenticated", status_code=401)
    payload = verify_token(token)
    if not payload:
        return PlainTextResponse("Invalid token", status_code=401)
    user_id = payload.get("sub")
    user = get_user_by_id(user_id)
    if not user:
        return PlainTextResponse("User not found", status_code=404)
    return templates.TemplateResponse("auth/profile.html", {"request": request, "user": user})
