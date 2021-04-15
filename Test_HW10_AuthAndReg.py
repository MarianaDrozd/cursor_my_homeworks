import unittest
import HW10_AuthAndReg as Ar


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.test_reg = Ar.Registration()

    def test_check_email_len(self):
        self.assertEqual(self.test_reg.check_email_len("qwasdrt@gmail.com"), True)
        self.assertEqual(self.test_reg.check_email_len("qwasdt@i.ua"), True)
        self.assertEqual(self.test_reg.check_email_len("@i.ua"), False)
        self.assertEqual(self.test_reg.check_email_len("qwasdrtiuiuiuiuiuiuiuiuiuiuiuiu@gmail.com"), False)

    def test_check_email_symbols(self):
        self.assertEqual(self.test_reg.check_email_symbols("qwast@gmail.com"), True)
        self.assertEqual(self.test_reg.check_email_symbols("q!!@gmail.com"), False)
        self.assertEqual(self.test_reg.check_email_symbols("(wast)@gmail.com"), False)
        self.assertEqual(self.test_reg.check_email_symbols("q wast@gmail.com"), False)
        self.assertEqual(self.test_reg.check_email_symbols("q   @gmail.com"), False)
        self.assertEqual(self.test_reg.check_email_symbols("qwastgmailcom"), False)

    def test_check_password_len(self):
        self.assertEqual(self.test_reg.check_password_len("8u65drt66uyll"), True)
        self.assertEqual(self.test_reg.check_password_len("8"), False)
        self.assertEqual(self.test_reg.check_password_len("8u65drt6ru6ru6ru6o7ti7t66uyll"), False)

    def test_check_password_symbols(self):
        self.assertEqual(self.test_reg.check_password_symbols("8u65drt60zll"), True)
        self.assertEqual(self.test_reg.check_password_symbols("8 i6dcf6lo"), False)
        self.assertEqual(self.test_reg.check_password_symbols("         "), False)
        self.assertEqual(self.test_reg.check_password_symbols("[]kin%]"), False)

    def test_check_nickname_len(self):
        self.assertEqual(self.test_reg.check_nickname_len("Uliana"), True)
        self.assertEqual(self.test_reg.check_nickname_len("Ul"), False)
        self.assertEqual(self.test_reg.check_nickname_len("UlianaGarnaDivchyna"), False)
        self.assertEqual(self.test_reg.check_nickname_len(""), False)

    def test_check_nickname_symbols(self):
        self.assertEqual(self.test_reg.check_nickname_symbols("Світлана"), True)
        self.assertEqual(self.test_reg.check_nickname_symbols("Svitlana"), True)
        self.assertEqual(self.test_reg.check_nickname_symbols("Світлан@"), False)
        self.assertEqual(self.test_reg.check_nickname_symbols("Св%тлана"), False)
        self.assertEqual(self.test_reg.check_nickname_symbols("Світ лана"), False)
        self.assertEqual(self.test_reg.check_nickname_symbols("В'ячеслав"), True)
        self.assertEqual(self.test_reg.check_nickname_symbols("      "), False)

    def test_user_registration(self):
        with self.assertRaises(Ar.EmailLenError):
            self.test_reg.user_registration("@.", "0987y098", "liu8o9")
        with self.assertRaises(Ar.EmailInvSymbolsError):
            self.test_reg.user_registration("ar!ra@gmail.com", "oij6oij0i", "luyluyt")
        with self.assertRaises(Ar.UserExistError):
            self.test_reg.user_registration("mail2@gmail.com", "23456789", "Olenka")
        with self.assertRaises(Ar.PasswordLenError):
            self.test_reg.user_registration("luhiku@i.ua", "i", "uyfrefrr")
        with self.assertRaises(Ar.PasswordInvSymbolsError):
            self.test_reg.user_registration("shgshg@i.ua", "loi4gli7g]k", "dstrwsht")
        with self.assertRaises(Ar.NicknameLenError):
            self.test_reg.user_registration("shgktdkt@i.ua", "loi4glolkju", "ds")
        with self.assertRaises(Ar.NicknameInvSymbolsError):
            self.test_reg.user_registration("shgktdkt@i.ua", "loi4glolkju", "d&okugcds")
        with self.assertRaises(Ar.NicknameExistError):
            self.test_reg.user_registration("shgktdkt@i.ua", "loi4glolkju", "Oleg")
        self.assertEqual(self.test_reg.user_registration("uygkluyg@gmail.com", "i86ri67lk", "Petro"), "200")
        self.assertEqual(self.test_reg.user_registration("mymail@gmail.com", "m1password", "Орися"), "200")


class TestAuthorization(unittest.TestCase):
    def setUp(self):
        self.test_auth = Ar.Authorization()

    def test_check_user(self):
        self.assertEqual(self.test_auth.check_user("mail1@gmail.com", "12345678", "Oleg"), True)
        self.assertEqual(self.test_auth.check_user("mail1@gmail.com", "9258452858", "Oleg"), False)
        self.assertEqual(self.test_auth.check_user("mail1@gmail.com", "12345678", "Nataliya"), False)

    def test_authorization(self):
        with self.assertRaises(Ar.AuthorizationError):
            self.test_auth.user_authorization("uykjy@gmail.com", "87658768", "Igor")
        with self.assertRaises(Ar.AuthorizationError):
            self.test_auth.user_authorization("mail1@gmail.com", "12345678", "Igor")
        with self.assertRaises(Ar.AuthorizationError):
            self.test_auth.user_authorization("mail1@gmail.com", "12345679", "Oleg")
        self.assertEqual(self.test_auth.user_authorization("mail1@gmail.com", "12345678", "Oleg"),
                         self.test_auth.token.id)
        self.assertEqual(self.test_auth.user_authorization("mail3@gmail.com", "34567891", "Мар'яна"),
                         self.test_auth.token.id)


if __name__ == "__main__":
    unittest.main()
