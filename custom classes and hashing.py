class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        print(f'Person(name={self.name},age={self.age})')
        p1 = Person('john', 78)
        p2 = Person('john', 75)
        hash(p1),hash(p2)
        print(p1 is p2)
        print(p1 == p2)

        p1 = Person('john',78)
        p2 = Person('john',75)
        persons = {p1: 'John object', p2:'Eric object'}
        for k in persons.keys():
              print(k)

        print(persons)