from abc import ABC, abstractmethod


# 1. Базовый класс Hero
class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} готов к бою!"


# 2. Дочерние классы
class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"


class WarriorHero(MageHero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp, mp)

    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"


# 3. Класс BankAccount (инкапсуляция, магия, классовые и статические методы)
class BankAccount:
    bank_name = "Simba"  # атрибут класса

    def __init__(self, hero, balance, password):
        self.hero = hero
        self._balance = balance      # защищённый атрибут
        self.__password = password   # приватный атрибут

    # Метод для входа
    def login(self, password):
        if password == self.__password:
            return "Вход выполнен успешно!"
        else:
            return "Неверный пароль!"

    # Свойство (только для чтения)
    @property
    def full_info(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    # Классовый метод
    @classmethod
    def get_bank_name(cls):
        return f"Банк: {cls.bank_name}"

    # Статический метод
    @staticmethod
    def bonus_for_level(lvl):
        return f"Бонус за {lvl} уровень: {lvl * 10} SOM"

    # Магические методы
    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if type(self.hero) == type(other.hero):
            total = self._balance + other._balance
            return f"Общий баланс: {total} SOM"
        else:
            return "Ошибка: нельзя объединять счета героев разных классов!"

    def __eq__(self, other):
        return self.hero.name == other.hero.name and self.hero.lvl == other.hero.lvl

