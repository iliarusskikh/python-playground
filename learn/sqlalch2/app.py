## Create a book
#curl -X POST -H "Content-Type: application/json" -d '{"title":"Python 101","author":"John Doe"}' http://localhost:8000/books
#
## Get all books
#curl http://localhost:8000/books
#
## Get a specific book
#curl http://localhost:8000/books/1
#
## Update a book
#curl -X PUT -H "Content-Type: application/json" -d '{"title":"Python 202","author":"Jane Doe"}' http://localhost:8000/books/1
#
## Delete a book
#curl -X DELETE http://localhost:8000/books/1

#pip install fastapi sqlalchemy uvicorn pydantic
#Uvicorn takes your FastAPI application and makes it accessible over HTTP,

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, field_validator
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from typing import List

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///books.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL,
#     pool_size=20,  # Max number of connections in the pool
#     max_overflow=10,  # Allow extra connections beyond pool_size
#     pool_timeout=30  # Seconds to wait for a connection
# )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# SQLAlchemy Book model
class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    published_date = Column(DateTime, nullable=False, default=datetime.utcnow)

# Create database tables
Base.metadata.create_all(bind=engine)

# Pydantic models for request/response validation
class BookCreate(BaseModel):
    title: str
    author: str

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    published_date: str

    @field_validator('published_date', pre=True)
    def convert_datetime_to_string(cls, value):
        if isinstance(value, datetime):
            return value.isoformat()
        return value

    class Config:
        orm_mode = True

# FastAPI app
app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new book
@app.post("/books", response_model=BookResponse, status_code=201)
async def create_book(book: BookCreate, db: SessionLocal = Depends(get_db)):
    db_book = Book(title=book.title, author=book.author)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Get all books
@app.get("/books", response_model=List[BookResponse])
async def get_books(db: SessionLocal = Depends(get_db)):
    books = db.query(Book).all()
    return books

# Get a single book
@app.get("/books/{id}", response_model=BookResponse)
async def get_book(id: int, db: SessionLocal = Depends(get_db)):
    book = db.query(Book).filter(Book.id == id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# Update a book
@app.put("/books/{id}", response_model=BookResponse)
async def update_book(id: int, book: BookCreate, db: SessionLocal = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db_book.title = book.title
    db_book.author = book.author
    db.commit()
    db.refresh(db_book)
    return db_book

# Delete a book
@app.delete("/books/{id}", status_code=204)
async def delete_book(id: int, db: SessionLocal = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return {"message": "Book deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)