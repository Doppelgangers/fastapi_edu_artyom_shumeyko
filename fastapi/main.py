import uvicorn
from fastapi import FastAPI

app = FastAPI()

fake_users = [
    {"id": 1, "role": "user", "name": "Bob"},
    {"id": 2, "role": "user", "name": "Steve"},
    {"id": 3, "role": "user", "name": "Jon"},
]


@app.get("/user/{user_id}")
def get_user(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]


fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "sell", "price": 123, "amount": 2.12},
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
]


@app.get("/trades")
def get_trades(limit: int = 10, offset: int = 0):
    return fake_trades[offset:][:limit]


@app.post("/user/{user_id}")
def change_name(user_id: int, name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, fake_users))[0]
    current_user["name"] = name
    return {"status": 200, "new_name": name}


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
