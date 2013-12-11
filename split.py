# Script to distribute bitcoin balance of coinbase.com account amongst users

# requires:
# pip install coinbase

from coinbase import CoinbaseAccount

# Create file info.py containing the following variables:
from info import API_KEY, USERS

"""
# Example USERS list
USERS = [
    {
        'name'    : 'User 1',
        'weight'  : 0.5,
        'address' : 'abcdefg',
    },
    {
        'name'    : 'User 2',
        'weight'  : 0.5,
        'address' : 'hijklmn',
    },
]
"""


def validate_address(addr):
    # TODO: validate bitcoin addresses
    return True


def validate_users(users):
    if users == None:
        print "Missing list of users"
        return False

    total_weight = 0
    for user in users:
        weight = user["weight"]
        if weight < 0 or weight > 1:
            print "User", user["name"], "has invalid weight"
            return False

        total_weight += weight
        if not validate_address(user["address"]):
            print "User", user["name"], "has invalid address"
            return False

    if total_weight != 1:
        print "Error: Weights do not sum to 1"
        return False

    print str(len(users)), "total users found"

    return True


def send_bitcoin(account, to, amount, note):
    try:
        tx = account.send(to_address=to, amount=amount, notes=note)
        print "\tSuccessfully sent", str(tx.amount), tx.amount.currency, \
              "to", tx.recipient_address, "\n"
    except:
        print "\tError sending", str(amount), "to", to, "\n"
    
    
def main():
    if not validate_users(USERS):
        return 
    
    account = CoinbaseAccount(api_key=API_KEY)
    bal = account.balance
    print "coinbase balance:", str(bal), "BTC\n"

    if bal <= 0:
        print "Insufficient funds to split"
        return

    total = 0
    print "Splitting payment..."
    for user in USERS:
        split = user["weight"] * bal
        total += split
        print "\t", user["name"], str(user["weight"]), str(split), "BTC"
        send_bitcoin(account, user["address"], split, "bitcoinparty")
    
    print "split total:", str(total)
    print "coinbase balance:", str(account.balance), "BTC"
    
    
if __name__ == "__main__":
    main()
    
