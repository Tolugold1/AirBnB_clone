#!/usr/bin/python3
"""Unittest for BaseModal class"""
import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for class BaseModel"""
    def test_attribute(self):
        """test if a class has Id, created_at and updated_at"""
        sample = BaseModel()
        sample.name = "My_First_Model"
        sample.age = 22
        self.assertTrue(hasattr(sample, "name"))
        self.assertTrue(hasattr(sample, "age"))
        self.assertTrue(hasattr(sample, "id"))
        self.assertTrue(hasattr(sample, "created_at"))
        self.assertTrue(hasattr(sample, "updated_at"))


if __name__ == "__main__":
    unittest.main()
