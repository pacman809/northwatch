from web3 import Web3
import json
import requests


def masternode(personal_address):
	results = []
	total_shares = float(0)

	api_url = requests.get("https://mn-api.haloplatform.tech/owned/{}".format(personal_address))
	data_results = api_url.json()

	count = len(data_results["result"])
	if count != 0:
		for x in data_results["result"]:
			shares = float('%.08f' % x["SHARES"]) 
			total_shares = shares + total_shares
			shares = Web3.fromWei(shares, 'ETHER')
			totals = Web3.fromWei(total_shares, 'ETHER')

			masternode_shares = {
			"tier" 		:			int(x["TIER"]),
			"shares" 	:		 	int(shares),
			"masternode": 			x["ADDRESS"],
			}

			results.append(masternode_shares)

			tota = {
			"total" 	: totals,
			}
			
			
	

		results.append(tota)
				
		return results

	else:

		total={
		"total" 	: "None"
		}

		results.append(total)
		return results
	
# SEND IN AN ADDRESS AND IT RETURNS MASTERNODE RESULTS OR A TOTAL OF "NO MASTERNODES"
