from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

def bidder(biding_record):
  highest_bid=0
  winner=""
  for bidder in biding_record:
    bid_amount=biding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid=bid_amount
      winner=bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

loop=False
dicti={}
while not loop:
  name=input("Enter your name:")
  bid = int(input("Enter the bid amount:$"))
  dicti[name]=bid
  continue_next=input("Is there another person to bid? (yes/no)").lower()
  if continue_next=="no":
    loop=True
    bidder(dicti)
  elif continue_next=="yes":
    clear()
