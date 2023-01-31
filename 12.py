marks=[55,64,75,80,34]
length=len(marks)
print("length is",length)
marks_sum=sum(marks)
print("the total marks you got is",marks_sum)
# function to find average marks
def find_average_marks(marks):
    sum_of_marks=sum(marks)
    total_subjects=len(marks)
    average_marks=sum_of_marks/total_subjects
    return aberage_marks
