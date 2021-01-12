import uvicorn
from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from sqlalchemy.orm import Session
import os

from models import Base, User as DbUser
from schemas import User as SchemaUser
from database import SessionLocal, engine

# models.pyに書いてあるモデルクラスの定義に従いDBを構築
Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        # pylint: disable=E1101
        db.close()


@app.exception_handler(404)
async def not_found(request, ex):
    return FileResponse(path="static/index.html", media_type="text/html")


@app.get('/api/users')
async def get_users(db: Session = Depends(get_db)):
    users = db.query(DbUser).all()
    return {"users": users}


@app.post('/api/users')
async def register_user(user: SchemaUser, db: Session = Depends(get_db)):
    db_user = DbUser(name=user.name, dept=user.dept)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"text": "created"}


app.mount("/static", StaticFiles(directory="static", html=True), name="static")


if __name__ == "__main__":
    port = int(os.environ["PORT"])
    uvicorn.run(app, host="0.0.0.0", port=port)
