#!/usr/bin/python3
"""Unittests for FileStorage class."""

import unittest
import os
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
  """Test cases for the FileStorage class."""

  def setUp(self):
    """Set up test environment before each test."""
    self.model = BaseModel()
    self.model.save()

  def tearDown(self):
    """Clean up after each test"""
    try:
      os.remove("file.json")
    except FileNotFoundError:
      pass
  
  def test_all_returns_dict(self):
    """Test that all() returns the storage dictionary."""
    all_objs = storage.all()
    self.assertIsInstance(all_objs, dict)
  
  def test_new_and_save(self):
    """Test that new() adds an object and save() stores it in file.json."""
    key = "BaseModel. " + self.model.id
    storage.reload()
    all_objs = storage.all()
    self.assertIn(key, all_objs)
  
  def test_reload(self):
    """Test that reload() loads objects from file.json."""
    storage.reload()
    key = "BaseModel." + self.model.id
    self.assertIn(key, storage.all())


if __name__ == "__main__":
  unittest.main()