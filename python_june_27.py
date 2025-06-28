from tkinter.font import names

from fontTools.misc.textTools import caselessSort

employee={
    "Id":1,
    "name":'sabeer'
}
print(employee)
#set Default
employee.setdefault("email","sab@gmail.com")
print(employee)
employee.setdefault("Role","developer")
print(employee)
employee.setdefault("age","25")
print(employee)
#get method
print(employee['name'])
print(employee['Role'])
print(employee['age'])
#key method
print(employee.keys())
#values method
print(employee.values())
#get
print(employee.get("name"))
#items
print(employee.items())
#delete
#pop
employee.pop("name")
print(employee)
#popitem
employee.popitem()
print(employee)
#clear
employee.clear()
print(employee)

student={
    "name":'praneeth',
    "class":'10th',
    "Id":'22'
}
print(student)
#set Default
student.setdefault("school","Vikram high school")
print(student)
#get method
print(student['name'])
#key method
print(student.keys())
#value method
print(student.values())
#get
print(student.get("name"))
#items
print(student.items())
#delete
#pop
print(student.pop("Id"))
print(student)
#popitem
print((student.popitem()))
print(student)
#clear
student.clear()
print(student)

#control stmt
#conditional stmt
#if
list={"mango","apple","banana","grapee"}
name="mango"
if(name in list):
    print("name is exists")
else:
    print("name not exists")
#ex-2
list={"lion","tiger","elephant","dog","fish"}
name="monkey"
if(name in list):
    print("name is exists")
else:
    print("name not exists")

    #elif
a=20
b=40
if a>b:
    print("a is bigger than b")
elif a<b:
    print("a is smaller than b")
else:
    print("a is equals to b")

#ex-2
    day = 3

    if day == 1:
        print("Monday")
    elif day == 2:
        print("Tuesday")
    elif day == 3:
        print("Wednesday")
    else:
        print("Another day")

#nested If
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("You are eligible to vote.")
    else:
        print("You must be a citizen to vote.")
else:
    print("You must be at least 18 to vote.")

#ternary operator

list={"nikhil","meena","praneeth"}
name="nikhil"
print("name exists")if(name in list)else print("name not exists")
#EX-2
list={"Sabeer","pranay","krishna"}
name="sabeer"
print("name exists")if(name in list)else print("name not exists")
#switch
# if elif elif
employe={
    "id":1,
    "name":"pavan",
    "employetype":"perminent"
}
if employe.get("employetype")=="perminent":
    print("perminent employe")
elif employe.get("employetype")=="contractor":
    print("contractor employe")

    #ex-2
Studentt={
    "ID":22,
    "name":"kiran",
    "Remarks":"irregular"

}
if Studentt.get("Remarks")=="regular":
    print("regular Studentt")
else :Studentt.get("Remarks")=="irregular"
print("irregular Studentt")

