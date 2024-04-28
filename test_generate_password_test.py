import unittest
from main.py import generate_password, get_password_length

class TestGeneratePassword(unittest.TestCase):
    def test_generate_password_length(self):
        length = 10
        password = generate_password(length)
        self.assertEqual(len(password), length)

    def test_generate_password_characters(self):
        password = generate_password(10)
        characters = string.ascii_letters + string.digits + string.punctuation
        self.assertTrue(all(char in characters for char in password))

class TestGetPasswordLength(unittest.TestCase):
    def test_get_password_length_positive_integer(self):
        
        with unittest.mock.patch('builtins.input', return_value='10'):
            self.assertEqual(get_password_length(), 10)

    def test_get_password_length_invalid_input_then_valid(self):
        
        with unittest.mock.patch('builtins.input', side_effect=['abc', '10']):
            self.assertEqual(get_password_length(), 10)

if __name__ == "__main__":
    unittest.main()
