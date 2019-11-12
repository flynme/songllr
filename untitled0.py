class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        return "{} is {} years old".format(self.name, self.age)
mikey = Dog("Mikey", 6)
dada = Dog("dada",8)
xixu = Dog("xixu",5)
def get_biggest_number(a,b,c):
    if a<b>c:
        s=dada
    if a<c>b:
        s=xixu
    if b<a>c:
        s=mikey
    return s
print(get_biggest_number(mikey.age,dada.age,xixu.age).description())