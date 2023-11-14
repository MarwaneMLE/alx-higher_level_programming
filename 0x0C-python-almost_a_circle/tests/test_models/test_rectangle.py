import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Unit tests for the Rectangle class."""

    def test_rectangle_instantiation(self):
        """Test the instantiation of the Rectangle class."""
        rectangle = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)
        self.assertEqual(rectangle.id, 1)

    def test_rectangle_with_negative_width(self):
        """Test the instantiation of Rectangle with a negative width."""
        with self.assertRaises(ValueError):
            Rectangle(-5, 10, 2, 3, 1)

    def test_rectangle_with_negative_height(self):
        """Test the instantiation of Rectangle with a negative height."""
        with self.assertRaises(ValueError):
            Rectangle(5, -10, 2, 3, 1)

    def test_rectangle_with_negative_x(self):
        """Test the instantiation of Rectangle with a negative x-coordinate."""
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -2, 3, 1)

    def test_rectangle_with_negative_y(self):
        """Test the instantiation of Rectangle with a negative y-coordinate."""
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 2, -3, 1)

    def test_rectangle_area(self):
        """Test the area method of Rectangle."""
        rectangle = Rectangle(4, 5)
        self.assertEqual(rectangle.area(), 20)

    def test_rectangle_display(self):
        """Test the display method of Rectangle."""
        rectangle = Rectangle(3, 2)
        self.assertEqual(rectangle.display(), None)  # Not testing stdout here

    def test_rectangle_update(self):
        """Test the update method of Rectangle."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        rectangle.update(2, 2, 2, 2, 2)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 2)

    def test_rectangle_to_dictionary(self):
        """Test the to_dictionary method of Rectangle."""
        rectangle = Rectangle(5, 5, 5, 5, 1)
        dictionary = rectangle.to_dictionary()
        expected_dict = {'id': 1, 'width': 5, 'height': 5, 'x': 5, 'y': 5}
        self.assertDictEqual(dictionary, expected_dict)

    def test_rectangle_str_representation(self):
        """Test the string representation of Rectangle."""
        rectangle = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(rectangle), "[Rectangle] (12) 2/1 - 4/6")

    def test_rectangle_area_large_values(self):
        """Test the area method with large values."""
        rectangle = Rectangle(10**6, 10**6)
        self.assertEqual(rectangle.area(), 10**12)

    def test_rectangle_display_large_values(self):
        """Test the display method with large values."""
        rectangle = Rectangle(5, 5, 2, 2)
        self.assertEqual(rectangle.display(), None)  # Not testing stdout here

    def test_rectangle_update_negative_values(self):
        """Test the update method with negative values."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        rectangle.update(-2, -2, -2, -2, -2)
        self.assertEqual(rectangle.id, -2)
        self.assertEqual(rectangle.width, -2)
        self.assertEqual(rectangle.height, -2)
        self.assertEqual(rectangle.x, -2)
        self.assertEqual(rectangle.y, -2)

    def test_rectangle_to_dictionary_large_values(self):
        """Test the to_dictionary method with large values."""
        rectangle = Rectangle(10**6, 10**6, 10**6, 10**6, 1)
        dictionary = rectangle.to_dictionary()
        expected_dict = {'id': 1, 'width': 10**6, 'height': 10**6, 'x': 10**6, 'y': 10**6}
        self.assertDictEqual(dictionary, expected_dict)

    def test_rectangle_str_representation_large_values(self):
        """Test the string representation of Rectangle with large values."""
        rectangle = Rectangle(10**6, 10**6, 10**6, 10**6, 1)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 1000000/1000000 - 1000000/1000000")


if __name__ == "__main__":
    unittest.main()

