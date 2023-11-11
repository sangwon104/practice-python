# variable
won = 10000;
PI = 3.14;
Ticker = "BTC";

print(type(won));
print(type(PI));
print(type(Ticker));

# condition
BTC  = 3200
BTC = BTC * 1.05 # 5% 수익

if BTC > 4500 :
    print("wow!!!")
elif BTC > 3000 and BTC < 3500 :
    print("huuuu")
else :
    print("no!!!")

# data structure
## list
coins = ['BTC', 'XRP', 'DOGE', 'ETH']
for coin in coins :
    print(coin)
coins.append('BTH')
print(coins[-1])

## tuple
coins = {'BTC', 'XRP', 'DOGE', 'ETH'}
# coins.append('BTH') # 수정할 수 없다!

## dictionary
coins = {"BTC":4000, "ETH": 1000, "DOGE":400}
print(coins["BTC"])
coins = {"BITCOIN":4000, "ALTCOIN" : {"ETH": 1000, "DOGE":400}}
print(coins["ALTCOIN"]["ETH"])

## Pandas Dataframe

## loop
BTC = 3500

while BTC < 4000 :
    BTC += 200
    print("BTC : ", BTC)

print("wow!!")

coins = ['BTC', 'XRP', 'DOGE', 'ETH']

for i in range(0, 3) :
    coins[i]

coins = {"BITCOIN":4000, "ALTCOIN" : {"ETH": 1000, "DOGE":400}}
for coin in coins :
    print(coin, coins[coin])    

# function
def sum (num1, num2) :
    return num1 + num2

print(sum(1, 2))

def GetCoinPrice(coinName) :
    coins = {"BTC":4000, "ETH": 1000, "DOGE":400}
    for coin in coins :
        if coin == coinName :
            return coins[coinName]
    return "NODATA"

print(GetCoinPrice("BTC"))
print(GetCoinPrice("TEST"))