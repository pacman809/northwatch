from web3 import Web3
from search import connect_geth
import pymongo
global starttime


def dailyTransactions():
        global starttime
        
        web3 = connect_geth()

        db              =       "halo-explorer-mainnet" # CONSOLIDATE THIS TO NEW FILE
        myclient        =       pymongo.MongoClient("mongodb://localhost:27017/")
        mydb            =       myclient[db]
        myCol           =       mydb["blocks"]
        myCol2          =       mydb["transactions"]
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

