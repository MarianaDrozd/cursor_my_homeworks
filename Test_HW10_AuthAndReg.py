import HW10_AuthAndReg as Ar
import unittest


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.test_reg = Ar.Registration

    def test_user_registration(self):
        with self.assertRaises(Ar.EmailLenError):
            self.test_reg("@", "0987y098")
        with self.assertRaises(Ar.EmailInvSymbolsError):
            self.test_reg("ar!ra@gmail.com", "oij6oij0i")
        with self.assertRaises(Ar.UserExistError):
            self.test_reg("mymail@gmail.com", "m1password")
        with self.assertRaises(Ar.PasswordLenError):
            self.test_reg("luhiku@i.ua", "i")
        with self.assertRaises(Ar.PasswordInvSymbolsError):
            self.test_reg("shgshg@i.ua", "loi4gli7g]k")
        self.assertEqual(str(self.test_reg("uygkluyg@gmail.com", "i86ri67lk")), "200")
        self.assertEqual(str(self.test_reg("mymail@gmail.com", "m1password")), "200")

    def tearDown(self):
        pass


class TestAuthorization(unittest.TestCase):
    def setUp(self):
        self.user = Ar.Authorization

    def test_authorization(self):
        with self.assertRaises(Ar.AuthorizationError):
            self.user("uykjy@gmail.com", "87658768")
        self.assertEqual(Ar.Authorization("mail@gmail.com", "12345678"), Ar.UserToken())

    def tearDown(self):
        pass


