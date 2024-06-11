import re

class PasswordAnalyzer:
    def __init__(self, password):
        self.password = password
        self.length = len(password)
        self.has_upper = any(c.isupper() for c in password)
        self.has_lower = any(c.islower() for c in password)
        self.has_digit = any(c.isdigit() for c in password)
        self.has_special = any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for c in password)

    def analyze(self):
        score = 0
        if self.length >= 8:
            score += 1
        if self.has_upper:
            score += 1
        if self.has_lower:
            score += 1
        if self.has_digit:
            score += 1
        if self.has_special:
            score += 1

        strength = 'Very Weak'
        if score == 5:
            strength = 'Very Strong'
        elif score == 4:
            strength = 'Strong'
        elif score == 3:
            strength = 'Moderate'
        elif score == 2:
            strength = 'Weak'

        return {
            'strength': strength,
            'length': self.length,
            'has_upper': self.has_upper,
            'has_lower': self.has_lower,
            'has_digit': self.has_digit,
            'has_special': self.has_special,
            'recommendations': self.recommendations()
        }

    def recommendations(self):
        recommendations = []
        if self.length < 8:
            recommendations.append("Password should be at least 8 characters long.")
        if not self.has_upper:
            recommendations.append("Password should include at least one uppercase letter.")
        if not self.has_lower:
            recommendations.append("Password should include at least one lowercase letter.")
        if not self.has_digit:
            recommendations.append("Password should include at least one digit.")
        if not self.has_special:
            recommendations.append("Password should include at least one special character.")

        if not recommendations:
            recommendations.append("Your password is strong. Keep using good practices!")

        return recommendations


password = input("Enter a password to analyze: ")
analyzer = PasswordAnalyzer(password)
analysis = analyzer.analyze()

print(f"Password Strength: {analysis['strength']}")
print(f"Password Length: {analysis['length']}")
print(f"Contains Uppercase: {analysis['has_upper']}")
print(f"Contains Lowercase: {analysis['has_lower']}")
print(f"Contains Digit: {analysis['has_digit']}")
print(f"Contains Special Character: {analysis['has_special']}")
print("\nRecommendations:")
for recommendation in analysis['recommendations']:
    print(f"- {recommendation}")
