"""
Day 9 - Python Dictionaries and Nesting

Dictionaries
 - {Key: Value}
 - Reference items by key, e.g. dict["key"]
 - Add items by key, e.g. dict["key"] = number
 - Loop through a dictionary by key, e.g. for key in dictionary:

Nesting
 - You can nest different data structures within other data structures and even mix types, e.g {"key": number, number: [list]}

"""

# Blind Auction Program
# Allow bidders to type a name and a bid and then return the person who had the highest bid
# Clear the screen before the next bid happens

still_bidding = True
bid_max = {
    "name": "Hello",
    "bid": -1
}
while still_bidding:
    person = input("Please enter your name: ")
    bid = int(input("Please enter your bid: "))
    if bid > bid_max["bid"]:
        bid_max["name"] = person
        bid_max["bid"] = bid
    add_bidder = input("Would you like to add another bidder? (y/n): ")
    if add_bidder == "n":
        still_bidding = False

print(f"The winner of the auction is {bid_max['name']} with a bid of {bid_max['bid']}")