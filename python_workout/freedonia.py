from decimal import Decimal

RATES = {
    'Chico': Decimal(0.5),
    'Groucho': Decimal(0.7),
    'Harpo': Decimal(0.5),
    'Zeppo': Decimal(0.4)
}
def HourTooLowError(Exception): pass
def HourTooHighError(Exception): pass


def calculate_tax(amount: int, province, hour: int):
    """Calculates final price adding tax according to province and hour the sale is made
    Example input:
        calculate_tax(500, 'Harpo', 12)
    Example output:
        625
    Args:
        amount (int): the amount of the purchase
        province (str): Chico|Groucho|Harpo|Zeppo
        hour (int): integer from 0-24 representing the hour
    Returns:
        int: the final price (amount + tax)
    """
    # Error checking
    if hour < 0:
        raise HourTooLowError(f'Hour of {hour} is < 0')

    if hour >= 24:
        raise HourTooHighError(f'Hour of {hour} is >= 24')

    if hour == 0:
        tax = 0
    elif hour >= 12 and hour <= 13:
        tax = amount * (RATES.get(province, 0) * Decimal(0.5))
    elif hour >= 23 and hour < 24:
        tax = amount * (RATES.get(province, 0) * Decimal(0.958))
    else:
        tax = amount * (RATES.get(province, 0))
    return amount + tax
