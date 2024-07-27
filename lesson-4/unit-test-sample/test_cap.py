import unittest
import cap

class TestCap(unittest.TestCase):

    def test_single_word(self):
        text = "praddy"
        result = cap.capitaliseFunc(text)

        self.assertEqual(result, "Praddy")

    def test_multiple_word(self):
        text = "praddy is py"
        result = cap.capitaliseFunc(text)

        self.assertEqual(result, "Praddy Is Py")

if __name__ == "__main__":
    unittest.main()
