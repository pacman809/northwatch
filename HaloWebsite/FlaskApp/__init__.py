from flask import Flask, request, render_template, flash, redirect, send_file
from dailytx import dailyTransactions, OnedailyTransactions
from web3 import Web3
from heth import solvency
from explorerdryrun import getAccountHistory
from latesttx import lastTx, OnelastTx

import os
from flask import send_from_directory
from powerball import powerball
from data import onetimestamp,OneblockResults, performance, masternode, payout, query, balanceInfo, blockResults, getType, timestamp, transResults, rawParse, Oneperformance

app = Flask(__name__)
app.config["DEBUG"] = True
#--------------------------------------------------------------------------------------------------------------------------


@app.route("/sitemap")
def google():
	return render_template("sitemap.xml")

@app.route("/image")
def image():
	return send_file("positivessl_trust_seal_sm_124x32.png", mimetype='image/gif')
#--------------------------------------------------------------------------------------------------------------------------

@app.route("/.well-known/brave-rewards-verification.txt")
def brave():
	return render_template("brave-rewards-verification.txt")

#--------------------------------------------------------------------------------------------------------------------------

@app.route("/.well-known/pki-validation/673BAB75F6FEBBC68144FC4594C13136.txt")
def sslone():
	return render_template("673BAB75F6FEBBC68144FC4594C13136.txt")

#---------------------------------------------------------------------------------------------------------------------------


@app.route("/.well-known/pki-validation/1217BF0E73C8CC49E03EF1DAEA0DD25B.txt")
def ssl():
	return render_template("1217BF0E73C8CC49E03EF1DAEA0DD25B.txt")

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
	#return render_template('maint.html')

	
#---------------------------------------------------------------------------------------------------------------------------



@app.route('/ether1', methods=["GET", "POST"])
def ether1main():
	
	history = OnelastTx()
	return render_template('ether1index.html', history= history )
	#return render_template('maint.html')

	
#---------------------------------------------------------------------------------------------------------------------------
@app.route('/stats')
def stats():

	transactions = dailyTransactions()
	result = performance()
	return render_template('stats.html', result= result, transactions= transactions)

#---------------------------------------------------------------------------------------------------------------------------
@app.route('/ether1/stats')
def onestats():

	transactions = OnedailyTransactions()
	result = Oneperformance()
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
	inputData = getType(data)	

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

@app.route('/ether1/block/<id>', methods=['GET', 'POST'])


def Oneblock(id):
	
	block = int(id)
	result = OneblockResults(block)
	transactions = result
	current = Oneperformance()
	#data = result["input"]
	#inputData = getType(data)	

	if result is not  None:
		confirmations = current["BLOCKNUMBER"] - result["number"]
		status = "Database"
		#value = Web3.fromWei(result["value"], 'Ether')
		time = onetimestamp(result["timestamp"])

		return render_template('1block.html', result= result, id= id, status= status, confirmations= confirmations, time= time)

	else:
		status = "Not Databased RPC call coming"	
		return render_template('1block.html', result= result, id= id, status= status)

#---------------------------------------------------------------------------------------------------------------------------
@app.route('/process', methods=["POST"])
def process():


		search = request.form['search']
		searchUrl = query(search)
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

	results = transResults(id)
	parse 	= rawParse(results["input"])
	return render_template('transaction.html', results= results, parse= parse)

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


