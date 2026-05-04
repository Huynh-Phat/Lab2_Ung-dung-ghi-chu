import requests

class APIClient:
    def __init__(self, backend_url="http://127.0.0.1:8000", firebase_key="AIzaSyA1K-jiNBdUGIw1ZK-EWERNZfZ8YAFgJk0"):
        self.backend_url = backend_url
        self.firebase_key = firebase_key

    # --- Firebase Auth Logic ---
    def auth_request(self, email, password, mode="signInWithPassword"):
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:{mode}?key={self.firebase_key}"
        payload = {"email": email, "password": password, "returnSecureToken": True}
        return requests.post(url, json=payload).json()

    # --- Backend Logic ---
    def save_note(self, user_id, content):
        return requests.post(f"{self.backend_url}/notes/", json={"user_id": user_id, "content": content})

    def fetch_notes(self, user_id):
        return requests.get(f"{self.backend_url}/notes/{user_id}")