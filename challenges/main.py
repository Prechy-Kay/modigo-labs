# No starter code provided — write the full function yourself.
# Function name: split_bill
# Parameters: bill_amount, tip_percent, people
# Must return: each person's share, rounded to 2 decimal places


def split_bill(bill_amount, tip_percent, people):
    tip_amount = bill_amount * (tip_percent / 100)
    grand_total = bill_amount + tip_amount
    each_person_share = round((grand_total / people), 2)
    return each_person_share




split_bill(100, 10, 2)
split_bill(60, 20, 3)
split_bill(50, 0, 1)