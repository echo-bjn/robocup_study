class Person:
    def __init__(self,name,age,sex):
        self.age=age
        self.name=name
        self.sex=sex
    def personInfo(self):
        print(f"{self.name},{self.sex},{self.age}")

class Student(Person):
    def __init__(self,name,sex,age,college,clas):
        super(Student,self).__init__(name,sex,age)
        self.college=college
        self.clas=clas
    def personInfo(self):
        Person.personInfo(self)
        print(f"就读于{self.college}{self.clas}")

if __name__ == '__main__':
    stu=Student("小白","男","30岁","家里蹲大学","不存在学院")
    stu.personInfo()