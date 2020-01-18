
from web3 import Web3
from search import connect_geth
import json
import requests 
from datetime import datetime



def solvency():

	try:

		web3 = connect_geth()
		abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]')
		address = Web3.toChecksumAddress(0xd314d564c36c1b9fbbf6b440122f84da9a551029)
		contract = web3.eth.contract(address=address, abi=abi)
		total_supply = contract.functions.totalSupply().call()
		total_supply = Web3.fromWei(total_supply,"Ether")       
		total_supply = '%.18f' % total_supply           
		api_url = requests.get("https://api.blockcypher.com/v1/eth/main/addrs/0x70a41917365e772e41d404b3f7870ca8919b4fbe/balance")
		api_url2 = requests.get("https://api.coinmarketcap.com/v1/ticker/ethereum/?convert=USD")
		data_results = api_url.json()
		data_results2 = api_url2.json()
		price_usd = float(data_results2[0]["price_usd"])
		ETH = data_results['final_balance']
		ETH = Web3.fromWei(ETH, 'Ether')
		a = float(total_supply)
		b = float(ETH)
		difference = float(a-b)
		date = datetime.now()
		shortfall = price_usd * difference
		shortfall = '{0:.2f}'.format(shortfall)
		shortfall = price_usd * difference


		solve = {

		"date"			: date,
		"dex"			: total_supply,
		"eth"			: ETH,
		"difference"	: difference,
		"price"			: price_usd,
		"shortfall"		: shortfall
		}


		return solve

	except:

		solve = {

		"date"			: "No Connection",
		"dex"			: "No Connection",
		"eth"			: "No Connection",
		"difference"	: "No Connection",
		"price"			: "No Connection",
		"shortfall"		: "No Connection"
		}


		return solve
	