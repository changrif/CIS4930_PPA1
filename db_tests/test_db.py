import pytest
from unittest import TestCase
import mock
import mongomock
import datetime

class Email:
  def __init__(self, email, validated, timestamp):
    self.email = email
    self.validated = validated
    self.timestamp = timestamp

  def pop(self, v1, v2):
    pass

class Bmi:
  def __init__(self, feet, inches, weight, bmi, category, timestamp):
    self.weight = weight
    self.inches = inches
    self.weight = weight
    self.bmi = bmi
    self.category = category
    self.timestamp = timestamp

  def pop(self, v1, v2):
    pass

class ObjArrayStub:
  def __init__(self, obj):
    self.obj = obj
    self.length = len(obj)

  def count(self):
    return self.length
  
  def find(self):
    return self.obj
  
  def insert_one(self, data):
    pass

class Pymongo_db:
  def __init__(self, bmis, emails):
    self.bmis = ObjArrayStub(bmis)
    self.emails = ObjArrayStub(emails)

class Stub:
  def __init__(self, pymongo_db):
    self.pymongo_db = pymongo_db
    
stub_emails = [ Email("chandler@gmail.com", True, "getTime()"), Email("chandler@gmail", False, "getTime()") ]
stub_bmi = [ Bmi(5, 10, 150, "bmiNum", "category", "") ]
    
@mock.patch('pymongo.MongoClient')
def test_connection(mock_pymongo):
    mock_db = Pymongo_db(stub_bmi, stub_emails)
    stub = Stub(mock_db)
    mock_pymongo.return_value = stub
    from main import db
    assert str(mock_pymongo.call_args) == "call('mongodb://localhost:27017/')"
    assert mock_pymongo.pymongo_db.assert_called_once

@mock.patch('pymongo.MongoClient')
def test_getBMI(mock_pymongo):
    mock_db = Pymongo_db(stub_bmi, stub_emails)
    stub = Stub(mock_db)
    mock_pymongo.return_value = stub
    from main import db
    result = db.getBMI()
    assert result == stub_bmi
    
@mock.patch('pymongo.MongoClient')
def test_getEmails(mock_pymongo):
    mock_db = Pymongo_db(stub_bmi, stub_emails)
    stub = Stub(mock_db)
    mock_pymongo.return_value = stub
    from main import db
    result = db.getEmails()
    assert result == stub_emails

@mock.patch('pymongo.MongoClient')
def test_saveBMI(mock_pymongo):
    mock_db = Pymongo_db(stub_bmi, stub_emails)
    stub = Stub(mock_db)
    mock_pymongo.return_value = stub
    from main import db
    db.getTime = mock.MagicMock()
    db.getTime.return_value = "0000-00-00 00:00:00AM"
    result = db.saveBMI(5, 10, 150, "category", "bmiNum")
    assert mock_pymongo.pymongo_db.bmis.insert_one.assert_called_once
    assert result == {"bmi": "bmiNum", "category": "category", "feet": 5, "inches": 10, "weight": 150, "timestamp": "0000-00-00 00:00:00AM" }
    
@mock.patch('pymongo.MongoClient')
def test_saveEmail(mock_pymongo):
    mock_db = Pymongo_db(stub_bmi, stub_emails)
    stub = Stub(mock_db)
    mock_pymongo.return_value = stub
    from main import db
    db.getTime = mock.MagicMock()
    db.getTime.return_value = "0000-00-00 00:00:00AM"
    result = db.saveEmail(False, "email")
    assert mock_pymongo.pymongo_db.emails.insert_one.assert_called_once
    assert result == {"email": "email", "validated": False, "timestamp": "0000-00-00 00:00:00AM" }
    