def grade_calculation(score):
    if score >= 90:
        grade = "优秀"
    elif score >= 75:
        grade = "良好"
    else:
        grade = "及格"
    return grade