from flask import Flask, request, render_template, flash, redirect 
from performance import performance
from blockStats import blockResults
from dailytx import dailyTransactions
from toetoken import balanceInfo
from web3 import Web3
from getType import GetType
from getType import timestamp
from TransStats import TransResults
from heth import solvency
from explorerdryrun import getAccountHistory
from masternode import masternode
from latesttx import lastTx
from searchQuery import Query
from payout import payout
app = Flask(__name__)
app.config["DEBUG"] = True
import os
from flask import send_from_directory
from web3 import Web3
from powerball import powerball
#--------------------------------------------------------------------------------------------------------------------------


@app.route("/sitemap")
def google():
	return render_template("sitemap.xml")

#--------------------------------------------------------------------------------------------------------------------------

@app.route("/.well-known/brave-rewards-verification.txt")
def brave():
	return render_template("brave-rewards-verification.txt")

#--------------------------------------------------------------------------------------------------------------------------

@app.route("/.well-known/pki-validation/56FA2597B1C83239463680471A920401.txt")
def sslone():
	return render_template("56FA2597B1C83239463680471A920401.txt")

#---------------------------------------------------------------------------------------------------------------------------


@app.route("/.well-known/pki-validation/AF6E047DFEBBD1690C65D339A7014C87.txt")
def ssl():
	return render_template("AF6E047DFEBBD1690C65D339A7014C87.txt")

#---------------------------------------------------------------------------------------------------------------------------


@app.route("/keybase.txt")
def keybase_txt():
	return render_template("keybase.txt")


#---------------------------------------------------------------------------------------------------------------------------


@app.route("/robots.txt") 
def robots_txt():
    return render_template("robots.txt")


#---------------------------------------------------------------------------------------------------------------------------


@app.route('/splash')
def splash():

    block = performance()
    return render_template('splash.html', block= block)


#---------------------------------------------------------------------------------------------------------------------------


@app.route('/', methods=["GET", "POST"])
def main():
	
	history = lastTx()
	lastPayout = payout()
	return render_template('index.html', history= history, lastPayout= lastPayout)

	
#---------------------------------------------------------------------------------------------------------------------------


@app.route('/stats')
def stats():

	transactions = dailyTransactions()
	result = performance()
	return render_template('stats.html', result= result, transactions= transactions)

#---------------------------------------------------------------------------------------------------------------------------

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

#---------------------------------------------------------------------------------------------------------------------------

@app.route('/block/<id>', methods=['GET', 'POST'])


def block(id):
	
	block = int(id)
	result = blockResults(block)
	transactions = result
	current = performance()
	data = result["input"]
	inputData = GetType(data)	

	if result is not  None:
		confirmations = current["BLOCKNUMBER"] - result["number"]
		status = "Database"
		value = Web3.fromWei(result["value"], 'Ether')
		time = timestamp(result["timestamp"])

		return render_template('block.html', result= result, id= id, status= status, confirmations= confirmations, value= value, inputData= inputData, time= time)

	else:
		status = "Not Databased RPC call coming"	
		return render_template('block.html', result= result, id= id, status= status)

#---------------------------------------------------------------------------------------------------------------------------


@app.route('/process', methods=["POST"])
def process():


		search = request.form['search']
		searchUrl = Query(search)
		try:
			return redirect(searchUrl)
		except Exception as e:
			return redirect("https://www.haloexplorer.com")
		




#---------------------------------------------------------------------------------------------------------------------------


@app.route('/balance/<id>', methods=["GET", "POST"])

def balance(id):

	masternode1 = masternode(id)
	history = getAccountHistory(id)
	balance = balanceInfo(id)
	return render_template('balance.html', balance= balance, address= id, history= history[0], masternode= masternode1, txCount= history[1])
	balance.clear()
	balance = {}
	masternode1 = {}
	history = {}
	


#--------------------------------------------------------------------------------------------------------------------------------

@app.route('/tx/<id>')

def transResolve(id):

	#results = TransResults("0x24d185ebe2c0da0ce63f59793abda63062484cf4d8c50d2f4a1c6ea4f1a6c4f9")
	results = TransResults(id)
	#value = Web3.fromWei(results["value"], 'Ether')
	return render_template('transaction.html', results= results)

#-------------------------------------------------------------------------------------------------------------------------------

@app.route('/about')

def about():

	return render_template('about.html')

#-------------------------------------------------------------------------------------------------------------------------------

@app.route("/dex") 
def dex():
    return render_template("dex.html")

#-------------------------------------------------------------------------------------------------------------------------------



@app.route("/powercontract") 

def powercontract():
	PWR_contract = powerball()
	return render_template("PowerContract.html", result= PWR_contract)

#-------------------------------------------------------------------------------------------------------------------------------


@app.route("/None") 
def whoops():
    return render_template("whoops.html")

#-------------------------------------------------------------------------------------------------------------------------------

@app.route('/solvency')

def solvent():

	result = solvency()
	return render_template('solvent.html', result= result)

if __name__ == '__main__':
   app.run()


