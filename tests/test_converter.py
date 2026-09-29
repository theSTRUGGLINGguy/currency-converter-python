from converter import convert_currency


def test_usd_to_inr():

    result = convert_currency(100, "USD", "INR")

    assert result == 9599.433


def test_inr_to_usd():

    result = convert_currency(9599.433, "INR", "USD")

    assert round(result, 2) == 100.00


def test_same_currency():

    result = convert_currency(500, "USD", "USD")

    assert result == 500


def test_invalid_currency():

    result = convert_currency(100, "ABC", "USD")

    assert result is None