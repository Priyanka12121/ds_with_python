class student:
    def __init__(self):
        self.name=raw_input("enter the name")
        self.roll=raw_input("enter the rollno")
    def show(self):
        print("name: ",self.name)
        print("roll: ",self.roll)

s1=student()
s1.show()
        
    
