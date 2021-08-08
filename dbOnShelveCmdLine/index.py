import shelve
db = shelve.open('databases/staff')
print([db[field].name for field in db])
