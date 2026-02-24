import re

def check_password(password: str) -> dict:
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    else:
        feedback.append("Password should be at least 12 characters long")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character")

    strength = (
        "Weak" if score <= 2 else
        "Medium" if score <= 4 else
        "Strong"
    )

    return {
        "Strength": strength,
        "Score": f"{score}/6",
        "Feedback": feedback if feedback else ["Good password 👍"]
    }