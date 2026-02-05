from fastapi import FastAPI
import uvicorn


app = FastAPI()

# Mock database
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI example!"}


@app.get("/users")
def get_users():
    return users


@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        return user
    return {"error": "User not found"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import FastAPI

app = FastAPI()

# Very small post
post = {
    "id": 1,
    "title": "First deployment",
    "content": "This site is running on Render using FastAPI."
}

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/post")
def get_post():
    return post

