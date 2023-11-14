import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle

class TestSquare(unittest.TestCase):
    """Unit tests for the Square class."""

    def test_square_instantiation(self):
        """Test the instantiation of the Square class."""
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_square_with_negative_size(self):
        """Test the instantiation of Square with a negative size."""
        with self.assertRaises(ValueError):
            Square(-5, 2, 3, 1)

    def test_square_with_negative_x(self):
        """Test the instantiation of Square with a negative x-coordinate."""
        with self.assertRaises(ValueError):
            Square(5, -2, 3, 1)

    def test_square_with_negative_y(self):
        """Test the instantiation of Square with a negative y-coordinate."""
        with self.assertRaises(ValueError):
            Square(5, 2, -3, 1)

    def test_square_update(self):
        """Test the update method of Square."""
        square = Square(10, 10, 10, 1)
        square.update(2, 2, 2, 2)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 2)

    def test_square_to_dictionary(self):
        """Test the to_dictionary method of Square."""
        square = Square(5, 5, 5, 1)
        dictionary = square.to_dictionary()
        expected_dict = {'id': 1, 'size': 5, 'x': 5, 'y': 5}
        self.assertDictEqual(dictionary, expected_dict)

    def test_square_str_representation(self):
        """Test the string representation of Square."""
        square = Square(4, 2, 1, 12)
        self.assertEqual(str(square), "[Square] (12) 2/1 - 4")

    def test_square_size_large_values(self):
        """Test the size property with large values."""
        square = Square(10**6, 2, 3, 1)
        self.assertEqual(square.size, 10**6)

    def test_square_update_large_values(self):
        """Test the update method with large values."""
        square = Square(10**6, 10**6, 10**6, 1)
        square.update(2, 2, 2, 2)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 2)

    def test_square_to_dictionary_large_values(self):
        """Test the to_dictionary method with large values."""
        square = Square(10**6, 10**6, 10**6, 1)
        dictionary = square.to_dictionary()
        expected_dict = {'id': 1, 'size': 10**6, 'x': 10**6, 'y': 10**6}
        self.assertDictEqual(dictionary, expected_dict)

    def test_square_str_representation_large_values(self):
        """Test the string representation of Square with large values."""
        square = Square(10**6, 10**6, 10**6, 1)
        self.assertEqual(str(square), "[Square] (1) 1000000/1000000 - 1000000")


if __name__ == "__main__":
    unittest.main()

