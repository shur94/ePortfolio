import unittest
from driverless_system import DriverlessSystem, Camera, Obstacle, Decision, Data

class TestDriverlessSystem(unittest.TestCase):
    def setUp(self):
        # Create a DriverlessSystem instance before each test method
        self.system = DriverlessSystem()

    def test_make_decision(self):
        print("Testing make_decision method...")
        # Test the make_decision method when obstacle is detected
        self.system.obstacle.detected = 1
        self.system.make_decision()
        self.assertEqual(self.system.decision.result, 1)  # Expect decision to proceed
        print("Test for obstacle detection passed.")

        # Test the make_decision method when no obstacle is detected
        self.system.obstacle.detected = 0
        self.system.make_decision()
        self.assertEqual(self.system.decision.result, 0)  # Expect decision to halt
        print("Test for no obstacle detection passed.")

    def test_detect_obstacle(self):
        print("Testing detect_obstacle method...")
        # Test the detect_obstacle method to ensure it sets obstacle.detected correctly
        self.system.detect_obstacle()
        self.assertIn(self.system.obstacle.detected, [0, 1])  # Expect obstacle.detected to be 0 or 1
        print("Test for obstacle detection passed.")

    def test_store_data(self):
        print("Testing store_data method...")
        # Call the store_data method
        self.system.store_data()

        # Check if raw_data attribute is not None
        self.assertIsNotNone(self.system.data.raw_data)
        print("Test for data storage passed.")


if __name__ == '__main__':
    while True:
        unittest.main(argv=[''], exit=False)
        restart = input("Do you want to restart the test? (yes/no): ")
        if restart.lower() != 'yes':
            break
