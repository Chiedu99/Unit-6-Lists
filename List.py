#Chiedu Nduka-Eze last updated monday, October 17
#This program creates a list of all the prime numbers between 2 and a chosen max number

def promptUser():
    return int(input("What is your max number?:"))


def makeList(max):
    """This function creates the master list with all the numbers"""
    masterList = []
    for x in range(2, max):
        masterList.append(x)
    return masterList


def primeList(masterList):
    """This function puts all the prime numbers in the prime number list"""
    primeList = []
    while len(masterList) > 0:
        nextPrime = (masterList[0])
        primeList.append(nextPrime)
        for x in masterList:
            if x % nextPrime == 0:
                masterList.remove(x)
    print("aye bruh, your primes are:", primeList)


def main():
    max = promptUser()
    masterList = makeList(max)
    primeList(masterList)

main()
