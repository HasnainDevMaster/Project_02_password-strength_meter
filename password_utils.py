import re
import random
import string

# Blacklisted weak passwords
blacklist = ['password', '123456', 'qwerty', 'password123', 'admin', 'letmein']

def evaluate_password(password: str):
    score = 0
    feedback = []

    # Blacklist check
    if password.lower() in blacklist:
        return 1, 'Weak', ["Password is too common. Choose a less predictable one."]

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Uppercase check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    # Lowercase check
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    # Digit check
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add a digit (0-9).")

    # Special character check
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("Add a special character (!@#$%^&*).")

    # Strength label
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return score, strength, feedback

def generate_strong_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all selected character types.")

    char_pool = ''
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += "!@#$%^&*"

    if not char_pool:
        raise ValueError("At least one character type must be selected.")

    # Ensure one of each selected type is included
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice("!@#$%^&*"))

    # Fill the rest
    while len(password) < length:
        password.append(random.choice(char_pool))

    random.shuffle(password)
    return ''.join(password)

def evaluate_with_weights(password, weights):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += weights['length']
    else:
        feedback.append("Use at least 8 characters.")

    if any(c.isupper() for c in password):
        score += weights['uppercase']
    else:
        feedback.append("Add an uppercase letter.")

    if any(c.islower() for c in password):
        score += weights['lowercase']
    else:
        feedback.append("Add a lowercase letter.")

    if any(c.isdigit() for c in password):
        score += weights['digits']
    else:
        feedback.append("Add a digit (0-9).")

    if any(c in "!@#$%^&*" for c in password):
        score += weights['symbols']
    else:
        feedback.append("Add a special character (!@#$%^&*).")

    max_score = sum(weights.values())

    if score <= max_score * 0.4:
        strength = "Weak"
    elif score <= max_score * 0.8:
        strength = "Moderate"
    else:
        strength = "Strong"

    return score, max_score, strength, feedback
