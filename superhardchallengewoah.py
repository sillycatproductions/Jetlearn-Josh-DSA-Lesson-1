class Student:
    def __init__(self, age, iq, name, classroom):
        self.age = age
        self.iq = iq
        self.name = name
        self.classroom = classroom

    def get_iq(self):
        return self.iq
    def set_iq(self, new_iq):
        self.iq = new_iq

    def show_student(self):
        print('Hi my name is {}! I am {} years old and my IQ is {}! I am in the class {}!'.format(self.name, self.age, self.iq, self.classroom))

student1 = Student('12', '94', 'Bob', '8-4')
student1.set_iq('-92')
student1.show_student()

student2 = Student('25872635823648673465865866234687548374874568743564276342856', '-4784775', 'other bob', '1-5')
student2.show_student()