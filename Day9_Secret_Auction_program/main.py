print("Welcome to Secret Auction Program!")

bid_details = {}
bid_end = False

def winner_cal(dict):
    highest_bid = 0.00
    current_bid = 0.00
    for keys in dict:
        current_bid = dict[keys]
        if current_bid > highest_bid:
            highest_bid = current_bid
            winner = keys
    print(f"The winner of the bid is {winner} with bid ${highest_bid}")

while not bid_end:
    user_name = input("What is your name? :")
    bid_amount = float(input("What is your bid? : $"))
    bid_end = input("Are there more bidders? Type 'Yes' or 'No' :")
    bid_details[user_name] = bid_amount

    if bid_end.lower() == 'no':
        bid_end = True
        winner_cal(bid_details)
    else:
        bid_end = False