class Person:
    def __init__(self, name):
        self.name = name


class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f'{person.name} se ha subido al bus')
        else:
            print(f"El bus esta lleno {person.name} no puede subir")

    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f'{person.name} se ha bajado del bus')
        else:
            print(f'{person.name} no se encuentra en el bus')


person1 = Person("Carlos")
person2 = Person("Luis")
person3 = Person("Sergio")

bus = Bus(2)
bus.add_passenger(person1)
bus.add_passenger(person2)
bus.add_passenger(person3)

bus.remove_passenger(person2)
bus.remove_passenger(person3)
bus.remove_passenger(person2)