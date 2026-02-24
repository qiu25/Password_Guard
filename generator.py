import random
import string

def generate_password(length: int = 16) -> str:
    if length < 8:
        raise ValueError("Password length must be at least 8")

    characters = (
        string.ascii_letters +
        string.digits +
        "!@#$%^&*()_+-="
    )

    return "".join(random.choice(characters) for _ in range(length))