from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse, PlainTextResponse, HTMLResponse
from .flowers_routes import get_flower_by_id
import uuid
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.post("/cart/items")
def post_cart_items(response: RedirectResponse, flower_id: int = Form(...), cart_id: str = Form(None)):
    c = cart_id or str(uuid.uuid4())
    cookie_val = f"{c}:{flower_id}"
    r = RedirectResponse(url="/flowers", status_code=303)
    r.set_cookie(key="cart", value=cookie_val, httponly=True)
    return r

@router.get("/cart/items", response_class=HTMLResponse)
def get_cart_items(request: Request):
    val = request.cookies.get("cart")
    if not val:
        return PlainTextResponse("Cart is empty")
    parts = val.split(":")
    if len(parts) != 2:
        return PlainTextResponse("Cart data error")
    flower = get_flower_by_id(parts[1])
    if not flower:
        return PlainTextResponse("Flower not found in cart")
    total = flower.price
    return templates.TemplateResponse("cart/list.html", {"request": request, "flower": flower, "total": total})
