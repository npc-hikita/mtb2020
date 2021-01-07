from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# データを入れる器


class User(BaseModel):
    name: str
    dept: str


# デフォルトで1件データを登録しておく
users = [User(**{"name": "John", "dept": "営業課"})]

# データを取得するエンドポイント


@app.get('/api/users')
async def get_users():
    return {"users": users}

# データを登録するエンドポイント


@app.post('/api/users')
async def register_user(user: User):
    users.append(User(**{"name": user.name, "dept": user.dept}))
    return {"text": "created"}
