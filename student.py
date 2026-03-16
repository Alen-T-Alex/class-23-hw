file=open("student.txt","r")
total_marks=0
count=0
highest_marks=0
passed=0
topper=""
lowest_marks=100
lowest=""
for line in file:
    data=line.split()
    name=data[0]
    marks=int(data[1])
    print(name,"-",marks)
    total_marks=total_marks+marks
    count=count+1
    if marks>highest_marks:
        highest_marks=marks
        topper=name
    if marks>=40:
        passed=passed+1
    if marks<lowest_marks:
        lowest_marks=marks
        lowest=name
        

avg=total_marks/count
print("total students=",count,", average marks=",avg,", highest marks=",highest_marks,", topper=",topper,", passed=",passed,", lowest marks=",lowest_marks,", lowest=",lowest)