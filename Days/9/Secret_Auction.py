from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secret auction program.")

bidder_log = {
	"name": [],
	"bid": []
}

program_running = True

while program_running:
	bidder_name = input("What is your name?: ").lower()
	bid = int(input("What's your bid?: $"))
	other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
	clear()

	bidder_log['name'].append(bidder_name)
	bidder_log['bid'].append(bid)

	if other_bidders == 'no':
		program_running = False


bids = bidder_log['bid']

# Initialize
largest_bid = bids[0]
largest_bid_index = 0

if len(bids) > 1:
	for i in range(1, len(bids)):
		if bids[i] > largest_bid:
			largest_bid = bids[i]
			largest_bid_index = i

print(f"The winner is {bidder_log['name'][largest_bid_index]} with a bid of ${largest_bid}")

