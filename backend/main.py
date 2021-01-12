import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from starlette.responses import FileResponse
import os

app = FastAPI()


class User(BaseModel):
    name: str
    dept: str


# デフォルトで1件データを登録しておく
users = [User(**{"name": "John", "dept": "営業課"})]


@app.exception_handler(404)
async def not_found(request, ex):
    return FileResponse(path="static/index.html", media_type="text/html")


@app.get('/api/users')
async def get_users():
    return {"users": users}


@app.post('/api/users')
async def register_user(user: User):
    users.append(User(**{"name": user.name, "dept": user.dept}))
    return {"text": "created"}


os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static", html=True), name="static")


if __name__ == "__main__":
    print("PORT is " + os.environ["PORT"])
    uvicorn.run(app, host="0.0.0.0", port=os.environ["PORT"])
