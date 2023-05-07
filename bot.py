from classes import Record, AddressBook

phonebook = AddressBook()

def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return "There is no such name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Enter user name"
        except TypeError:
            return "Incorrect values"
    return inner

@input_error
def greeting():
    return "How can I help you?"

def unknown_command():
    return "Unknown command"

@input_error
def exit():
    return None

@input_error
def add_user(name, phone=None):
    record = phonebook.get(name, None)
    if record:
        if phone:
            record.add_phone(phone)
            return "Contact successfully updated"
        else:
            return "Contact already exists"
    else:
        if phone:
            record = Record(name, phone)
        else:
            record = Record(name)
        phonebook.add_record(record)
        return "Contact added successfully"


@input_error
def change_phone(name, phone):
    record = phonebook.get(name, None)
    if record:
        record.edit_phone(index=0, phone=phone)
        return "Phone number updated successfully"
    else:
        return "There is no such name"

def show_all():
    if not phonebook:
        return "The phonebook is empty"
    result = ''
    for record in phonebook.values():
        phones = ', '.join([phone.value for phone in record.phones])
        result += f"{record.name.value}: {phones}\n"
    return result.rstrip()


@input_error
def get_phone_number(name):
    record = phonebook.get(name, None)
    if record:
        if record.phones:
            return ', '.join([phone.value for phone in record.phones])
        else:
            return "Contact has no data"
    else:
        return "There is no such name"




commands = {
    'hello': greeting,
    'add': add_user,
    'change': change_phone,
    'show all': show_all,
    "phone": get_phone_number,
    'exit': exit,
    'good bye': exit,
    'close': exit,
}

def main():
    while True:
        command, *args = input(">>> ").strip().split(' ', 1)
        if commands.get(command):
            handler = commands.get(command)
            if args:
                args = args[0].split()
                result = handler(*args)
            else:
                result = handler(*args)
        elif args and commands.get(command + ' ' + args[0]):
            command = command + ' ' + args[0]
            args = args[1:]
            handler = commands.get(command)
            result = handler(*args)
        else:
            result = unknown_command()

        if not result:
            print('Good bye!')
            break

        print(result)

if __name__ == "__main__":
    main()
