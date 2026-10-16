# test_outlinehexa.py
"""
Tests for OutlineHexa module.
"""

import unittest
from outlinehexa import OutlineHexa

class TestOutlineHexa(unittest.TestCase):
    """Test cases for OutlineHexa class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OutlineHexa()
        self.assertIsInstance(instance, OutlineHexa)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OutlineHexa()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
