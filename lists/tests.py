from django.test import TestCase

class SmokeTest(TestCase):
    """Does our magically-created test runner even run a unittest?"""

    def test_bad_adding(self):
        self.assertEqual("apple" + "berry", 42)