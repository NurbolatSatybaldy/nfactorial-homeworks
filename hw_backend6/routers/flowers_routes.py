from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse, PlainTextResponse
from db import get_connection
from models import Flower
from auth import verify_token
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()

def create_flower(name, quantity, price):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO flowers (name, quantity, price) VALUES (%s, %s, %s)", (name, quantity, price))
    conn.commit()
    cur.close()
    conn.close()

def get_all_flowers():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, quantity, price FROM flowers ORDER BY id DESC")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [Flower(r["id"], r["name"], r["quantity"], r["price"]) for r in rows]

def get_flower_by_id(fid):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, quantity, price FROM flowers WHERE id=%s", (fid,))
    r = cur.fetchone()
    cur.close()
    conn.close()
    if r:
        return Flower(r["id"], r["name"], r["quantity"], r["price"])

def add_purchase(uid, fid):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO purchases (user_id, flower_id) VALUES (%s, %s)", (uid, fid))
    conn.commit()
    cur.close()
    conn.close()

def get_purchases(uid):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT flowers.name, flowers.price FROM purchases JOIN flowers ON purchases.flower_id=flowers.id WHERE purchases.user_id=%s", (uid,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

@router.get("/flowers", response_class=HTMLResponse)
def get_flowers_page(request: Request):
    flowers = get_all_flowers()
    return templates.TemplateResponse("flowers/list.html", {"request": request, "flowers": flowers})

@router.post("/flowers")
def post_flower(name: str = Form(...), quantity: int = Form(...), price: float = Form(...)):
    create_flower(name, quantity, price)
    return RedirectResponse(url="/flowers", status_code=303)

@router.post("/purchased")
def post_purchased(request: Request):
    token = request.cookies.get("jwt_token")
    if not token:
        return PlainTextResponse("Not authenticated", status_code=401)
    payload = verify_token(token)
    if not payload:
        return PlainTextResponse("Invalid token", status_code=401)
    user_id = payload.get("sub")
    val = request.cookies.get("cart")
    if not val:
        return PlainTextResponse("Cart is empty")
    parts = val.split(":")
    if len(parts) != 2:
        return PlainTextResponse("Cart data error")
    fid = parts[1]
    f = get_flower_by_id(fid)
    if not f:
        return PlainTextResponse("Flower not found", status_code=404)
    add_purchase(user_id, fid)
    r = RedirectResponse(url="/purchased", status_code=303)
    r.delete_cookie("cart")
    return r

@router.get("/purchased", response_class=HTMLResponse)
def get_purchased(request: Request):
    token = request.cookies.get("jwt_token")
    if not token:
        return PlainTextResponse("Not authenticated", status_code=401)
    payload = verify_token(token)
    if not payload:
        return PlainTextResponse("Invalid token", status_code=401)
    user_id = payload.get("sub")
    rows = get_purchases(user_id)
    return templates.TemplateResponse("flowers/purchased.html", {"request": request, "purchases": rows})
