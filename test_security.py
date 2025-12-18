import unittest
from security import validar_password

class TestPasswordValidator(unittest.TestCase):

  def test_password_corta(self):
    self.assertFalse(validar_password("1234"))

  def test_password_llarga(self):
    self.assertTrue(validar_password("123456789"))

if __name__ == "__main__":
  unittest.main()
