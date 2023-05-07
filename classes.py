from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    pass

class Record:
    def __init__(self, name, phone=None):
        self.name = Name(name)
        self.phones = []
        if phone:
            self.add_phone(phone)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def edit_phone(self, index, phone):
        self.phones[index] = Phone(phone)
    
    def delete_phone(self, index):
        del self.phones[index]
    
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

