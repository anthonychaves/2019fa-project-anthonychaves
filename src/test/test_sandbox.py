import pytest

from sandbox import PositiveDefinite
from unittest import TestCase


class TestSandbox(TestCase):

    def setUp(self) -> None:
        print(__name__)

    def test_sandbox(self):
        class MyModel:
            a = PositiveDefinite()
            b = PositiveDefinite(100)

        mm = MyModel()

        # Exercise the __set__ method in PositiveDefinite
        mm.a = 5
        # Exercise the __get__ method, and test the result of __set__ and __get__.
        self.assertEqual(5, mm.a, "Descriptor __get__ method.")

        # We expect a ValueError when we pass in a negative number
        with pytest.raises(ValueError) as e:
            mm.a = -5

        self.assertEqual(1, len(e.value.args))
        self.assertEqual("Value is definitely not positive.", e.value.args[0])

        # We expect a value error when we pass a non-int value
        with pytest.raises(ValueError) as e:
            mm.a = "test"

        self.assertEqual(1, len(e.value.args))
        self.assertEqual("Value is definitely not positive.", e.value.args[0])

        # We need to exercise the initval assignment
        self.assertEqual(100, mm.b, "Descriptor default initval")
