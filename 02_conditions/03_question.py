score = int(input("Enter the score :"))

if score >=101:
    print("please verify the grade")
    exit()   

if score>=90 :
    grade = "A"
elif score>=80:
    grade = "B"
elif score>=70:
    grade = "C"
elif score>=60:
    grade = "D"
else:
    grade = "F"

print("student grade:",grade)