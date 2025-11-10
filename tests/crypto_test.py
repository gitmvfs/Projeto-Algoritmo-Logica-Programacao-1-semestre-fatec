import pytest
from controller.criptografia import generate_hash, check_hash

def test_encrypt_decrypt():
    word = "senha_teste"
    h = generate_hash(word)
    assert isinstance(h, bytes)
    assert check_hash(h, word) is True
    assert check_hash(h, "outra_senha") is False
