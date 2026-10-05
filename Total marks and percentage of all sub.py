#WAP to calculate total marks and percentage of all subjects.
total_marks = 0
subjects=int(input("Enter number of subjects:"))
for i in range(subjects):
    subject_marks=int(input(f"Enter marks for subject{i+1}:"))
    total_marks+=subject_marks
percentage=(total_marks/(subjects*100))*100
print(f"Total marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")