# Imported Files/functions
import art

# Auction Code
logo = art.logo
print(logo)
#auction dictionary
auction_dictionary = {}

end_auction = False
# User input
while end_auction is False:
    user_name = input("What is your name? ")
    user_bid = input("What is your bid price? ")

    auction_dictionary[user_name] = user_bid #adding to the dictionary

    max_value = max(auction_dictionary, key=auction_dictionary.get)
    highest_bid = auction_dictionary[max_value]
    continue_loop = input("Are there other users that want to bid? Type 'yes' or 'no'")
    if continue_loop.lower() == "yes":
        end_auction = False
    else:
        end_auction = True
        print(f'The winner is {max_value} with a bid of {highest_bid}')



