from sandbox import PositiveDefinite
from unittest import TestCase


class TestSandbox(TestCase):

    def setUp(self) -> None:
        print(__name__)

    def test_sandbox(self):
        self.assertEqual("Expected", "Actual", "Smoke Test")
