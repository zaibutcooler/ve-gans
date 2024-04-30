import unittest
from vegans import Vegans


class TestTraining(unittest.TestCase):
    def test_training(self):
        model = Vegans()
        model.train(upload=False, real=False)


if __name__ == "__main__":
    unittest.main()
