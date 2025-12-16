"""
Password Strength Analyzer
CYB333 Security Automation Final Project

This script evaluates the strength of a password based on length,
character variety, and common weak patterns. It provides feedback
and suggestions to help users create stronger passwords.
"""
import re

def analyze_password(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short. Use at least 12 characters.")

    # Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Common weak patterns
    common_patterns = ["123", "password", "qwerty", "abc"]
    if any(pattern in password.lower() for pattern in common_patterns):
        feedback.append("Avoid common patterns like '123' or 'password'.")

    return score, feedback


def strength_label(score):
    if score >= 6:
        return "Strong"
    elif score >= 4:
        return "Moderate"
    else:
        return "Weak"


def main():
    print("Password Strength Analyzer")
    print("-" * 30)

    password = input("Enter a password to evaluate: ")
    score, feedback = analyze_password(password)
    strength = strength_label(score)

    print(f"\nPassword Strength: {strength}")

    if feedback:
        print("Suggestions:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("Your password looks strong.")


if __name__ == "__main__":
    main()
