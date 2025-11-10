class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        education = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(f"Привет! Меня зовут {self.name}. Я {self.occupation}, родился(лась) {self.birth_date}, и у меня {education}.")

person1 = Person("Айдана", "12 марта 2004", "дизайнер", True)
person2 = Person("Айдина", "25 июля 2005", "программист", False)
person3 = Person("Адинай", "9 января 2003", "фотограф", True)

print(person1.name, person1.birth_date, person1.occupation, person1.higher_education)
print(person2.name, person2.birth_date, person2.occupation, person2.higher_education)
print(person3.name, person3.birth_date, person3.occupation, person3.higher_education)
print()
person1.introduce()
person2.introduce()
person3.introduce()

