#Create a student class which takes name and marks of three  subjects as arguments in the constructor
#Then create a method to print the average of the marks

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def avg(self):
        ans = 0
        for i,num in enumerate(self.marks):
            ans+=self.marks[i]
        return ans/len(self.marks)

#main method
mylist = [56,76,4]
s1 = Student("Namita",mylist)
print(s1.avg())            

