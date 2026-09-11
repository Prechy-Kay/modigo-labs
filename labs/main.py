def format_line_item(description, amount, tax_rate=7.5, currency="$"):
    taxed_total = round (amount + (amount * tax_rate / 100), 2)
    return (f"{description}: {currency}{taxed_total}")
    # TODO: calculate the taxed total using tax_rate, round to 2 decimal places,
    # and return "{description}: {currency}{total}"

format_line_item("Notebook", 10)