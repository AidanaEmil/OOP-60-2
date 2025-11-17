from abc import ABC, abstractmethod

class Hero:
    def __init__(self,name,lvl,hp):
        self.name=name
        self.lvl=lvl
        self.hp=hp
    def action(self):
        return f"{self.name} готов к бою!"

class MageHero(Hero):
    def __init__(self,name,lvl,hp,mp):
        super().__init__(name,lvl,hp)
        self.mp=mp
    def action(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"

class WarriorHero(MageHero):
    def __init__(self,name,lvl,hp,mp=0):
        super().__init__(name,lvl,hp,mp)
    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"

class BankAccount:
    bank_name="Simba"
    def __init__(self,hero,balance,password):
        self.hero=hero
        self._balance=balance
        self.__password=password

    def login(self,password):
        if password==self.__password:
            return True
        else:
            return False

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name

    @staticmethod
    def bonus_for_level(lvl):
        return lvl*10

    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self,other):
        if type(self.hero)==type(other.hero):
            new_balance=self._balance+other._balance
            return BankAccount(self.hero,new_balance,'123')
        else:
            print("Ошибка: нельзя сложить разные классы героев!")

    def __eq__(self,other):
        return self.hero.name==other.hero.name and self.hero.lvl==other.hero.lvl

class SmsService(ABC):
    @abstractmethod
    def send_otp(self,phone):
        pass

class KGSms(SmsService):
    def send_otp(self,phone):
        return f"<text>Код: 1234</text><phone>{phone}</phone>"

class RUSms(SmsService):
    def send_otp(self,phone):
        return {"text":"Код: 1234","phone":phone}

# --- Проверка работы ---
merlin=MageHero("Merlin",40,800,150)
conan=WarriorHero("Conan",50,1000)
print(merlin.action())
print(conan.action())
print(conan.action())

acc1=BankAccount(merlin,5000,'111')
acc2=BankAccount(conan,3000,'222')
print(acc1)
print(acc2)
print("Банк:",BankAccount.get_bank_name())
print("Бонус за 50 уровень:",BankAccount.bonus_for_level(50),"SOM")

kg=KGSms()
print(kg.send_otp("+996777123456"))


