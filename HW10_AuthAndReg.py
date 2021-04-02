import uuid


class MyBaseException(Exception):
    pass


class EmailInvSymbolsError(MyBaseException):
    pass


class PasswordInvSymbolsError(MyBaseException):
    pass


class EmailLenError(MyBaseException):
    pass


class PasswordLenError(MyBaseException):
    pass


class UserExistError(MyBaseException):
    pass


class AuthorizationError(MyBaseException):
    pass


wrong_symbols = ["?", "!", ",", " ", "(", ")", "[", "]", "{", "}", "=", "+", "-", "*", "/", r"\\", "'", '"', ".",
                 "@", "%", "$", "#", "|", "<", ">", "~", "`"]

wrong_symbols1 = ["?", "!", ",", " ", "(", ")", "[", "]", "{", "}", "=", "+", "-", "*", "/", r"\\", "'", '"',
                  "%", "$", "#", "|", "<", ">", "~", "`"]

email_symbols = ["@", "."]

database = {"mail1@gmail.com": "12345678", "mail2@gmail.com": "23456789", "mail3@gmail.com": "34567891"}


class UserToken:
    def __init__(self):
        self.id = uuid.uuid4()

    def __str__(self):
        return self.id


class Registration:

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def check_email_len(self):
        if len(self.email) < 4 or len(self.email) > 30:
            return False
        return True

    def check_email_symbols(self):
        for e in self.email:
            if e in wrong_symbols1:
                return False
            elif ["@", "."] not in self.email:
                return False
            return True

    def check_exist(self):
        if self.email not in database:
            database.update({self.email: self.password})
            return True
        return False

    def check_password_len(self):
        if len(self.password) < 8 or len(self.password) > 15:
            return False
        return True

    def check_password_symbols(self):
        for p in self.password:
            if p in wrong_symbols:
                return False
            return True

    def user_registration(self):
        if self.check_email_len() is False:
            raise EmailLenError("Email should have from 4 to 30 symbols length!")
        elif self.check_email_symbols() is False:
            raise EmailInvSymbolsError("Your email has invalid symbol(s)!")
        elif self.check_exist() is True:
            raise UserExistError("This user already exists")
        elif self.check_password_len() is False:
            raise PasswordLenError("Password should have from 8 to 16 symbols length!")
        elif self.check_password_symbols() is False:
            raise PasswordInvSymbolsError("Your password has invalid symbol(s)!")
        else:
            return "200"


class Authorization:
    token = UserToken()

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def check_user(self):
        if self.email in database.keys():
            if self.password == database[self.email]:
                return True
            return False
        return False

    def user_authorization(self):
        if self.check_user() is False:
            return self.token
        raise AuthorizationError("Authorization Error!")


user = Registration("mail@gmail.com", "12345678")
