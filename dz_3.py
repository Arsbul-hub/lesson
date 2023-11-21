# ооп - объектно ориентированное программирвание


class App:
    run_time = "20:00"  # атрибут
    a = 5  # атрибут
    b = 10  # атрибут
    c = None

    def run_program(self):  # метод (функция)
        print("Программа запущена!")
        print(self.run_time)
        self.calculate_c()
        print(self.c)

    def calculate_c(self):
        self.c = (self.a ** 2 + self.b ** 2) ** 0.5


if __name__ == "__main__":  # если этот файл является главным
    app = App()

    # app.calculate_c()
    app.run_program()
