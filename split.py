# Script to distribute bitcoin balance of coinbase.com account amongst users

# requires:
# pip install coinbase

from hashlib import sha256
from coinbase import CoinbaseAccount
import oauth2client

from info import API_KEY, USERS
 
DIGITS58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def validate_address(addr):
    return True


def validate_users(users):
    total_weight = 0
    
    for user in users:
        total_weight += user["weight"]
        if not validate_address(user["address"]):
            print "User", user["name"], "has invalid address"
            return False

    if total_weight != 1:
        print "Error: Weights do not sum to 1"
        return False

    print str(len(users)), "total users found"

    return True


def send_bitcoin(account, to, amount, note):
    tx = account.send(to_address=to, amount=amount, notes=note)

    print "Successfully sent", str(tx.amount), tx.amount.currency, "to", \
          tx.recipient_address

    
def main():
    if not validate_users(USERS):
        return 
    
    account = CoinbaseAccount(api_key=API_KEY)
    print "balance:", str(account.balance)

    if account.balance > 1.0:
        print "Splitting payment"
        for user in USERS:
            print user["name"], user["weight"]
	    # send_bitcoin(account, user["address"], user["weight"], "")
    
    print "balance:", str(account.balance)
    
    
if __name__ == "__main__":
    main()
    
