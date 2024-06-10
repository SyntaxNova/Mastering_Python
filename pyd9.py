class student:
    def __init__(self , name, m1 , m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def average(self):
        sum = self.m1 + self.m2 + self.m3
        avg = sum/3
        return avg

s1 = student("Atharva" , 100 ,93 , 95)
print(f"avg marks of {s1.name} is = ", s1.average())