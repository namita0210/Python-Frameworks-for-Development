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

#Q2: Create a bank account class with debit, credit and balance functionalities
class Bank :
    def __init__(self, balance , acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def credit(self, amt):
        self.balance += amt
        print("The account has been credited with Rs. ",amt,"and the balance is ",self.balance)

    def debit(self, amt):
        self.balance -= amt
        print("The account has been debited with Rs. ",amt,"and the balance is ",self.balance)

    def getBalance(self):
        return self.balance    

#Q3: Define a circle class to create a circle with radius r using the constructor
class Circle:

    def __init__(self , radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius        
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
        
#main method
# mylist = [56,76,4]
# s1 = Student("Namita",mylist)

# customer1 = Bank(1200,123)
# customer1.credit(10)  

c1 = Circle(5)
print(c1.area())


