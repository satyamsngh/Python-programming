from abc import ABC , abstractmethod

class animal(ABC):
    @abstractmethod
    def leopard(self):
        pass

class lion(animal):
    def leopard(self):
        print("carnivorus")

class dog(animal):
    def leopard(self):
        print("eat carnivorus")

a=lion()
a.leopard()

b=dog()
b.leopard()