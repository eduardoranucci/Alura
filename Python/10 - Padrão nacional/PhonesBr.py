from http import server
import re as regex


class PhonesBr:

    def __init__(self, phone):
        
        if self.validate_phone(phone):
            self.number = phone
        else:
            raise ValueError('Phone number incorrect.')

    def __str__(self):
        return self.format_number()

    def validate_phone(self, phone):
        pattern = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        search = regex.findall(pattern, phone)
        if search:
            return True
        else:
            return False

    def format_number(self):
        pattern = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        search = regex.search(pattern, self.number)
        if search.group(1) == None:
            formatted_number = f'+55({search.group(2)}){search.group(3)}-{search.group(4)}'
        else:
            formatted_number = f'+{search.group(1)}({search.group(2)}){search.group(3)}-{search.group(4)}'
        return formatted_number 