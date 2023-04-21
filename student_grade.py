
student_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62
}
student_grades = {}
def student_grade():
    for student in student_scores.keys():
        # print(student)
        score = student_scores[student]
        if score > 90:
            student_grades[student] = "Outstanding"
        elif score >80:
            student_grades[student] = "Exceeds Expectations"
        elif score >70:
            student_grades[student] = "Acceptable"
        else:
            student_grades[student] = "Fail"

    print(student_grades)

print(student_scores)
response = input("Enter you want to do ( Add , Remove ,Delete ) :")
if response == 'Add':
    name = input("Enter Student Name :")
    score = int(input("Enter student score : "))
    student_scores.update({name:score})
elif response == 'Remove':
    name = input("Enter name you want to remove :")
    student_scores.pop(name)
elif response == 'Delete':
    student_scores.clear()

student_grade()

grade_value = student_grades.values()

outstanding_count = 0
exceeds_expectation_count = 0
acceptable_count = 0
fail_count = 0

for x in grade_value:
    if x == 'Outstanding' :
        outstanding_count += 1
    elif x == 'Exceeds Expectations' :
        exceeds_expectation_count += 1
    elif x == 'Acceptable' :
        acceptable_count += 1
    elif x == 'Fail':
        fail_count += 1

print(f'No: of Outstanding student : {outstanding_count}')
print(f'No: of Exceeds Expectations students : {exceeds_expectation_count}')
print(f'No: of Acceptable students : {acceptable_count}')
print(f'No: of fail students : {fail_count}')
        
student_score_backup = student_scores.copy()
student_grade_backup = student_grades.copy()
print(student_score_backup)
print(student_grade_backup)
