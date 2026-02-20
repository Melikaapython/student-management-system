def passed_students(students):
    result = {}

    for name, scores in students.items():
        avg = sum(scores.values()) / len(scores)

        if avg >= 16:
            result[name] = avg

    return result
students = {
    "Ali": {"math": 18, "physics": 15, "cs": 19},
    "Sara": {"math": 14, "physics": 16, "cs": 17},
    "Mina": {"math": 19, "physics": 18, "cs": 20}
}

print(passed_students(students))
