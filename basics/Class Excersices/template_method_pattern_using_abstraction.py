from abc import ABC, abstractmethod

class Recipy(ABC):

    def execute(self):
        self.prepare()
        self.recipy()
        self.cleanup()

    @abstractmethod
    def prepare(self): pass

    @abstractmethod
    def recipy(self): pass

    @abstractmethod
    def cleanup(self): pass


class Cake_Recipy(Recipy):

    def prepare(self):
        print(' Gather your Ingredients! \n 1)Eggs, \n 2)Flour \n 3) Milk \n 4) Sugar');

    def recipy(self):
        print('\n 1) Mix Flour and Eggs \n 2) Keep beating the batter till it attains a fine consistency \n 2) Pour in the sugar and mix it for 2 minutes')
        print('\n 3) Pour the batter in the baking tray and put it in the oven')
        print('\n 4) Wait for 10 minutes till the cake bakes!')

    def cleanup(self):
        print('\n Clean the dishes properly!')

Cake_Recipy().execute()


