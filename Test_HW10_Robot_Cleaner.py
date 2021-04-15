import unittest
import HW10_RobotCleaner


class TestRobotCleaner(unittest.TestCase):
    def setUp(self):
        self.vasya = HW10_RobotCleaner.RobotCleaner(-5, 500, 500)
        self.petya = HW10_RobotCleaner.RobotCleaner(0, 0, 0)
        self.zhorick = HW10_RobotCleaner.RobotCleaner("50", -350, 300)
        self.kuzia = HW10_RobotCleaner.RobotCleaner(60, 0, -60)
        self.robots = [self.vasya, self.petya, self.zhorick, self.kuzia]

    def test_init(self):
        with self.assertRaises(ValueError):
            self.r_test1 = HW10_RobotCleaner.RobotCleaner("60", "p", [300])
        with self.assertRaises(TypeError):
            self.r_test2 = HW10_RobotCleaner.RobotCleaner(None, {450}, "0")
        for r in self.robots:
            self.assertIsInstance(r.charge_battery, float, "Value is not a number!")
            self.assertIsInstance(r.trash_can, float, "Value is not a number!")
            self.assertIsInstance(r.water_quantity, float, "Value is not a number!")

    def test_wash(self):
        for r in self.robots:
            self.assertGreaterEqual(r.water_quantity, 0, "Negative value!")
            self.assertLessEqual(r.water_quantity, 1000, "More than 500!")
            with self.assertRaises(HW10_RobotCleaner.NoWater):
                HW10_RobotCleaner.RobotCleaner(90, 0, 0).wash()

    def test_vacuum_cleaner(self):
        for r in self.robots:
            self.assertGreaterEqual(r.charge_battery, 0, "Negative value!")
            self.assertLessEqual(r.charge_battery, 100, "More than 100!")
            self.assertGreaterEqual(r.trash_can, 0, "Negative value!")
            self.assertLessEqual(r.trash_can, 500, "More than 500!")
            with self.assertRaises(HW10_RobotCleaner.LowBattery):
                HW10_RobotCleaner.RobotCleaner(9, 250, 500).vacuum_cleaner()
            with self.assertRaises(HW10_RobotCleaner.NoCharge):
                HW10_RobotCleaner.RobotCleaner(0, 100, 200).vacuum_cleaner()
            with self.assertRaises(HW10_RobotCleaner.FullTrash):
                HW10_RobotCleaner.RobotCleaner(50, 501, 400).vacuum_cleaner()

    def test_move(self):
        for r in self.robots:
            with self.assertRaises(SystemExit):
                try:
                    r.move()
                except HW10_RobotCleaner.NoCharge:
                    break
            return


if __name__ == "__main__":
    unittest.main()
