name = (input("Enter the Student Name:")) 

sub_1 = int(input("Enter the marks of subject 1:"))
sub_2 = int(input("Enter the marks of subject 2:"))
sub_3 = int(input("Enter the marks of subject 3:"))
sub_4 = int(input("Enter the marks of subject 4:"))
sub_5 = int(input("Enter the marks of subject 5:"))

total = sub_1 + sub_2 + sub_3 + sub_4 + sub_5
avg = total/5
if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 60:
    grade = 'D'
else:
    grade = 'E'

# SD Calculation
sd_total = ((sub_1 - avg) ** 2 +
            (sub_2 - avg) ** 2 +
            (sub_3 - avg) ** 2 +
            (sub_4 - avg) ** 2 +
            (sub_5 - avg) ** 2)

sd = (sd_total / 5) ** 0.5

# CV Calculation
cv = (sd / avg) * 100

print("Name:",name)
print("Total marks:",total)
print("Average marks:",avg)
print("Grade:",grade)

print("Standard Deviation:", round(sd, 2))
print("Coefficient of Variation:", round(cv, 2), "%")  

