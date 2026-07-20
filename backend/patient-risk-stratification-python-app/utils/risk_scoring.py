# utils/risk_scoring.py

def calculate_risk_score(age, glucose, cholesterol, bmi, bp):

    score = 0

    score += age * 0.2
    score += glucose * 0.15
    score += cholesterol * 0.1
    score += bmi * 0.2
    score += bp * 0.15

    return min(round(score / 2, 2), 100)