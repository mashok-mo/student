import random

class Student:
    def __init__(self, health, energy, progress, happy, predisposition):
        self.health = health
        self.energy = energy
        self.progress = progress
        self.happy = happy
        self.predisposition = predisposition

    def study(self):
        self.energy -= random.randint(10,20)
        self.health -= random.randint(10,20)
        self.progress += random.randint(20,25)
        self.happy -= random.randint(10,20)
        return('учился')
    def relax(self):
        self.happy += random.randint(5,10)
        self.health += random.randint(5,10)
        self.energy += random.randint(5,10)
        return('отдыхал')
    def fun(self):
        self.energy += random.randint(5,10)
        self.health -= random.randint(10,20)
        self.happy += random.randint(5,10)
        return('развлекался')
    def do_sport(self):
        self.energy -= random.randint(15,20)
        self.health += random.randint(5,10)
        self.happy += random.randint(5,10)
        return('занимался спортом')

    def check_property(self, property):
        if property <= 0:
            return(False)

    def action_definition(self, seed, n1, n2, n3, study, do_sport, fun, relax):
        if seed <= n1:
            return(study)
        elif seed > n1 and seed <= n2:
            return (do_sport)
        elif seed > n2 and seed <= n3:
            return (fun)
        else:
            return (relax)

    def update(self):
        seed = random.randint(0,100)
        if self.predisposition == 1: #ботаник
            return(self.action_definition(seed, 75, 80, 90, self.study(), self.do_sport(), self.fun(), self.relax()))
        elif self.predisposition == 2: #спортсмен
            return (self.action_definition(seed, 15, 80, 85, self.study(), self.do_sport(), self.fun(), self.relax()))
        elif self.predisposition == 3: #чиллер
            return (self.action_definition(seed, 20, 20, 30, self.study(), self.do_sport(), self.fun(), self.relax()))
        elif self.predisposition == 4: #роцкер
            return (self.action_definition(seed, 15, 25, 90, self.study(), self.do_sport(), self.fun(), self.relax()))

    def check_progress(self):
        if self.progress <50:
            return(False)


class Controller:
    def __init__(self, num_student):
        self.num_student = num_student
        self.student_list = []

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
        print(f'\nСеместр {i+1}')
        print_list(controller.update_semester())
main()

