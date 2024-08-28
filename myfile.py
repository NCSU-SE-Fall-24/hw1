def calculate_tax(amount, tax_rate):
    """
    calculate_tax function calculates the tax

    :param amount: enter the positive float value great than 0
    :param tax_rate: pass the tax rate in the percentage
    :return: it returns the total amount including the tax 
    """
    try: 
        if amount < 0:
            raise ValueError("Invalid amount: Not allowed to enter less than 0")
        elif tax_rate < 0:
            raise ValueError("Invalid tax rate: Not allowed to enter less than 0%")
        else:
            tax = amount * (tax_rate / 100)
            total_amount = amount + tax
            print(f"Total amount after adding {tax_rate}% tax: {total_amount}")
            return total_amount
    except ValueError as e:
        raise e
    except Exception as e:
        raise e