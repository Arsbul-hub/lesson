class Car:
    mass = 1  # масса
    max_speed = 100  # максимальная скорость
    current_speed = 0  # текущая скорость
    a = 10  # ускорение

    def gas(self):
        self.current_speed += self.a


class Bus(Car):
    mass = 4  # масса
    max_speed = 40  # максимальная скорость
    doors_count = 6  # количество дверей

    def gas(self):
        self.current_speed += 40

    def stop(self):
        self.current_speed = 0


city_bus_1 = Bus()
car_1 = Car()

while True:
    print(city_bus_1.current_speed)
    city_bus_1.gas()
    print(city_bus_1.current_speed)
    if city_bus_1.current_speed == 1000:
        city_bus_1.stop()
