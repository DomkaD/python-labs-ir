class Insect:
#конструктор
    def __init__(self, name = None, speed = None, mass = None, about = '', living = 0):
        self.__name = name
        self.__speed = speed
        self.__mass = mass
        self.about = about
        self.living = living
#деструктор
    def __del__(self):
        print("Insect end")
#методи доступу
    def get_name(self):
        return self.__name

    def get_speed(self):
        return self.__speed

    def get_mass(self):
        return self.__mass

    def set_name(self, new_name):
        self.__name = new_name

    def set_speed(self, new_speed):
        self.__speed = new_speed

    def set_mass(self, new_mass):
        self.__mass = new_mass

#перевизначення str i repr
    def __str__(self):
        return f"Insect: name: {self.__name}, speed: {self.__speed} m/s, mass: {self.__mass} g"

    def __repr__(self):
        return (f"Insect(name='{self.__name}', speed={self.__speed}, mass={self.__mass}, "
                f"about='{self.about}', living={self.living})")

#використовується щоб визначити чи виконується цей скрипт як основний
# if __name__ == "__main__":
def main():
    insect1 = Insect("fly", 20, 10, "flying object", 1)
    insect2 = Insect("bee", 10, 15)
    insect3 = Insect()
    insect1.set_name('beetle')
    print(insect1)
    print(insect2)
    print(insect3)
    print(repr(insect1))
    print(repr(insect2))
    print(repr(insect3))
main()
