from unittest import TestCase

from main import *


class TestML(TestCase):
    scores = None
    avg = None

    @classmethod
    def setUpClass(cls):
        cls.scores = [1, 1.5, 2, 1.8, 3, 1.15, 1.55, 2]
        cls.avg = sum(cls.scores)/len(cls.scores)

    @staticmethod
    def is_close_to(data, target=1, error=0.01):
        """
        Returns true if the target is within a  1% error
        range of the target value.
        """
        diff = abs(target - data)
        return diff/target <= error

    def test_softmax_total(self):
        """
        Tests to make sure the total value returned by
        the softmax function is ~1.
        """
        result = softmax(self.scores)
        test_max = 0
        for score in self.scores:
            test_max += result[score]
        assert(type(result) == dict)
        assert(self.is_close_to(test_max))

    def test_one_hot_encoding(self):
        """
        Tests the one-hot encoding to ensure only 1 value
        was set to 1.
        """
        result = one_hot_encode(softmax(self.scores))
        count = len(list(filter(lambda x: x==1, result.values())))
        assert(count == 1)
