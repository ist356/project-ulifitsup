import unittest
from code.desc_clean import clean_desc

class TestCleanDesc(unittest.TestCase):

    def test_clean_desc_with_valid_description(self):
        description = """
        About the Role:
        This is a test role description.
        What You'll Do:
        Test the code.
        What You'll Need:
        Experience in testing.
        Benefits of Working at CrowdStrike:
        Many benefits.
        Expected Close Date of Job Posting is:01-26-2025
        """
        result = clean_desc(description)
        self.assertEqual(result["description"], "This is a test role description.")
        self.assertEqual(result["requirements"], ["Experience in testing."])
        self.assertEqual(result["deadline"], "01-26-2025")

    def test_clean_desc_without_about_role(self):
        description = """
        What You'll Do:
        Test the code.
        What You'll Need:
        Experience in testing.
        Benefits of Working at CrowdStrike:
        Many benefits.
        Expected Close Date of Job Posting is:01-26-2025
        """
        result = clean_desc(description)
        self.assertEqual(result["description"], "")
        self.assertEqual(result["requirements"], ["Experience in testing."])
        self.assertEqual(result["deadline"], "01-26-2025")

    def test_clean_desc_without_requirements(self):
        description = """
        About the Role:
        This is a test role description.
        What You'll Do:
        Test the code.
        Benefits of Working at CrowdStrike:
        Many benefits.
        Expected Close Date of Job Posting is:01-26-2025
        """
        result = clean_desc(description)
        self.assertEqual(result["description"], "This is a test role description.")
        self.assertEqual(result["requirements"], [])
        self.assertEqual(result["deadline"], "01-26-2025")

    def test_clean_desc_without_deadline(self):
        description = """
        About the Role:
        This is a test role description.
        What You'll Do:
        Test the code.
        What You'll Need:
        Experience in testing.
        Benefits of Working at CrowdStrike:
        Many benefits.
        """
        result = clean_desc(description)
        self.assertEqual(result["description"], "This is a test role description.")
        self.assertEqual(result["requirements"], ["Experience in testing."])
        self.assertEqual(result["deadline"], "")

    def test_clean_desc_with_empty_description(self):
        description = ""
        result = clean_desc(description)
        self.assertEqual(result["description"], "")
        self.assertEqual(result["requirements"], [])
        self.assertEqual(result["deadline"], "")

if __name__ == "__main__":
    unittest.main()