class Vihicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white','yellow']
    def __init__(self, owner: str, model: str, color: str,engine_power: int):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color
    def get_model(self):
        return f'Модель: {self.__model}'
    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'
    def get_color(self):
        return f'Цвет: {self.__color}'
    def print_info(self):
        print(f'Модель: {self.__model}\nМощность двигателя: {self.__engine_power}\nЦвет: {self.__color}\nВладелец: {self.owner}')
    def set_color(self, new_color: str):
        if new_color.lower() in Vihicle.__COLOR_VARIANTS:
            self.__color = new_color.lower()
            print(f'Цвет изменён на {new_color}')
        else:
            print(f'Нельзя сменить цвет на {new_color}')
class Sedan(Vihicle):
    __PASSENGERS_LIMIT = 5
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()