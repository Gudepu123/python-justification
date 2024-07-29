import unittest
from justify import justify_text

class TestJustifyText(unittest.TestCase):
    def test_justify_text(self):
        paragraph = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."
        width = 20
        expected_output = [
            "This  is  a   sample",
            "text      but      a",
            "complicated  problem",
            "to be solved, so  we",
            "are adding more text",
            "to   see   that   it",
            "actually      works."
        ]
        self.assertEqual(justify_text(paragraph, width), expected_output)

if __name__ == "__main__":
    unittest.main()
