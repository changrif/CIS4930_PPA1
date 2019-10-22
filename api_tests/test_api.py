import pytest
from unittest import TestCase
import mock
from api import api

import requests
import threading

t1 = threading.Thread(target=api.run)
t1.daemon = True
t1.start()

mock_bmi = {
    "feet": 5, 
    "inches": 10, 
    "weight": 150, 
    "category": "Normal weight", 
    "bmi": 21.6, 
    "timestamp": '0000-00-00 00:00:00AM'
}

mock_email = {
    "email": "hello", 
    "validated": False, 
    "timestamp": '0000-00-00 00:00:00AM'
}

# *******************************************
# *** REAL REQUESTS - functionality tests ***
# *******************************************
@mock.patch('main.db.getBMI')
def test_bmi_emptyRequest(mock_bmi):
    mock_bmi.return_value = []
    response = requests.get('http://localhost:5000/bmi')
    assert response.ok

@mock.patch('main.db.saveBMI')
@mock.patch('main.bmi.calculate')
def test_bmi_request(mock_calculate, mock_save):
    mock_calculate.return_value = (mock_bmi["category"], mock_bmi["bmi"])
    mock_save.return_value = mock_bmi
    
    response = requests.get('http://localhost:5000/bmi?feet=5&inches=10&weight=150')
    
    assert response.ok
    assert response.json() == mock_bmi
    
def test_bmi_badRequest():
    response = requests.get('http://localhost:5000/bmi?feet=nope&inches=10&weight=150')
    assert response.status_code == 400
   
@mock.patch('main.db.getEmails')
def test_email_emptyRequest(mock_email):
    mock_email.return_value = []
    response = requests.get('http://localhost:5000/email')
    assert response.ok

@mock.patch('main.db.saveEmail')
@mock.patch('main.email.verify')
def test_email_request(mock_verify, mock_save):
    mock_verify.return_value = mock_email["validated"]
    mock_save.return_value = mock_email
    
    response = requests.get('http://localhost:5000/email?address=hello')
    
    assert response.ok
    assert response.json() == mock_email
   
def test_email_badRequest():
    response = requests.get('http://localhost:5000/email?addres=test@gmail.com')
    assert response.status_code == 400
    
def test_badRoute():
    response = requests.get('http://localhost:5000/error')
    assert response.status_code == 404

# **********************      
# *** MOCKED METHODS ***
# **********************
@mock.patch('requests.get')
def test_bmi_mockEmptyRequest(mock_get):
    mock_get.return_value.ok = True
    mock_get.return_value.json = []
    response = requests.get('localhost:5000/bmi')
    assert response.json == []
    assert response.ok

@mock.patch('requests.get')
def test_bmi_mockRequest(mock_get):
    mock_get.return_value.ok = True
    mock_get.return_value.json = mock_bmi
    response = requests.get('localhost:5000/bmi?feet=5&inches=10&weight=150')
    assert response.json == mock_bmi
    assert response.ok
    
@mock.patch('requests.get')
def test_bmi_mockBadRequest(mock_get):
    mock_get.return_value.status_code = 400
    response = requests.get('localhost:5000/bmi?feet=hello&inches=10&weight=150')
    assert not (response == None)
    assert response.status_code == 400

@mock.patch('requests.get')
def test_email_mockEmptyRequest(mock_get):
    mock_get.return_value.ok = True
    mock_get.return_value.json = []
    response = requests.get('localhost:5000/email')
    assert response.json == []
    assert response.ok
    
@mock.patch('requests.get')
def test_email_mockRequest(mock_get):
    mock_get.return_value.ok = True
    mock_get.return_value.json = mock_email
    response = requests.get('localhost:5000/email?address=test@gmail.com')
    assert response.json == mock_email
    assert response.ok
    
@mock.patch('requests.get')
def test_email_mockBadRequest(mock_get):
    mock_get.return_value.status_code = 400
    response = requests.get('localhost:5000/email?addrss=test@gmail.com')
    assert not (response == None)
    assert response.status_code == 400
    
@mock.patch('requests.get')
def test_badRoute(mock_get):
    mock_get.return_value.status_code = 404
    response = requests.get('http://localhost:5000/error')
    assert response.status_code == 404