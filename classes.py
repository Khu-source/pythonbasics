#class Point():
    #def __init__(self, x, y):
        #self.x = x
        #self.y = y

#p = Point(2, 8)
#print(p.x)
#print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passenger.append(name)
        return True

    def open_seats(self):
        return self.capactity - len(self.passengers)

flight = Flight(3)

people = ["a","b","c","d"]

for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} successfully")
    else:
        print(f"Not added {person} successfully")