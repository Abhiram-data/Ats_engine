
import unittest
import os

class TestAISystem(unittest.TestCase):
    def test_modular_folders(self):
        # Verify the structure designed in the tasks [cite: 7]
        folders = ['ats_engine', 'screening_ai', 'interview_ai']
        for folder in folders:
            self.assertTrue(os.path.exists(folder), f"{folder} is missing!")

if __name__ == '__main__':
    unittest.main()