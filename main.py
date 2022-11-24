#Пять типов студентов: ботаник, спортсмен, чиллер, роцкер
#БОТАНИК
#75% - study, 5% - do sport, 10% - fun, 10% - relax
#СПОРТСМЕН
#15% - study, 65% - do sport, 5% - fun, 15% - relax
#ЧИЛЛЕР
#20% - study, 0% - do sport, 10% - fun, 70% - relax
#РОЦКЕР
#15% - study, 10% - do sport, 65% - fun, 10% - relax

import random

class Student:
    def __init__(self, health, energy, progress, happy, intelligence, predisposition):
        self.health = health
        self.energy = energy
        self.progress = progress
        self.happy = happy
        self.intelligence = intelligence
        self.predisposition = predisposition

    def study(self):
        self.energy -= random.randint(5,10)
        self.health -= random.randint(1,5)
        self.progress += random.randint(10,20)
        self.happy -= random.randint(5,15)
        return('учился')
    def relax(self):
        self.happy += random.randint(5,10)
        self.health += random.randint(5,10)
        self.energy += random.randint(5,10)
        return('отдыхал')
    def fun(self):
        self.energy += random.randint(5,10)
        self.health -= random.randint(1,5)
        self.happy += random.randint(5,15)
        return('развлекался')
    def do_sport(self):
        self.energy -= random.randint(5,15)
        self.health += random.randint(5,10)
        self.happy += random.randint(5,10)
        return('занимался спортом')

    #def f(self):


    def update(self):
        seed = random.randint(0,100)
        if self.predisposition == 1: #ботаник
            if seed <=75:
                return (self.study())
            elif seed >75 and seed <=80:
                return (self.do_sport())
            elif seed >80 and seed <=90:
                return (self.fun())
            elif seed >90:
                return (self.relax())
        elif self.predisposition == 2: #спортсмен
            if seed <=15:
                return (self.study())
            elif seed >15 and seed <=80:
                return (self.do_sport())
            elif seed >80 and seed <=85:
                return (self.fun())
            elif seed >85:
                return (self.relax())
        elif self.predisposition == 3: #чиллер
            if seed <= 20:
                return (self.study())
            elif seed > 20 and seed <= 30:
                return (self.fun())
            elif seed > 30:
                return (self.relax())
        elif self.predisposition == 4: #роцкер
            if seed <=15:
                return (self.study())
            elif seed >15 and seed <=25:
                return (self.do_sport())
            elif seed >25 and seed <=90:
                return (self.fun())
            elif seed >90:
                return (self.relax())

    def check_health(self):
        if self.health <=0:
            return(False)

    def check_happy(self):
        if self.happy <=0:
            return(False)

    def check_progress(self):
        if self.progress <50:
            return(False)

    def check_energy(self):
        if self.energy <=0:
            return(False)

class Controller:
    def __init__(self, num_student):
        self.num_student = num_student
        self.student_list = []

    def create_student(self):
        for i in range(self.num_student):
            student = Student(100,100,0,100,0,random.randint(1,4))
            if student.predisposition == 1:
                student.intelligence = 80
            elif student.predisposition == 2:
                student.intelligence = 30
            elif student.predisposition == 3:
                student.intelligence = 50
            elif student.predisposition == 4:
                student.intelligence = 40
            self.student_list.append(student)

    def update_semester(self):
        print_list = []
        delete_student_list = []
        for i in range(len(self.student_list)):
            self.student_list[i].update()
            print_list.append(f'Студент {i+1} весь месяц {self.student_list[i].update()}.\nЗдоровье: {self.student_list[i].health}\nЭнергия: {self.student_list[i].energy}\nСчастье: {self.student_list[i].happy}\nУспеваемость: {self.student_list[i].progress}\nИнтеллект: {self.student_list[i].intelligence}')

            if self.student_list[i].check_health() == False:
                print_list.append(f'Сердце студента {i+1} не выдержало этот семестр')
                delete_student_list.append(self.student_list[i])

            elif self.student_list[i].check_energy() == False:
                print_list.append(f'Студент {i+1} упал без сил перед стенами университета')
                delete_student_list.append(self.student_list[i])

            elif self.student_list[i].check_happy() == False:
                print_list.append(f'Студент {i+1} попал в психбольницу с тяжелой депрессией')
                delete_student_list.append(self.student_list[i])

            elif self.student_list[i].check_progress() == False:
                print_list.append(f'Студент {i+1} не закрыл фх')
                delete_student_list.append(self.student_list[i])
            i+=1

        return(print_list)

def main():
    num_student = int(input('Введите количество студентов: '))
    num_semester = int(input('Введите количество семестров: '))
    controller = Controller(num_student)
    controller.create_student()
    for i in range (num_semester):
        controller.update_semester()
        print(controller.update_semester())
main()

