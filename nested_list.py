# Given the names and grades for each student in a class of N students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Python code to sort the lists using the second element 
# of sublists inplace way to sort, use of third variable
def Sort(sub_li):
   
    l = len(sub_li)
     
    for i in range(0, l):
        for j in range(0, l-i-1):
             
            if (sub_li[j][1] > sub_li[j + 1][1]):
                tempo = sub_li[j]
                sub_li[j] = sub_li[j + 1]
                sub_li[j + 1] = tempo
     
    return sub_li
 
# Input list
sub_li = [['rishav', 10], ['akash', 5], ['ram', 20], ['gaurav', 15]]

# Printing the list 
print(Sort(sub_li))

