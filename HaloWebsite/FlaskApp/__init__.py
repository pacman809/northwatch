import requests
import codecs
from flask import Flask, request, render_template, flash, redirect, send_file
from dailytx import dailyTransactions, OnedailyTransactions
from web3 import Web3
from heth import solvency
from explorerdryrun import getAccountHistory, OnegetAccountHistory, TwogetAccountHistory
from latesttx import lastTx, OnelastTx, TwolastTx
from status import NodeStatus
import os
from flask import send_from_directory
from powerball import powerball
from data import OnetransResults, TwotransResults, onetimestamp, OneblockResults, TwoblockResults, performance, masternode, payout, query, Onequery, Twoquery, balanceInfo, Twoperformance, OnebalanceInfo, TwobalanceInfo, blockResults, getType, timestamp, transResults, rawParse, Oneperformance
from Upland import UserProfile

app = Flask(__name__)
app.config["DEBUG"] = True

site_url = "www.haloexplorer.com"
#--------------------------------------------------------------------------------------------------------------------------


@app.route("/sitemap")
def google():
	return render_template("/SITEMAP/sitemap.xml")

@app.route("/image")
def image():
	return send_file("/SITEMAP/positivessl_trust_seal_sm_124x32.png", mimetype='image/gif')
#--------------------------------------------------------------------------------------------------------------------------

@app.route("/.well-known/brave-rewards-verification.txt")
def brave():
	return render_template("/KEYS/brave-rewards-verification.txt")

#--------------------------------------------------------------------------------------------------------------------------

@app.route("/.well-known/pki-validation/673BAB75F6FEBBC68144FC4594C13136.txt")
def sslone():
	return render_template("/KEYS/673BAB75F6FEBBC68144FC4594C13136.txt")

#---------------------------------------------------------------------------------------------------------------------------


@app.route("/.well-known/pki-validation/1217BF0E73C8CC49E03EF1DAEA0DD25B.txt")
def ssl():
	return render_template("/KEYS/1217BF0E73C8CC49E03EF1DAEA0DD25B.txt")

#---------------------------------------------------------------------------------------------------------------------------


@app.route("/keybase.txt")
def keybase_txt():
	return render_template("/KEYS/keybase.txt")


#---------------------------------------------------------------------------------------------------------------------------


@app.route("/robots.txt") 
def robots_txt():
    return render_template("/KEYS/robots.txt")


#---------------------------------------------------------------------------------------------------------------------------


@app.route('/HALO', methods=["GET", "POST"])
def main():
	
	history = lastTx()
	lastPayout = payout()
	return render_template('/HALO/index.html', history= history, lastPayout= lastPayout, url= site_url)
	#return render_template('maint.html')

	
#---------------------------------------------------------------------------------------------------------------------------



@app.route('/ETHER1', methods=["GET", "POST"])
def ether1main():
	
	history = OnelastTx()
	return render_template('/ETHER1/index.html', history= history )
	#return render_template('maint.html')

	
#---------------------------------------------------------------------------------------------------------------------------



@app.route('/EGEM', methods=["GET", "POST"])
def egemmain():

        history = TwolastTx()
        return render_template('/EGEM/index.html', history= history )
        #return render_template('maint.html')


#---------------------------------------------------------------------------------------------------------------------------
@app.route('/HALO/stats')
def stats():

	transactions = dailyTransactions()
	result = performance()
	return render_template('/HALO/stats.html', result= result, transactions= transactions)

#---------------------------------------------------------------------------------------------------------------------------
@app.route('/ETHER1/stats')
def onestats():

	transactions = OnedailyTransactions()
	result = Oneperformance()
	return render_template('/ETHER1/stats.html', result= result, transactions= transactions)

#---------------------------------------------------------------------------------------------------------------------------

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

#---------------------------------------------------------------------------------------------------------------------------

@app.route('/HALO/block/<id>', methods=['GET', 'POST'])


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

		return render_template('/HALO/block.html', result= result, id= id, status= status, confirmations= confirmations, value= value, inputData= inputData, time= time)

	else:
		status = "Not Databased RPC call coming"	
		return render_template('/HALO/block.html', result= result, id= id, status= status)

#---------------------------------------------------------------------------------------------------------------------------

@app.route('/ETHER1/block/<id>', methods=['GET', 'POST'])


def Oneblock(id):
	
	block 				= int(id)
	result 				= OneblockResults(block)
	transactions 		= result
	current 			= Oneperformance()
	#extradata 			= result["extra_data"]
	try:
		extra_data			= result['extra_data'][2:]
		extra_data 			= codecs.decode(extra_data, "hex").decode('utf-8')
	except:
		extra_data			= "Bad Hex"
	#data = result["input"]
	#inputData = getType(data)	

	if result is not  None:
		confirmations = current["BLOCKNUMBER"] - result["number"]
		status = "Database"
		#value = Web3.fromWei(result["value"], 'Ether')
		time = onetimestamp(result["timestamp"])

		return render_template('/ETHER1/block.html', result= result, id= id, status= status, confirmations= confirmations, time= time, extra_data= extra_data)

	else:
		status = "Not Databased RPC call coming"	
		return render_template('/ETHER1/block.html', result= result, id= id, status= status)

#---------------------------------------------------------------------------------------------------------------------------
@app.route('/EGEM/block/<id>', methods=['GET', 'POST'])


def Twoblock(id):
	
	block 				= int(id)
	result 				= TwoblockResults(block)
	transactions 		= result
	current 			= Twoperformance()
	#extradata 			= result["extra_data"]
	try:
		extra_data			= result['extra_data'][2:]
		extra_data 			= codecs.decode(extra_data, "hex").decode('utf-8')
	except:
		extra_data			= "Bad Hex"
	#data = result["input"]
	#inputData = getType(data)	

	if result is not  None:
		confirmations = current["BLOCKNUMBER"] - result["number"]
		status = "Database"
		#value = Web3.fromWei(result["value"], 'Ether')
		time = onetimestamp(result["timestamp"])

		return render_template('/EGEM/block.html', result= result, id= id, status= status, confirmations= confirmations, time= time, extra_data= extra_data)

	else:
		status = "Not Databased RPC call coming"	
		return render_template('/EGEM/block.html', result= result, id= id, status= status)

#---------------------------------------------------------------------------------------------------------------------------
@app.route('/HALO/process', methods=["POST"])
def process():


		search = request.form['search']
		searchUrl = query(search)
		try:
			return redirect(searchUrl)
		except Exception as e:
			return redirect("https://{}").format(site_url)
		




#---------------------------------------------------------------------------------------------------------------------------
@app.route('/ETHER1/process', methods=["POST"])
def Oneprocess():


		search = request.form['search']
		searchUrl = Onequery(search)
		try:
			return redirect(searchUrl)
		except Exception as e:
			return redirect("https://{}/ETHER1").format(site_url)
		


@app.route('/EGEM/process', methods=["POST"])
def Twoprocess():


		search = request.form['search']
		searchUrl = Twoquery(search)
		try:
			return redirect(searchUrl)
		except Exception as e:
			return redirect("https://{}/EGEM").format(site_url)
		




#---------------------------------------------------------------------------------------------------------------------------


@app.route('/HALO/balance/<id>', methods=["GET", "POST"])

def balance(id):

	masternode1 = masternode(id)
	history = getAccountHistory(id)
	balance = balanceInfo(id)
	return render_template('/HALO/balance.html', balance= balance, address= id, history= history[0], masternode= masternode1, txCount= history[1])
	balance.clear()
	balance = {}
	masternode1 = {}
	history = {}
	


#--------------------------------------------------------------------------------------------------------------------------------


@app.route('/ETHER1/balance/<id>', methods=["GET", "POST"])

def Onebalance(id):

	#masternode1 = masternode(id)
	history = OnegetAccountHistory(id)
	balance = OnebalanceInfo(id)
	return render_template('/ETHER1/balance.html', balance= balance, address= id, history= history[0], txCount= history[1])
	balance.clear()
	balance = {}
	masternode1 = {}
	history = {}
	



@app.route('/EGEM/balance/<id>', methods=["GET", "POST"])

def Twobalance(id):

	#masternode1 = masternode(id)
	history = TwogetAccountHistory(id)
	balance = TwobalanceInfo(id)
	#ETH = float(history[2]) * float(balance[1])
	return render_template('/EGEM/balance.html', balance= balance, address= id, history= history[0], txCount= history[1])
	balance.clear()
	balance = {}
	masternode1 = {}
	history = {}
	


#--------------------------------------------------------------------------------------------------------------------------------
@app.route('/HALO/tx/<id>')

def transResolve(id):

	results = transResults(id)
	parse 	= rawParse(results["input"])
	return render_template('/HALO/transaction.html', results= results, parse= parse)


@app.route('/ETHER1/tx/<id>')

def OnetransResolve(id):

	try:
		results = OnetransResults(id)
		parse 	= rawParse(results["input"])
		return render_template('/ETHER1/transaction.html', results= results, parse= parse)
	except:
		results = OnetransResults(id)
		parse 	= "No Input"
		return render_template('/ETHER1/transaction.html', results= results, parse= parse)

@app.route('/EGEM/tx/<id>')

def TwotransResolve(id):

	try:
		results = TwotransResults(id)
		parse 	= rawParse(results["input"])
		return render_template('/EGEM/transaction.html', results= results, parse= parse)
	except:
		results = TwotransResults(id)
		parse 	= "No Input"
		return render_template('/EGEM/transaction.html', results= results, parse= parse)

#-------------------------------------------------------------------------------------------------------------------------------	

#-------------------------------------------------------------------------------------------------------------------------------

@app.route('/about')

def about():

	return render_template('about.html')

#-------------------------------------------------------------------------------------------------------------------------------

@app.route("/dex") 
def dex():
    return render_template("/HALO/dex.html")

#-------------------------------------------------------------------------------------------------------------------------------



@app.route("/HALO/powercontract") 

def powercontract():
	PWR_contract = powerball()
	return render_template("/HALO/PowerContract.html", result= PWR_contract)

#-------------------------------------------------------------------------------------------------------------------------------


@app.route("/HALO/None") 
def whoops():
    return render_template("/HALO/whoops.html")

@app.route("/ETHER1/None") 
def Onewhoops():
    return render_template("/ETHER1/whoops.html")

#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------

@app.route('/HALO/solvency')

def solvent():

	result = solvency()
	return render_template('/HALO/solvent.html', result= result)


@app.route('/')

def maint():
	status = NodeStatus()
	return render_template('/northwatch.html', status= status)	

#--------------------------UPLAND STUFF---------------------------------------------
@app.route('/llama')

def my_form():

    return render_template('UPLAND/llama2.html')


@app.route('/llama', methods=['POST'])

def my_form_post():

	text = request.form['text']
	text = text.lower()
	username = text.upper()
	profile = UserProfile(text)
	
	return render_template('UPLAND/llama3.html', profile= profile,  username= username)


if __name__ == '__main__':
   app.run()


