class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        education = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(f"Привет! Меня зовут {self.name}. Я {self.occupation}, родился(лась) {self.birth_date}, и у меня {education}.")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        print(f"Привет! Меня зовут {self.name}. Я учусь в группе {self.group_name}. Работаю {self.occupation}.")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(f"Привет! Меня зовут {self.name}. Я {self.occupation}, и моё хобби — {self.hobby}.")


classmate1 = Classmate("Айдана", "12 марта 2004", "дизайнер", True, "OOP-60-2")
classmate2 = Classmate("Айдина", "25 июля 2005", "программист", False, "OOP-60-2")

friend1 = Friend("Адинай", "9 января 2003", "фотограф", True, "рисование")
friend2 = Friend("Алия", "17 июня 2004", "веб-дизайнер", True, "путешествия")

people = [classmate1, classmate2, friend1, friend2]

for person in people:
    person.introduce()
