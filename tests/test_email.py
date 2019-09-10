import pytest

from main import email

some_string = "test"
domain = "test"

def test_email_verify_returns_boolean():
    address = "test"
    assert isinstance(email.verify(address), bool)
    
def test_email_contains_one_atsymbol():
    assert not(email.verify(some_string + "@@" + domain))
    assert not(email.verify(some_string))
    assert email.verify(some_string + "@" + domain)
    
def test_email_contains_string_at_domain():
    assert not(email.verify("@test"))
    assert not(email.verify("test@"))
    assert email.verify("test@test")

def test_email_string_starts_wo_period():
    assert not(email.verify(".a@test"))
    
def test_email_string_ends_wo_period():
    assert not(email.verify("a.@test"))
    
def test_email_string_consecutive_periods():
    assert not(email.verify("a....a@test"))
    assert not(email.verify("a...a@test"))
    assert not(email.verify("a..a@test"))
    assert email.verify("a.a@test")