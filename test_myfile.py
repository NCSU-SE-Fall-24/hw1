from myfile import calculate_tax

def test_passing():
    result = calculate_tax(100, 7.25)
    assert result == 107.25  

def test_failing_invalid_amount():
    calculate_tax(-100, 7.25)  
