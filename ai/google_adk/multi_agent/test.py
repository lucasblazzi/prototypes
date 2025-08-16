import requests

session = requests.post("http://localhost:8000/create_session", json={"user_id": "test_user"})

session = session.json()
print(f"Session created: {session}")
print(f"Session created with ID: {session['id']}")

response = requests.post("http://localhost:8000/invoke", json={
    "user_id": session["userId"],
    "session_id": session["id"],
    "query": {"content": f"What are my daily tasks? My user id is {session['userId']}."}
})

print(response.text)
# print(response.json())
