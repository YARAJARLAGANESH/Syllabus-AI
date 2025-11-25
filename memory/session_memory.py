import time
class SessionMemory:
    def __init__(self, session_id: str, user_id: str = None):
        self.session_id = session_id
        self.user_id = user_id
        self.created_at = time.time()
        self.expires_at = self.created_at + 7*24*3600  # 7 days default
        self.data = {}

    def set(self, key, value):
        self.data[key] = value

    def get(self, key, default=None):
        return self.data.get(key, default)
