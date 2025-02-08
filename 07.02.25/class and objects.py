class students:
    def __init__(self,name,tamil,eng,math,sci,sco): #constructor
        self.Name=name
        self.Tamil=tamil
        self.English=eng
        self.Maths=math
        self.Science=sci
        self.Social=sco

    def total(self):
        total=500  # static for all students
        add=self.Tamil+self.English+self.Maths+self.Science+self.Social
        print(f'{self.Name} total mark is {add}/{total}')


student1=students("sankar",90,99,89,88,92)

student1.total()


  
