from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from starlette.middleware.sessions import SessionMiddleware
from pydantic import BaseModel
import os
import uuid

# Initialize FastAPI app
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="my-temporary-dev-key-123pyt")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Database setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'database.db')}"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define User model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=True)

    def __repr__(self):
        return f'<User {self.name}>'

# Create database tables
Base.metadata.create_all(bind=engine)

# Pydantic model for form validation
class UserForm(BaseModel):
    name: str
    age: int | None

# Helper function to flash messages
def flash(request: Request, message: str, category: str = "success"):
    if "_messages" not in request.session:
        request.session["_messages"] = []
    request.session["_messages"].append({"message": message, "category": category})

# Helper function to get flash messages
def get_flashed_messages(request: Request):
    messages = request.session.get("_messages", [])
    request.session["_messages"] = []
    return messages

# Route for home page (list all users)
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    db = SessionLocal()
    try:
        users = db.query(User).all()
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "users": users, "messages": get_flashed_messages(request)}
        )
    finally:
        db.close()

# Route to add a new user
@app.get("/add", response_class=HTMLResponse)
async def add_user_form(request: Request):
    return templates.TemplateResponse(
        "add_user.html",
        {"request": request, "messages": get_flashed_messages(request)}
    )

@app.post("/add", response_class=HTMLResponse)
async def add_user(request: Request, name: str = Form(...), age: str = Form(None)):
    db = SessionLocal()
    try:
        if not name:
            flash(request, "Name is required!", "error")
            return templates.TemplateResponse(
                "add_user.html",
                {"request": request, "messages": get_flashed_messages(request)}
            )
        age_value = int(age) if age else None
        new_user = User(name=name, age=age_value)
        db.add(new_user)
        db.commit()
        flash(request, "User added successfully!", "success")
        return RedirectResponse(url="/", status_code=303)
    except Exception as e:
        db.rollback()
        flash(request, f"Error adding user: {str(e)}", "error")
        return templates.TemplateResponse(
            "add_user.html",
            {"request": request, "messages": get_flashed_messages(request)}
        )
    finally:
        db.close()

# Route to edit an existing user
@app.get("/edit/{id}", response_class=HTMLResponse)
async def edit_user_form(request: Request, id: int):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return templates.TemplateResponse(
            "edit_user.html",
            {"request": request, "user": user, "messages": get_flashed_messages(request)}
        )
    finally:
        db.close()

@app.post("/edit/{id}", response_class=HTMLResponse)
async def edit_user(request: Request, id: int, name: str = Form(...), age: str = Form(None)):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        user.name = name
        user.age = int(age) if age else None
        db.commit()
        flash(request, "User updated successfully!", "success")
        return RedirectResponse(url="/", status_code=303)
    except Exception as e:
        db.rollback()
        flash(request, f"Error updating user: {str(e)}", "error")
        return templates.TemplateResponse(
            "edit_user.html",
            {"request": request, "user": user, "messages": get_flashed_messages(request)}
        )
    finally:
        db.close()

# Route to delete a user
@app.get("/delete/{id}", response_class=HTMLResponse)
async def delete_user(request: Request, id: int):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        db.delete(user)
        db.commit()
        flash(request, "User deleted successfully!", "success")
        return RedirectResponse(url="/", status_code=303)
    except Exception as e:
        db.rollback()
        flash(request, f"Error deleting user: {str(e)}", "error")
        return RedirectResponse(url="/", status_code=303)
    finally:
        db.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
