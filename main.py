import random

class Student:
    def __init__(self, health, energy, progress, happy, predisposition):
        self.__health = health
        self.__energy = energy
        self.__progress = progress
        self.__happy = happy
        self.__predisposition = predisposition

    @property
    def health(self):
        return self.__health
    @property
    def energy(self):
        return self.__energy
    @property
    def progress(self):
        return self.__progress
    @property
    def happy(self):
        return self.__happy
    @property
    def predisposition(self):
        return self.__predisposition

    @health.setter
    def health(self, health):
        self.__health = health
    @energy.setter
    def energy(self, energy):
        self.__energy = energy
    @progress.setter
    def progress(self, progress):
        self.__progress = progress
    @happy.setter
    def happy(self, happy):
        self.__happy = happy

    def change_property(self, health, energy, progress, happy):
        self.health += health
        self.energy += energy
        self.progress += progress
        self.happy += happy

    def study(self):
        self.change_property(-random.randint(10, 20), -random.randint(10, 20), random.randint(25, 30),
                             -random.randint(15, 20))
        return('учился')
    def relax(self):
        self.change_property(random.randint(5, 10), random.randint(5, 10), 0,
                             random.randint(5, 10))
        return('отдыхал')
    def fun(self):
        self.change_property(-random.randint(5, 10), random.randint(5, 10), 0,
                             random.randint(5, 10))
        return('развлекался')
    def do_sport(self):
        self.change_property(random.randint(5, 10), -random.randint(5, 10), 0,
                             random.randint(5, 10))
        return('занимался спортом')

    def action_definition(self, seed, n1, n2, n3):
        if seed <= n1:
            action = self.study
        elif seed > n1 and seed <= n2:
            action = self.do_sport
        elif seed > n2 and seed <= n3:
            action = self.fun
        else:
            action = self.relax
        return (action())

    def update(self):
        seed = random.randint(0,100)
        if self.__predisposition == 1: #ботаник
            return(self.action_definition(seed, 75, 80, 90))
        elif self.__predisposition == 2: #спортсмен
            return (self.action_definition(seed, 15, 80, 85))
        elif self.__predisposition == 3: #чиллер
            return (self.action_definition(seed, 20, 20, 30))
        elif self.__predisposition == 4: #роцкер
            return (self.action_definition(seed, 15, 25, 90))

    def check_progress(self):
        if self.__progress <50:
            return(False)
    def check_property(self, property):
        if property <= 0:
            return(False)


class Controller:
    def __init__(self, num_student):
        self.__num_student = num_student
        self.__student_list = []

    @property
    def num_student(self):
        return self.__num_student

    @property
    def student_list(self):
        return self.__student_list

    def create_student(self):
        print_list = []
        for i in range(self.num_student):
            student = Student(80,80,0,80,random.randint(1,4))
            if student.predisposition == 1:
                print_list.append(f'Cтудент {i+1} - ботаник')
            elif student.predisposition == 2:
                print_list.append(f'Cтудент {i+1} - спортсмен')
            elif student.predisposition == 3:
                print_list.append(f'Cтудент {i+1} - чиллер')
            elif student.predisposition == 4:
                print_list.append(f'Cтудент {i+1} - роцкер')
            self.student_list.append(student)
        return (print_list)

    def update_semester(self):
        for j in range(len(self.student_list)):
            self.student_list[j].health = 80
            self.student_list[j].energy = 80
            self.student_list[j].happy = 80
            self.student_list[j].progress = 0

        print_list = []
        delete_student_list = []

        def update_month(self):
            print_list.append(f'\nМесяц {i+1}')
            for j in range(len(self.student_list)):
                print_list.append(f'\nСтудент {j+1} весь месяц {self.student_list[j].update()}.\nЗдоровье: {self.student_list[j].health}\nЭнергия: {self.student_list[j].energy}\nСчастье: {self.student_list[j].happy}\nУспеваемость: {self.student_list[j].progress}')

        for i in range(0, 5):
            update_month(self)

        print_list.append(f'\nРезультаты семестра: ')

        for j in range(len(self.student_list)):
            if self.student_list[j].check_property(self.student_list[j].health) == False:
                print_list.append(f'Сердце студента {j + 1} не выдержало этот семестр')
                delete_student_list.append(self.student_list[j])

            elif self.student_list[j].check_property(self.student_list[j].energy) == False:
                print_list.append(f'Студент {j + 1} упал без сил перед стенами университета')
                delete_student_list.append(self.student_list[j])

            elif self.student_list[j].check_property(self.student_list[j].happy) == False:
                print_list.append(f'Студент {j + 1} попал в психбольницу с тяжелой депрессией')
                delete_student_list.append(self.student_list[j])

            elif self.student_list[j].check_progress() == False:
                print_list.append(f'Студент {j + 1} не закрыл фх')
                delete_student_list.append(self.student_list[j])

            else:
                print_list.append(f'Поздравим студента {j + 1}! Он закрыл семестр')

        if len(delete_student_list)!=0:
            for i in range(len(delete_student_list)):
                self.student_list.remove(delete_student_list[i])

        return(print_list)

def print_list(list):
    for i in range(len(list)):
        print(list[i])

def main():
    num_student = int(input('Введите количество студентов: '))
    num_semester = int(input('Введите количество семестров: '))
    controller = Controller(num_student)
    print_list(controller.create_student())
    for i in range (num_semester):
        if len(controller.student_list)!=0:
            print(f'\nСеместр {i+1}')
            print_list(controller.update_semester())
        else:
            print('\nНикто из студентов не прошел голодные игры. Игра окончена')
            break
main()

