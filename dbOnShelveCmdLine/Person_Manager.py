import shelve
class Person:
    def __init__(self, name, age, pay = 0, job = None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
    def giveRaise(self, percent):
        self.pay = self.pay * (1 + percent)
    def getLastName(self):
        return self.name.split()[-1]
    def __str__(self):
        str = ''
        for entry in self.__dict__:
            str += '%s => %s\n' % (entry, getattr(self, entry)) if not entry.startswith('__') else ''
        return str
    def dumpToDB(self, dbname):
        db = shelve.open(dbname)
        db[self.name] = self
        db.close()
        print('Dumped %s to %s database' % (self.name, dbname))
class Manager(Person):
    def __init__(self, name, age, pay = 0):
        Person.__init__(self, name, age, pay, 'manager')
    def giveRaise(self, percent, bonus = 0.1):
        Person.giveRaise(self, percent + bonus)



if __name__ == '__main__':
    bob = Person('Bob Larson', 27, 18300, 'police officer')
    sue = Person('Sue Jackson', 22)
    print(bob)
    print(sue)
    bob.dumpToDB('./databases/staff')
    db = shelve.open('./databases/staff')
    print(db['Bob Larson'])
