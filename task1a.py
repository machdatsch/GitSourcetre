
class password(object):
    def __init__(self,password):
        self.password = password
    def __str__(self):
        return len(self.password)*"*"
    def resolve_password(self):
        return self.password
    def change_password(self,other):
        self.password = other
        return self.password
    def check_validity(self,*args):
        for arg in args:
            if arg(self.password) == False:
                return False
            else:
                return True

################################################################################

### validity check functions ###

def no_shorter_than_8(string):
    "checks that a given string is not shorter than 8 characters"

    return len(string) >= 8

def contains_special_chars(string):
    "checks that a given string does contain special characters"

    return not string.isalnum()

def starts_upper_case(string):
    "checks that a given string begins with an upper case letter"

    if string[0].isupper():
        return True
    return False

################################################################################

### some test cases ###

pw1 = password("Password_1234")
print(pw1) # should print: *************
print(pw1.resolve_password()) # should print: Password_1234
print(pw1.check_validity(no_shorter_than_8,contains_special_chars,starts_upper_case)) # should print: True
print(pw1.change_password("password_1234"))
print(pw1.check_validity(starts_upper_case)) # should print: False

