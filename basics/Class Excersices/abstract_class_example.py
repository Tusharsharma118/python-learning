from abc import ABC,abstractmethod

class Mammals(ABC):
    @abstractmethod
    def make_sound(self, sound): pass


class Cat(Mammals):
    def __init__(self):
        self.family = 'Cats'

    def make_sound(self, sound):
        print('Cats go:- ' + sound)


Cat().make_sound('Meow!')

