import unittest
from vegans import Vegans


class TestTraining(unittest.TestCase):
    def test_loading_pretrained(self):
        model = Vegans()
        model.load_pretrained()

    def test_generator(self):
        model = Vegans()
        print("TODO, make generator")
        pass


if __name__ == "__main__":
    unittest.main()
