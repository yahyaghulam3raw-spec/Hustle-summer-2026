# Yahya N, Lab 5, Intro to python
#ticket 1
ages =[17, 11, 25, 13, 9]

for age in ages:
    if age > 13:
        print(age, "Access granted")
    else:
            print(age, "Too young") #access granted:17, 25. no access:9, 11, 13
# age holds the power to let you in or not 

#ticket 2

keep_checking = "yes"

while keep_checking == "yes":
    age = int(input("Enter an age "))
    if age > 13:
        print(age, "Access granted")
    else:
        print(age, "too young")
        keep_checking = input("Checking another age? (yes/no): ") #if user types no then maybe it wont even begin
#It gives people a chance if they accidently put the wrong age
#ticket 3

while True:
    response = input("Enter an age or type 'stop': ")
    if response == "stop": break
    age = int(response)
    if age > 13:
        print(age, "Access granted")
    else: 
        print(age, "too young") #the loop would never end
        #not much opf a diffrence to me besides wording, so i guess they serve trhe same purpose 

#ticket 4

def can_access(age): return age <13

ages = [25, 17, 134, 11, 9]

for age in ages:
    if can_access(age):
        print(age, "Access granted")
    else:
        print(age, "Too young")

#ticket #5

def signup_report(ages_list): 
    approved = 0
    print("SteamPass Signup Report")
    for i, age in enumerate (ages_list, start=1):
        if can_access(age):
            print(f"Signup #{i} Age {age:2} access. granted")
            approved += 1
        else:
            print(f"Signup #{i} Age {age:2} Too young")
    print(f"\nApproved: {approved} out of {len(ages_list)}")
signups = [22, 19, 15, 13, 10, 8]
signup_report(signups)
#2/6, and  I used Functions, parameter, for loopp, enumerate, len, f string 