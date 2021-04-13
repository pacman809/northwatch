import json
from web3 import Web3
from datetime import datetime


def timestamp(stamp):
    time = stamp
    dt = datetime.fromtimestamp(time // 1000000000)
    return dt.strftime('%Y-%m-%d %H:%M:%S')


def powerball():
    address = "0x1c52caf9d3223da181dd7970f74f6bddebc06ac2"  # POWERBALL CONTRACT
    abi = json.loads(
        '[{"constant":false,"inputs":[{"name":"numbers","type":"uint256[6][]"}],"name":"buy","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"name":"_round","type":"uint256"}],"name":"claim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"close","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_round","type":"uint256"}],"name":"drawNumbers","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"constant":true,"inputs":[],"name":"jackpot","outputs":[{"name":"jackpot","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MAX_NUMBER","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MAX_POWERBALL_NUMBER","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"nowtime","outputs":[{"name":"nowtime","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"rakeamount","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"round","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"ROUND_LENGTH","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"rounds","outputs":[{"name":"endTime","type":"uint256"},{"name":"drawBlock","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"TICKET_PRICE","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_round","type":"uint256"},{"name":"user","type":"address"}],"name":"ticketsFor","outputs":[{"name":"tickets","type":"uint256[6][]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"ts","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_round","type":"uint256"}],"name":"winningNumbersFor","outputs":[{"name":"winningNumbers","type":"uint256[6]"}],"payable":false,"stateMutability":"view","type":"function"}]')
    geth_url = "http://192.168.1.231:8545"
    web3 = Web3(Web3.HTTPProvider(geth_url))
    address = Web3.toChecksumAddress(address)
    contract_balance = int(web3.eth.getBalance(address))
    contract_balance = web3.fromWei(contract_balance, 'Ether')

    contract = web3.eth.contract(address=address, abi=abi)
    Max_Number = contract.functions.MAX_NUMBER().call()
    Max_Powerball_Number = contract.functions.MAX_POWERBALL_NUMBER().call()
    Round = contract.functions.round().call()
    Length = contract.functions.ROUND_LENGTH().call()
    Ticket_Price = contract.functions.TICKET_PRICE().call()
    rounds = contract.functions.rounds(int(Round)).call()
    winningNumbers = contract.functions.winningNumbersFor(Round).call()
    realTime = timestamp(rounds[0])

    # print(Max_Number)
    # print(Max_Powerball_Number)
    # print(Round)
    # print(Length)
    # print(Web3.fromWei(Ticket_Price, 'Ether'))
    # print(rounds)

    result = {
        "Max_Number": Max_Number,
        "Max_Powerball_Number": Max_Powerball_Number,
        "Current_Round": Round,
        "Round_Length": Length,
        "Ticket_Price": Web3.fromWei(Ticket_Price, 'Ether'),
        "rounds": rounds,
        "address": address,
        "winningNumbers": winningNumbers,
        "balance_of_contract": contract_balance,
        "time": realTime
    }

    return result
