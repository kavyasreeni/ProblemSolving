# Given the names and grades for each student in a class of N students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

deatils_of_people_list = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    name_score_list = []
    name_score_list.append(name)
    name_score_list.append(score)
    deatils_of_people_list.append(name_score_list)
    # print(deatils_of_people_list)
    # deatils_of_people_list.sort()
    sorted(deatils_of_people_list)
    # sorted_list = deatils_of_people_list[-2]
    print(deatils_of_people_list)
    