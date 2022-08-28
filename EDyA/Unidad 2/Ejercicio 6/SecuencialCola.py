from gettext import install
from typing import Any

class Cola:
    __cola: list[Any]

    def __init__(self):
        self.__cola=[]

    def add(self, item):
        self.__cola.append(item)
    
    def remove(self):
        self.__cola.pop(0)
    
    def getSize(self):
        return(len(self.__cola))

    def watch(self):
        for i in self.__cola:
            print(i)

if __name__=="__main__":
    cola=Cola()
    cola.add(1)
    cola.add(2)
    cola.add(3)
    cola.add(4)

    cola.remove()
    cola.watch()


