from drivers.add import add

def test_add_positive_numbers():
    """Test addition of two positive numbers."""
    result = add(2, 3)
    assert result == 5, f"Expected 5 but got {result}"

def test_add_negative_numbers():
    """Test addition of two negative numbers."""
    result = add(-2, -3)
    assert result == -5, f"Expected -5 but got {result}"


