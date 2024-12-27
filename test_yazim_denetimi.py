import pytest
from yazim_denetimi import check_spelling

# Test: Yazım hatalarını tespit etme
def test_check_spelling():
    text = "Helo, bu bir test metnidir."
    corrected = check_spelling(text)
    assert corrected == "Hello, bu bir test metnidir."  # Doğru yazım önerisi 'Hello'

def test_no_spelling_error():
    text = "Merhaba, bu bir doğru yazım."
    corrected = check_spelling(text)
    assert corrected == text  # Hata yoksa, metin aynen kalmalı
