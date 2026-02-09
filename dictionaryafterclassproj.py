student_data = {
    'id1': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english', 'math', 'science']},
    'id2': {'name': ['David'], 'class': ['V'], 'subject_integration': ['english', 'math', 'science']},
    'id3': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english', 'math', 'science']},
    'id4': {'name': ['Surya'], 'class': ['V'], 'subject_integration': ['english', 'math' , 'science']}

}

count = 0

for value in student_data.values():
    if value['name'][0] == 'Sara':
        count += 1

print(count)