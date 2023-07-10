import math
def get_grade(s1, s2, s3):
    score = sum([s1,s2,s3]) / 3
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score <80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    elif 0 <= score < 60:
        return "F"

print(get_grade(95, 90, 93))
print(get_grade(100, 85, 96))
print(get_grade(92, 93, 94))
print(get_grade(100, 100, 100))

print(get_grade(70, 70, 100))

print(get_grade(70, 70, 70))

    