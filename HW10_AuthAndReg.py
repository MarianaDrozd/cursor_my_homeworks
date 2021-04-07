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
    @staticmethod
    def check_email_len(email):
        if len(email) < 4 or len(email) > 30:
            return False
        return True

    @staticmethod
    def check_email_symbols(email):
        for e in email:
            if e in wrong_symbols1:
                return False
            # elif "@." not in email:
            #     return False
            return True

    @staticmethod
    def check_password_len(password):
        if len(password) < 8 or len(password) > 15:
            return False
        return True

    @staticmethod
    def check_password_symbols(password):
        for p in password:
            if p in wrong_symbols:
                return False
            return True

    def user_registration(self, email, password):
        if self.check_email_len(email) is False:
            raise EmailLenError("Email should have from 4 to 30 symbols length!")
        elif self.check_email_symbols(email) is False:
            raise EmailInvSymbolsError("Your email has invalid symbol(s)!")
        elif email in database.keys():
            raise UserExistError("This user already exists")
        elif self.check_password_len(password) is False:
            raise PasswordLenError("Password should have from 8 to 16 symbols length!")
        elif self.check_password_symbols(password) is False:
            raise PasswordInvSymbolsError("Your password has invalid symbol(s)!")
        else:
            database.update({email: password})
            return "200"


class Authorization:
    token = UserToken()

    # def __init__(self, email: str, password: str):
    #     self.email = email
    #     self.password = password
    @staticmethod
    def check_user(email, password):
        if email in database.keys():
            if password in database.values():
                return True
            return False

    def user_authorization(self, email, password):
        if self.check_user(email, password) is True:
            return self.token.__str__()
        raise AuthorizationError("Authorization Error!")


# user1 = Registration()
#
# user1.user_registration("mail58@gmail.com", "12553478")
# print(database)
# user2 = Authorization()
#
# user2.user_authorization("mail1@gmail.com", "12345678")
