def dpMakeChange(coinValueList,change,minCoins,coinsUsed2):
   for cents in range(change+1):
      # coinCount when initialized basically represents the index,
      # which represents the amount of pennies used to make change.
      coinCount = cents
      newCoin = 1
      # list comprehension limits evaluation of potential coins
      # to those that are actually smaller then are desired amount.
      # e.g. a quarter won't be evaluated as an option for 15-cents of change.
      for j in [c for c in coinValueList if c <= cents]:
            # If we can confirm that the minimum number of coins needed
            # to make change is less then just using pennies, we have a winner.
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed2[cents] = newCoin
   #return minCoins[change]

def printCoins(coinsUsed,change):
   coin = change
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin

if __name__ == '__main__':
    amnt = 8
    clist = [1,5,10,25]
    clist_rev = [25,10,5,1]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for",amnt,"requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)
    print("The count list is as follows:")
    print(coinCount)

    print("in reverse")

    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)
    print("Making change for",amnt,"requires")
    print(dpMakeChange(clist_rev,amnt,coinCount,coinsUsed),"coins")
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)
    print("The count list is as follows:")
    print(coinCount)
