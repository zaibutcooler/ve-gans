import unittest
from vegans.dataset import TrainingSet


class TestTraining(unittest.TestCase):
    def test_download_dataset(self):
        data = TrainingSet()
        data.download_dataset()
        assert data.images is not None
        assert data.labels is not None


if __name__ == "__main__":
    unittest.main()
