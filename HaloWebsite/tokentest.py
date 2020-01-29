import json
from web3 import Web3
import requests
import data



def balanceInfo(personal_address):
    results = {}
    contract_address =  ["0xd314d564c36c1b9fbbf6b440122f84da9a551029", "0xc8481effc60fa765ccf8286ba346233ed113b024","0x59195ebd987bde65258547041e1baed5fbd18e8b","0xb8648f065205b9c31055653d668723f4b840e4c0","0x14d01e64f0573925e28d69dc3846b2f0986ab8b8","0x280750ccb7554faec2079e8d8719515d6decdc84","0x0792fe820e7f65da788ac002ce88c74816b59142","0xdc14c317abf4fca7ac2255f0da73b39f63598c76","0x0343350a2b298370381cac03fe3c525c28600b21","0xb70b02222c53abf4e9ccac8fb701425db2ec4de1","0x200941b46e8cbb645fe85cdd526e48826acfd8fa","0x72649f2a739f2ed7454ca146fb9ba589747287f2", "0xc43a6a22d3a430f175a994683005572cdb18f47c"]
    abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]')
    web3 = Web3(Web3.HTTPProvider(data.Gethurl))
    account_checksum = Web3.toChecksumAddress(personal_address)
    balance = web3.eth.getBalance(account_checksum)
    halo3 = web3.fromWei(balance, "ether")
    
    
    results.update( {"HALO": halo3} )

    for i in contract_address:
        address = Web3.toChecksumAddress(i)
        contract = web3.eth.contract(address=address, abi=abi)
        symbol = contract.functions.symbol().call()
        balance = contract.functions.balanceOf(account_checksum).call()
        

        if symbol == "BTC" or "FCT" and balance != 0 :
            balance = balance * 100000000000
            balance = '{0:.20f}'.format(balance).rstrip('0').rstrip('.')
            results.update( {symbol : balance} )
        
        if balance != 0:
            results.update( {symbol : balance} )

    return results
