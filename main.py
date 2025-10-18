import string
import secrets
from random import SystemRandom

def strong_password(password: str) -> tuple:
    arr = list(password)

    long_enough = len(arr) > 6
    has_lower   = any(c.islower() for c in arr)
    has_upper   = any(c.isupper() for c in arr)
    has_digit   = any(c.isdigit() for c in arr)
    has_symbol  = any(not c.isalnum() for c in arr)

    if all([long_enough, has_lower, has_upper, has_digit, has_symbol]):
        return True, "Password is strong ✅"

    msg = "Weak password for the following reasons:\n"
    if not long_enough:
        msg += "- Length must be greater than 6\n"
    if not has_lower:
        msg += "- Must contain at least one lowercase letter\n"
    if not has_upper:
        msg += "- Must contain at least one uppercase letter\n"
    if not has_digit:
        msg += "- Must contain at least one number\n"
    if not has_symbol:
        msg += "- Must contain at least one symbol\n"

    return False, msg


def generate_strong_password(min_len: int = 12) -> str:
    """Generate a strong password that contains lowercase, uppercase, digits, and symbols."""
    if min_len < 4:
        min_len = 4

    categories = {
        'lower': string.ascii_lowercase,
        'upper': string.ascii_uppercase,
        'digits': string.digits,
        'symbols': "!@#$%^&*()-_=+[]{};:,.<>/?"
    }

    pw_chars = [
        secrets.choice(categories['lower']),
        secrets.choice(categories['upper']),
        secrets.choice(categories['digits']),
        secrets.choice(categories['symbols']),
    ]

    all_chars = categories['lower'] + categories['upper'] + categories['digits'] + categories['symbols']
    while len(pw_chars) < min_len:
        pw_chars.append(secrets.choice(all_chars))

    SystemRandom().shuffle(pw_chars)

    return ''.join(pw_chars)


if __name__ == "__main__":
    password = input("Enter your password: ")
    is_strong, message = strong_password(password)
    print(message)

    if not is_strong:
        suggestion = generate_strong_password(12)
        print("\nSuggested strong password:\n", suggestion)
