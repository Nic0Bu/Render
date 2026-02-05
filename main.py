from fastapi import FastAPI

app = FastAPI()

# Mock database
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

# Very small post
post = {
    "id": 1,
    "title": "First deployment",
    "content": "This site is running on Render using FastAPI."
}

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return user
    return {"error": "User not found"}

@app.get("/post")
def get_post():
    return post
