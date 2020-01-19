
Inputs	= {
	
	"0x": 			"interHalo", #Done
	"0x0029185b": 	"noInfo",	
	"0x00e77545": 	"bcwithdrawl",	
	"0x0309bebc": 	"noInfo",	
	"0x03e985d9": 	"noInfo",	
	"0x04e27777": 	"noInfo",	
	"0x06862706": 	"noInfo",	
	"0x095ea7b3": 	"ethTransferWallettoDex1",
	"0x338b5dea":   "ethTransferWallettoDex2",
	"0x0b927666": 	"dexPlaceOrder",
	"0x0c8e8326": 	"noInfo",
	"0x13a30791": 	"noInfo",
	"0x19f7ae27": 	"noInfo",
	"0x2a95599f": 	"MarketplaceCancelOrder",
	"0x2e1a7d4d": 	"haloFromDexToWallet",
	"0x31663639": 	"dexFilledOrder",
	"0x44811585": 	"serviceFee",
	"0x4b67e07f": 	"noInfo",
	"0x4d4ea199": 	"noInfo",
	"0x4e656f5f": 	"noInfo",
	"0x5848e444": 	"noInfo",
	"0x5bd05f7f": 	"noInfo",
	"0x60606040": 	"contractDeployment",
	"0x61443a5f": 	"noInfo",
	"0x65863672": 	"noInfo",
	"0x68627069": 	"noInfo",
	"0x6d69fcaf": 	"noInfo",
	"0x6f0ef949": 	"noInfo",
	"0x726c4d6f": 	"CommitToSharedContract",
	"0x749726fe": 	"noInfo",
	"0x76319190": 	"noInfo",
	"0x763819ea": 	"masternodeCreate",
	"0x792fa508": 	"masternodeSuspend",
	"0x7c325d0e": 	"masternodeTerminate",
	"0x7f746573": 	"noInfo",
	"0x8255069d": 	"dexOrderCancelled",
	"0x9407ea98": 	"noInfo",
	"0x976640e2": 	"noInfo",
	"0x98ca05eb": 	"noInfo",
	"0x99404220": 	"noInfo",
	"0x9e281a98": 	"hethToEth",
	"0x9f8a89ba": 	"nodeActivate",
	"0xa9059cbb": 	"WrappedTokenTransfer",
	"0xb214faa5": 	"gamesDeposit",
	"0xb36c2acc": 	"ethOffNetwork",
	"0xb5ec9999": 	"noInfo",
	"0xc885bc58": 	"masternodePayout",
	"0xc94ee098": 	"noInfo",
	"0xcbb0f029": 	"boughtMarketplace",
	"0xceeb7066": 	"noInfo",
	"0xd0e30db0": 	"HaloWalletToDex",
	"0xd4444da6": 	"masternodeSell",
	"0xdf6c39fb": 	"payout",
	"0xea115fdb": 	"noInfo",
	"0xf612f5ce": 	"noInfo",
	"0xff3252a1": 	"noInfo",
	"0x68627069":   "systemPing",
	"0xd28c25d4":	"Smart Contract"
}

def HexToDec(hex):
	
	x = 	int(hex, 16)
	x = 	str(x)
	
	return 	x



def DecToHex(dec):
	x = 	int(dec)
	x =		hex(x)

	return x



def InputParse(input):
	
	fields =  		int(len(input))
	fieldlenth = 	fields - 10
	fieldNumber = 	fieldlenth/64
	a = 			10 
	x = 			1
	list = 			[input[0:10]]

	while x <= fieldNumber:
		b = 		a + 64
		sector = 	input[a:b]
		sect = 		HexToDec(sector)
		a = 		b
		x = 		x + 1
		list.append(sect)
	return list	



def GetType(inpoot):
	answer = InputParse(inpoot)
	if answer[0] in Inputs :
		type = answer[0]
		type = Inputs[type]
		answer = [type] + answer
		
		return(answer)
	else:
		answer = "0x00000000"
		type = "Unknown"
		answer = type + answer
		return answer

def timestamp(stamp):
		time = 			stamp
		dt = 			datetime.fromtimestamp(time // 1000000000)
		s = 			dt.strftime('%Y-%m-%d %H:%M:%S')
		return s
