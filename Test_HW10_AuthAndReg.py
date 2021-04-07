import unittest
import HW10_AuthAndReg as Ar


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.test_reg = Ar.Registration()

    def test_user_registration(self):
        with self.assertRaises(Ar.EmailLenError):
            self.test_reg.user_registration("@", "0987y098")
        with self.assertRaises(Ar.EmailInvSymbolsError):
            self.test_reg.user_registration("ar!ra@gmail.com", "oij6oij0i")
        with self.assertRaises(Ar.UserExistError):
            self.test_reg.user_registration("mail2@gmail.com", "23456789")
        with self.assertRaises(Ar.PasswordLenError):
            self.test_reg.user_registration("luhiku@i.ua", "i")
        with self.assertRaises(Ar.PasswordInvSymbolsError):
            self.test_reg.user_registration("shgshg@i.ua", "loi4gli7g]k")
        self.assertEqual(self.test_reg.user_registration("uygkluyg@gmail.com", "i86ri67lk"), "200")
        self.assertEqual(self.test_reg.user_registration("mymail@gmail.com", "m1password"), "200")

    def tearDown(self):
        pass


class TestAuthorization(unittest.TestCase):
    def setUp(self):
        self.test_auth = Ar.Authorization()

    def test_authorization(self):
        with self.assertRaises(Ar.AuthorizationError):
            self.test_auth.user_authorization("uykjy@gmail.com", "87658768")
        self.assertEqual(self.test_auth.user_authorization("mail1@gmail.com", "12345678"), self.test_auth.token.id)

    def tearDown(self):
        pass
