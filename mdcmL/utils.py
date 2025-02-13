import hashlib

class Utils:
    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()
