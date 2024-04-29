"""_summary_
El patrón Iterator se utiliza para proporcionar una 
forma de acceder secuencialmente a los elementos de una colección 
sin exponer su representación. 

En Python, este patrón es muy común y se implementa de forma natural
utilizando iteradores y generadores.
Raises:
    StopIteration: Cuando el iterator no tiene un next

Returns:
    string: Muestra por pantalla un listado de los elementos usados a travé de un iterador
"""

class Collection:
    def __init__(self):
        self.data = []

    def add_element(self, element):
        self.data.append(element)
    
    def __iter__(self):
        return Iterator(self.data)

class Iterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            element = self.data[self.index]
            self.index += 1
            return element
        else:
            raise StopIteration



demo_collection = Collection()
for value in range(1,10):
    demo_collection.add_element(f"{value}º Piso")


iterator = iter(demo_collection)
for element in iterator:
    print(element)
