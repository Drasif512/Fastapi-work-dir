from fastapi import FastAPI, Depends, HTTPException, status
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel



app = FastAPI()

models.Students.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

   # return SessionLocal(autocommit=False, autoflush=False, bind=engine)
    # return Session(autocommit=False, autoflush=False)
    # return SessionLocal()
    # return Session()
    # return db_session()
    # return Session()
    # return get_db()
    # return db_session()
    # return Session()  

@app.post('/class',status_code=status.HTTP_201_CREATED)
def create(request: schemas.Students, db: Session= Depends(get_db)):
    new_student = models.Students(firstName=request.firstName,lastName=request.lastName)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student
 
@app.get('/class',response_model=List[schemas.ShowStudents])
def all(db: Session = Depends(get_db)):
    students = db.query(models.Students).all()
    return students

@app.get("/class/{id}", response_model=schemas.ShowStudents)
def show(id: int, db: Session = Depends(get_db)):
    student = db.query(models.Students).filter(models.Students.id == id).first()
    if not student:
        raise HTTPException(status_code=404, detail=f"Student with id {id} not available")
    return student


@app.delete('/class/{id}',status_code=status.HTTP_200_OK)
def delete(id: int, db: Session = Depends(get_db)):
    db.query(models.Students).filter(models.Students.id == id).delete(synchronize_session=False)
    db.commit()
    return {"detail": f"Student with id {id} deleted"}


    # if not Student:
    #     raise HTTPException(status_code=404, detail=f"Student with id {id} not available")

@app.put('/class/{id}', status_code=status.HTTP_200_OK)
def update(id, request: schemas.Students, db: Session = Depends(get_db)):
    update_data = {
        "firstName": request.firstName,
        "lastName": request.lastName,
        # Add other fields to update as needed
    }
    student = db.query(models.Students).filter(models.Students.id == id)
    if not student.first():
        raise HTTPException(status_code=404, detail=f"Student with id {id} not found")
    student.update(update_data)
    db.commit()
    # db.refresh(update_student)
    return "Updated Succesfully"




@app.post('/chat/{id}')
def chat(request):
    return {"message": f"Hello! how can I help you?"
             f"Responce: {request}" }