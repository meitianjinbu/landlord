from threading import Thread


class MyThread(Thread):
    def __init__(self, func, args, name='game'):
        super().__init__()
        self.func = func
        self.args = args
        self.name = name
        self.stoped = False

    def run(self):
        while not self.stoped:
            self.func(*self.args)
