from myfile import calculate_tax

def test_passing():
    result = calculate_tax(100, 7.25)
    assert result == 107.25  


def test_failing():
    try:
        # This raises a ValueError
        calculate_tax(-100, 7.25)  
    except ValueError as e:
        assert str(e) == "Invalid Amount: Not allowed to enter less than 0"
    else:
        assert False, "ValueError was not raised for a negative amount"