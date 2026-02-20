def average(scores):
	return sum(scores.values())/len(scores)
	
def selected_students(students):
    result = {}

    for name, scores in students.items():
        avg = average(scores)

        if avg >= 17 and scores["math"] >= 18:
            result[name] = round(avg, 2)

    return result  
	 
students={
         "Ali":{"math":18,"physics":15,"cs":19},
         "Reza":{"math":14,"physics":16,"cs":17},
         "Mina":{"math":19,"physics":18,"cs":20}
}

print(selected_students(students))
