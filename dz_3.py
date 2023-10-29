from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
from direct.task import Task


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Загружаем модель блока
        self.block = self.loader.loadModel("models/box")
        self.block.reparentTo(self.render)

        # Создаем сетку блоков
        self.grid = [[None] * 10 for _ in range(10)]
        for i in range(10):
            for j in range(10):
                block_instance = self.block.copyTo(self.render)
                block_instance.setPos(i, j, 0)
                self.grid[i][j] = block_instance

        # Загружаем модель игрока
        self.player = self.loader.loadModel("models/box")
        self.player.reparentTo(self.render)

        # Устанавливаем начальные координаты игрока
        self.player_pos = [0, 0]
        self.player.setPos(self.player_pos[0], self.player_pos[1], 0)

        # Устанавливаем обработчики клавиш
        self.accept("arrow_up", self.move_player, [0, 1])
        self.accept("arrow_down", self.move_player, [0, -1])
        self.accept("arrow_left", self.move_player, [-1, 0])
        self.accept("arrow_right", self.move_player, [1, 0])

        # Запускаем цикл обновления игры
        self.taskMgr.add(self.update, "update")

    def move_player(self, dx, dy):
        new_x = self.player_pos[0] + dx
        new_y = self.player_pos[1] + dy
        if 0 <= new_x < 10 and 0 <= new_y < 10:
            self.player_pos = [new_x, new_y]
            self.player.setPos(self.player_pos[0], self.player_pos[1], 0)

    def update(self, task):
        # Обновление игры
        return Task.cont


game = Game()
game.run()
