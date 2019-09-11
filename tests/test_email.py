import pytest

from main import email

some_string = "test"
domain = "test.com"

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
    assert email.verify("test@" + domain)

def test_email_string_starts_wo_period():
    assert not(email.verify(".a@" + domain))
    
def test_email_string_ends_wo_period():
    assert not(email.verify("a.@" + domain))
    
def test_email_string_consecutive_periods():
    assert not(email.verify("a....a@" + domain))
    assert not(email.verify("a...a@" + domain))
    assert not(email.verify("a..a@" + domain))
    assert email.verify("a.a@" + domain)
    
def test_email_cannot_start_nonnumeric():
    assert not(email.verify("0" + some_string + "@" + domain))
    assert email.verify(some_string + "@" + domain)
    
def test_email_can_contain_exclamationpoint():
    assert email.verify(some_string + "!" + "@" + domain)

def test_email_can_contain_dollarsign():
    assert email.verify(some_string + "$" + "@" + domain)
    
def test_email_can_contain_percentsign():
    assert email.verify(some_string + "%" + "@" + domain)
    
def test_email_can_contain_asterisk():
    assert email.verify(some_string + "*" + "@" + domain)
    
def test_email_can_contain_plus():
    assert email.verify(some_string + "+" + "@" + domain)
    
def test_email_can_contain_minus():
    assert email.verify(some_string + "-" + "@" + domain)
    
def test_email_can_contain_equals():
    assert email.verify(some_string + "=" + "@" + domain)
    
def test_email_can_contain_carrot():
    assert email.verify(some_string + "^" + "@" + domain)
    
def test_email_can_contain_underscorek():
    assert email.verify(some_string + "_" + "@" + domain)
    
def test_email_can_contain_leftbracket():
    assert email.verify(some_string + "{" + "@" + domain)
    
def test_email_can_contain_pipe():
    assert email.verify(some_string + "|" + "@" + domain)
    
def test_email_can_contain_rightbracket():
    assert email.verify(some_string + "}" + "@" + domain)
    
def test_email_can_contain_questionmark():
    assert email.verify(some_string + "?" + "@" + domain)
    
def test_email_cannot_contain_doublequote():
    assert not(email.verify(some_string + "\"" + "@" + domain))
    
def test_email_cannot_contain_left_parenthesis():
    assert not(email.verify(some_string + "(" + "@" + domain))
    
def test_email_cannot_contain_right_parenthesis():
    assert not(email.verify(some_string + ")" + "@" + domain))
    
def test_email_cannot_contain_comma():
    assert not(email.verify(some_string + "," + "@" + domain))
    
def test_email_cannot_contain_colon():
    assert not(email.verify(some_string + ":" + "@" + domain))
    
def test_email_cannot_contain_semicolon():
    assert not(email.verify(some_string + ";" + "@" + domain))
    
def test_email_cannot_contain_left_carrot():
    assert not(email.verify(some_string + "<" + "@" + domain))
    
def test_email_cannot_contain_right_carrot():
    assert not(email.verify(some_string + ">" + "@" + domain))
    
def test_email_cannot_contain_atsymbol():
    assert not(email.verify(some_string + "@" + "@" + domain))
    
def test_email_cannot_contain_left_bracket():
    assert not(email.verify(some_string + "[" + "@" + domain))
    
def test_email_cannot_contain_backslash():
    assert not(email.verify(some_string + "\\" + "@" + domain))
    
def test_email_cannot_contain_right_bracket():
    assert not(email.verify(some_string + "]" + "@" + domain))
    
def test_email_cannot_contain_singlequote():
    assert not(email.verify(some_string + "'" + "@" + domain))
    
def test_email_domain_cannot_contain_doublehypen():
    assert not(email.verify(some_string + "@" + "--" + domain))
    
def test_email_domain_must_have_period():
    assert not(email.verify(some_string + "@test"))