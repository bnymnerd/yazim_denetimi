import pytest
from yazim_denetimi import check_spelling

# Test: Yazım hatalarını tespit etme
def test_check_spelling():
    text = "Hello, what is your namew?"
    corrected = check_spelling(text)
    assert corrected == "Hello, what is your name?"  # Doğru yazım önerisi 'Hello'

def test_no_spelling_error():
    text = "Hello, correct."
    corrected = check_spelling(text)
    assert corrected == text  # Hata yoksa, metin aynen kalmalı



