import pytest

from controller.user_controller import register, login, database
from controller.criptografia import check_hash

def setup_function():
    # Clear database before each test
    database.clear()

def test_register_new_user():
    assert register("User Test", "test@example.com", "123") is True
    assert "test@example.com" in database
    assert check_hash(database["test@example.com"]["password"], "123") is True

def test_login_existing_user():
    register("User Test", "test@example.com", "123")
    assert login("test@example.com", "123") is True

def test_login_nonexistent_user():
    assert login("naoexiste@example.com", "123") is False

def test_register_existing_user_raises():
    register("User Test", "test@example.com", "123")
    with pytest.raises(Exception):
        register("Outro", "test@example.com", "456")
