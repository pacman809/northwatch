from web3 import Web3
import pymongo
global starttime
from data import database, connect_geth

def dailyTransactions():
        global starttime
        
        web3 = connect_geth()

        
        myCol           =       database()["blocks"]
        myCol2          =       database()["transactions"]
        count = 0


        latest_block = web3.eth.blockNumber - 1

        for x in myCol.find({"number": latest_block}):
                basetime = x["timestamp"] 
                starttime = basetime - 86400000000000
        try:        
                for x in myCol2.find( { "block_timestamp": { "$gt": starttime } } ):
                        if x["to_address"] != "0x0000000000000000000000000000000000000000":
                                count = count + 1
                

                return count

        except:
                count = 0
                return count
a = dailyTransactions()
print(a)

