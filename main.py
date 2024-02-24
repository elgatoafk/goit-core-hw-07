from collections import UserDict

"""Tools for working with functions and callable objects"""
from functools import wraps


def name_validation(func):
    # name can only contain letters
    @wraps(func)
    def inner(self, entered_name):
        if not entered_name.isalpha():
            print("The provided name is in incorrect format and cannot be accepted")
        return func(self, entered_name)

    return inner


def phone_validation(func):
    # phone can only contain numbers and must be 10 charaters long
    @wraps(func)
    def inner(self, *args):
        for arg in args:
            if not (arg.isdigit() and len(arg) == 10):
                print(f"{arg} is in incorrect format")
                return None
        return func(self, *args)

    return inner


class Field:
    # defining base class
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):

    @name_validation
    def __init__(self, entered_name):
        super().__init__(entered_name)

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, key):
        return str(self) == key


class Phone(Field):

    @phone_validation
    def __init__(self, phone):
        super().__init__(phone)

class Birthday(Field):
    def __init__(self, value):
        try:
            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")




class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    @phone_validation
    def add_phone(self, phone):
        self.phones.append(phone)

    @phone_validation
    def find_phone(self, phone):
        try:
            found = self.phones.index(phone)
            return self.phones[found]
        except ValueError:
            print("No such phone here, wanna add it?")

    @phone_validation
    def edit_phone(self, old_phone, new_phone):
        if old_phone in self.phones:
            index = self.phones.index(old_phone)
            self.phones[index] = new_phone
            print("Number edited")
        else:
            print("No such phone here")

    @phone_validation
    def delete_phone(self, phone):
        try:
            self.phones.remove(phone)
            print("Success, phone removed")
        except ValueError:
            print("No such phone found in the record")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, entered_record: Record):
        self.data[entered_record.name] = entered_record

    def find(self, entered_name):
        if entered_name in self.data.keys():
            print(f"Fetching {entered_name}...")
            return self.data.get(entered_name)
        else:
            print(f"Who is this {entered_name}?")

    def delete(self, name):
        if name in self.data:
            print(f"Deleting {name}...")
            del self.data[name]

        else:
            print(f"{name} does not exist")
