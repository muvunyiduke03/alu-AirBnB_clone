#!/usr/bin/python3
"""Unittests for the BaseModel class"""


import unittest
import os
import models
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
  """Test cases for the BaseModel class."""

  def setUp(self):
    """Set up test environment before each test."""
    self.model = BaseModel()

  def tearDown(self):
    """Clean up after each test."""
    try:
      os.remove("file.json")
    except FileNotFoundError:
      pass

  def test_instance_creation(self):
    """Test if a new instance is created properly."""
    self.assertIsInstance(self.model, BaseModel)
    self.assertTrue(hasattr(self.model, "id"))
    self.assertTrue(hasattr(self.model, "created_at"))
    self.assertTrue(hasattr(self.model, "updated_at"))

  def test_save_method(self):
    """Test that save updates 'updated_at' attribute"""
    old_updated_at = self.model.updated_at
    self.model.save()
    self.assertNotEqual(old_updated_at, self.model.updated_at)

  def test_to_dict_method(self):
    """Test conversion of instance to dictionary."""
    model_dict = self.model.to_dict()
    self.assertIsInstance(model_dict, dict)
    self.assertEqual(model_dict["__class__"], "BaseModel")
    self.assertEqual(model_dict["id"], self.model.id)
    self.assertIsInstance(model_dict["created_at"], str)

  
  def test_str_representation(self):
    """Test __str__ representation of BaseModel."""
    self.assertIn(self.model.id, str(self.model))
    self.assertIn("BaseModel", str(self.model))

if __name__ == "__main__":
  unittest.main()
