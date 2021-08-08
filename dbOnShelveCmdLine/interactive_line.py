import shelve
from Person_Manager import *
db = shelve.open('./databases/staff')
fields = ('name', 'age', 'pay', 'job')
maxfieldlength = max(len(field) for field in fields)
while True:
    key = input('Enter person\'s name to load/add new person: ')
    if not key: break
    if key in db:
        for field in fields:
            print('%s => %s' % (field.ljust(maxfieldlength), getattr(db[key], field)))
    else:
        answer = input('Want to make new record? (Yes, No) ')
        if (not answer or answer == 'Yes'):
            name = input('\nname: \n')
            age = int(input('age: \n'))
            pay = int(input('pay: \n'))
            job = input('job: \n')
        db[name] = Person(name, age, pay, job)
