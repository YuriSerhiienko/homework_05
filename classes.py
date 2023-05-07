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
        if isinstance(phone, str):
            phone = Phone(phone)
        if phone not in self.phones:
            self.phones.append(phone)
    
    def edit_phone(self, index, phone):
        self.phones[index] = Phone(phone)
    
    def delete_phone(self, index):
        del self.phones[index]
    
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def search(self, name=None, phone=None):
        results = []
        for contact in self.data.values():
            if (name and name.lower() in contact.name.value.lower()) or (phone and phone in [phone.value for phone in contact.phones]):
                results.append(contact)
        return results
