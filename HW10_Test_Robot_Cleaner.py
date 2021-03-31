import unittest
import HW10_RobotCleaner


class TestRobotCleaner(unittest.TestCase):
    def setUp(self):
        self.vasya = HW10_RobotCleaner.RobotCleaner(-5, 500, 600)
        self.petya = HW10_RobotCleaner.RobotCleaner(0, 0, 0)
        self.zhorick = HW10_RobotCleaner.RobotCleaner("50", -350, 300)
        self.kuzia = HW10_RobotCleaner.RobotCleaner(60, 0, -60)
        with self.assertRaises(ValueError):
            self.r_test1 = HW10_RobotCleaner.RobotCleaner("60", "p", [300])
        with self.assertRaises(TypeError):
            self.r_test2 = HW10_RobotCleaner.RobotCleaner(None, {450}, "0")

        self.robots = [self.vasya, self.petya, self.zhorick, self.kuzia]

    def test_init(self):
        for r in self.robots:
            self.assertIsInstance(r.charge_battery, float, "Value is not a number!")
            self.assertIsInstance(r.trash_can, float, "Value is not a number!")
            self.assertIsInstance(r.water_quantity, float, "Value is not a number!")

    def test_wash(self):
        for r in self.robots:
            self.assertGreaterEqual(r.water_quantity, 0, "Negative value!")
            self.assertLessEqual(r.water_quantity, 1000, "More than 500!")

    def test_vacuum_cleaner(self):
        for r in self.robots:
            self.assertGreaterEqual(r.charge_battery, 0, "Negative value!")
            self.assertLessEqual(r.charge_battery, 100, "More than 100!")
            self.assertGreaterEqual(r.trash_can, 0, "Negative value!")
            self.assertLessEqual(r.trash_can, 500, "More than 500!")


    def test_move(self):
        i = 1
        for r in self.robots:
            print(f"=========Test move {i} {r.__class__.__name__}=========")
            i += 1
            with self.assertRaises(SystemExit):
                try:
                    r.move()
                except HW10_RobotCleaner.NoCharge:
                    break
        return

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
