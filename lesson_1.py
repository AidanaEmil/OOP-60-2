class Hero:
    def __init__(self, nick_name, lvl , hp):
        self.nick_name = nick_name
        self.lvl = lvl
        self.hp = hp

kirito = Hero('Kirito', 100, 1000)

asuna = Hero('Asuna', 100, 1000)

print(kirito.lvl)
print(kirito.hp)