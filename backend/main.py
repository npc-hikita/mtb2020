import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    dept: str


# デフォルトで1件データを登録しておく
users = [User(**{"name": "John", "dept": "営業課"})]


@app.get('/api/users')
async def get_users():
    return {"users": users}


@app.post('/api/users')
async def register_user(user: User):
    users.append(User(**{"name": user.name, "dept": user.dept}))
    return {"text": "created"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
