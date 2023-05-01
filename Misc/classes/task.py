from loader import PICTURES


class CurrentTask:
    def __init__(self, task_list: tuple[str]):
        self.type = task_list[1]
        self.level = task_list[2]
        self.value = task_list[3]
        self.poster = PICTURES.get(f'task_{self.level}')

    def task(self, index: int, total: int):
        return f'{index + 1}/{total}\nТема: {self.type}\nУровень: {self.level}\n\n{self.value}'
