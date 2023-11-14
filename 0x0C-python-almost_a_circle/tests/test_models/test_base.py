import unittest
from models.base import Base
from models.square import Square
from models.square import Rectangle

class TestBase(unittest.TestCase):
    """Unit tests for the Base class."""

    def test_base_instantiation(self):
        """Test the instantiation of the Base class."""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_base_with_id(self):
        """Test the instantiation of Base with a specified ID."""
        base = Base(10)
        self.assertEqual(base.id, 10)

    def test_base_with_str_id(self):
        """Test the instantiation of Base with a string as ID."""
        base = Base("test_id")
        self.assertEqual(base.id, "test_id")

    def test_base_with_float_id(self):
        """Test the instantiation of Base with a float as ID."""
        base = Base(5.5)
        self.assertEqual(base.id, 5.5)

    def test_base_with_dict_id(self):
        """Test the instantiation of Base with a dictionary as ID."""
        base = Base({"a": 1, "b": 2})
        self.assertEqual(base.id, {"a": 1, "b": 2})

    def test_base_with_bool_id(self):
        """Test the instantiation of Base with a bool as ID."""
        base = Base(True)
        self.assertEqual(base.id, True)

    def test_base_with_list_id(self):
        """Test the instantiation of Base with a list as ID."""
        base = Base([1, 2, 3])
        self.assertEqual(base.id, [1, 2, 3])

    def test_base_with_tuple_id(self):
        """Test the instantiation of Base with a tuple as ID."""
        base = Base((1, 2))
        self.assertEqual(base.id, (1, 2))

    def test_base_with_set_id(self):
        """Test the instantiation of Base with a set as ID."""
        base = Base({1, 2, 3})
        self.assertEqual(base.id, {1, 2, 3})

    def test_base_with_inf_id(self):
        """Test the instantiation of Base with infinity as ID."""
        base = Base(float('inf'))
        self.assertEqual(base.id, float('inf'))

    def test_base_with_nan_id(self):
        """Test the instantiation of Base with NaN as ID."""
        base = Base(float('nan'))
        self.assertNotEqual(base.id, base.id)

    def test_base_with_two_args(self):
        """Test the instantiation of Base with two arguments."""
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_base_to_json_string_empty_list(self):
        """Test to_json_string method with an empty list."""
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_base_to_json_string_none_list(self):
        """Test to_json_string method with None."""
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_base_save_to_file_empty_list(self):
        """Test save_to_file method with an empty list."""
        Base.save_to_file([])
        with open("Base.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_base_save_to_file_none_list(self):
        """Test save_to_file method with None."""
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_base_from_json_string_empty_string(self):
        """Test from_json_string method with an empty string."""
        obj_list = Base.from_json_string("")
        self.assertEqual(obj_list, [])

    def test_base_from_json_string_none_string(self):
        """Test from_json_string method with None."""
        obj_list = Base.from_json_string(None)
        self.assertEqual(obj_list, [])

    def test_base_create_rectangle(self):
        """Test create method for Rectangle."""
        rect_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 0, 'y': 0}
        rect = Base.create(**rect_dict)
        self.assertIsInstance(rect, Rectangle)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_base_create_square(self):
        """Test create method for Square."""
        square_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        square = Base.create(**square_dict)
        self.assertIsInstance(square, Square)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

if __name__ == "__main__":
    unittest.main()

