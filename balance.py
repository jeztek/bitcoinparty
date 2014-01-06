from coinbase import CoinbaseAccount

from info import API_KEY

def main():
    account = CoinbaseAccount(api_key=API_KEY)
    print "coinbase balance:", str(account.balance), "BTC"
    
    
if __name__ == "__main__":
    main()
    
