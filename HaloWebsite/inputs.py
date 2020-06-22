import pymongo
from web3 import Web3
from data import connect_geth, timestamp, database, onetimestamp, one_connect_geth, two_connect_geth, Onedatabase

#------------------------------------------------------------------------------------------------------------
#GENERAL TRANSACTION
def hextodec(hex):					#Converts Decimal To Hex
	
	x = 	int(hex, 16)
	x = 	str(x)
	
	return 	x


def dectohex(dec):
	x = 	int(dec)
	x =		hex(x)

	return x


def parse(input):				#Takes Input And Parses 
	
	fields 		=	int(len(input))
	fieldlenth 	= 	fields - 10
	fieldNumber = 	fieldlenth/64
	a 			= 	10 
	x 			= 	1
	list		= 	[]

	while x <= fieldNumber:
		b 		= 	a + 64
		sector 	= 	input[a:b]
		sect 	= 	hextodec(sector)
		a 		= 	b
		x 		= 	x + 1

		list.append(sect)
	
	return list	

#-----------------------------------------------------------------------------------------------------------

known_address_contract={

	"0x45842a0f603ef5a5aa44503767c6ab9fd03d824e"	: "STEX Hot Wallet",
	"0x630583fde8e6899c74d942814a3719b6d544220e"	: "Northwatch Donations",
	"0xc8a9d002fdaebf5bf03d530c3047d96b44257f10"	: "T4i MN Pool",
	"0x3fcf16e7090fe013b5648d796908916b2290b6c6"	: "Block And Chain Games",
	"0x5271aa0ec2e9cc54db55136554a10cf2f7daa82b"	: "HaloDex SC",
	"0x123ea742a564eaa8e83871618bd9baaf400ff482"	: "LAToken Hot Wallet"

	}

#-----------------------------------------------------------------------------------------------------------


def tokenType(contract):

	tokens={
	"0x0"	: "HALO",
	"0xd314d564c36c1b9fbbf6b440122f84da9a551029"	: "ETH",
	"0xc8481effc60fa765ccf8286ba346233ed113b024"	: "BAT",
	"0x59195ebd987bde65258547041e1baed5fbd18e8b"	: "DBET",
	"0xb8648f065205b9c31055653d668723f4b840e4c0"	: "BTC", #8 Decimals
	"0x14d01e64f0573925e28d69dc3846b2f0986ab8b8"	: "HST",
	"0x280750ccb7554faec2079e8d8719515d6decdc84"	: "VET",
	"0x0792fe820e7f65da788ac002ce88c74816b59142"	: "OMG",
	"0xdc14c317abf4fca7ac2255f0da73b39f63598c76"	: "USDC",
	"0x343350a2b298370381cac03fe3c525c28600b21"		: "VTHO",
	"0xb70b02222c53abf4e9ccac8fb701425db2ec4de1"	: "ZRX",
	"0x200941b46e8cbb645fe85cdd526e48826acfd8fa"	: "FLASH",
	"0x72649f2a739f2ed7454ca146fb9ba589747287f2"	: "UDOO",
	"0x792fe820e7f65da788ac002ce88c74816b59142"		: "VTHO",
	"0xc57b9e7a29bc7fa4ee9e23994105a3c0278832cd"	: "TOKEN",
	"0x7cb51f76837e4c0e48cdabdf01107ca90bdbe561"    : "TOKEN2",
	"0x32e31f27aaf3501a4f7139970477020baf9c8e1c"	: "TESTP", #PEG
	"0x9c9b95ed2123c3d7e8e7b65c7cd7b302bc26a13a"	: "TEST", #???
	"0xdf5e6ded3dfe4041519eb9d1e57dbe71b2760262"	: "F1", #FCT
	"0xc43a6a22d3a430f175a994683005572cdb18f47c"	: "TEST", #Halo Classic Test
	"0x1793bc201acbb64f3925ae5cb4355e78864a2597"	: "HALOC", #Halo Classic Legit
	"0x5f2786097350e9d0a0cbba233774631991dc5e40"	: "EVED", #EVED
	"0x0023bc712073f013fd810693a7c40da5002e9b84"	: "Dud", #TUTOTEST
	"0xbc77c9ae443940b8ca147870063ee2213264d8b6"	: "WIZARD", #WIZARD
	"0xf6ad1612a655977ed1d0934aefa541f8660ee3a2"	:"UNKNOWN",
	"0xddb500dbe30c91398a2ade12234d4075aabea650"	: "XXX"	, #FACTOM
	"0x978dc9ca2d75c9d187a9cb542c74c50c579a034a"	: "F2",
	"0xdfd55110016251c7537d7645f35f92afcfc468ed" 	: "HXRO", #
	"0xa6002d6df526683b528f87f95b4903f3c76cb7de"	: "FCT", #8 decimals
	"0x4734e87fbd52516ff729345bbf910557f630477c"	: "PEGNET",
	"0x0343350a2b298370381cac03fe3c525c28600b21"	: "VTHO"

	}

	Onetokens		={

	"0xd2ecdb1c74ffbffc3debcff5b603006fbef89fa3", # "TTC"
	"0x92e6c6eee2d4de4585ffe101e1e3288fb4e28330", # "KOT"
	"0xf69bc54fda5d2689a4d4fe8c1e6a5cbc25f6dc59", # "VOTE"
	"0xc715e66000ceaee350c82c34b9b153c3c52f295b", # "BTC"
	"0xa888fbc3f9ca63776913d807804fc31c5ebda6d7", # "KOT"
	"0x0290e09904fb5f0a93d2b231757bcdf8250f68f3", # ""
	"0x47e9c4dcad7075f18f2dce6b227b1cdb071d8f96", # "DYEX"
	"0xb414d147b2fbdeef1b1c867d2ab13a97fb03e230", # "ICD"
	"0x8ff672b71b0064e45b1ab161e6882fa01ce02fbc", # "PSTL"
	"0x4a87e1c4897b216be40c84efc3ccf7c5a9b9cec9", # "FWD"
	"0xe3a444c91fae96dd4323b32842aeb30c6d93848f", # "ICO"
	"0x28549f5a9f0412e9c5c0349370a00b1577a0e862", # "CMCF"
	"0x735287951abcaa8687a1cf1ec93e7f447f37f1e2", # "FCKCK"
	"0x7cca98459f1b7a2df55f3b4f4375de3fbbf0a0e1", # "USDD"
	"0x51750bafc234e99e53f3f2f56b2a180040dd0b7a" # "USDD"

	}


	x = str(contract)
	coin = tokens[x]
	return coin



def OnetokenType(contract):


	Onetokens		={


	"0xd2ecdb1c74ffbffc3debcff5b603006fbef89fa3" : "TTC",
	"0x92e6c6eee2d4de4585ffe101e1e3288fb4e28330" : "KOT",
	"0xf69bc54fda5d2689a4d4fe8c1e6a5cbc25f6dc59" : "VOTE",
	"0xc715e66000ceaee350c82c34b9b153c3c52f295b" : "BTC",
	"0xa888fbc3f9ca63776913d807804fc31c5ebda6d7" : "KOT",
	"0x0290e09904fb5f0a93d2b231757bcdf8250f68f3" : "",
	"0x47e9c4dcad7075f18f2dce6b227b1cdb071d8f96" : "DYEX",
	"0xb414d147b2fbdeef1b1c867d2ab13a97fb03e230" : "ICD",
	"0x8ff672b71b0064e45b1ab161e6882fa01ce02fbc" : "PSTL",
	"0x4a87e1c4897b216be40c84efc3ccf7c5a9b9cec9" : "FWD",
	"0xe3a444c91fae96dd4323b32842aeb30c6d93848f" : "ICO",
	"0x28549f5a9f0412e9c5c0349370a00b1577a0e862" : "CMCF",
	"0x735287951abcaa8687a1cf1ec93e7f447f37f1e2" : "FCKCK",
	"0x7cca98459f1b7a2df55f3b4f4375de3fbbf0a0e1" : "USDD",
	"0x51750bafc234e99e53f3f2f56b2a180040dd0b7a" : "USDD"

	}

	x = str(contract)
	coin = Onetokens[x]
	return coin


def Twotokentype(contract):

	Twotokens		={

	"0xf3fe5bf46525577ca16980aecfacaf0a7a0e8970" : "TRX",
	"0x037148f537e3e46db9ee7d71d050f0865fdc36df" : "UEGEM",
	"0xd2fd37ef18910f6ed4fd7d60ab5179902a4a5e9b" : "TEST",
	"0x954e6c333a6415a6ed3d5cf4057824b23a3a2cc2" : "EGEMSTAKE1",
	"0xd50537325faab2e09b6c5f2d2661e6e6d8273f1b" : "EGEMSTAKE1",
	"0xc302c5c09387f0584318048b02e8f80f09f20fc4" : "EGEMSTAKE1",
	"0x5c87e1c5867365a41fc1deff56d4d554db38bd8c" : "POS",
	"0xb0aad95e4ca0afdde25b936a0a9133d801a301f9" : "EGEMSTAKE1",
	"0x8288649dae790ae0326dc784685a531b9e7d32c0" : "EGEMSTAKE1",
	"0x03ee556c795fd61900c2b9683cee069600bb0dcb" : "EGEMSTAKE1",
	"0x7b90ace6081e04eaa3595716c01c3a2bb8c93908" : "EGEMSTAKE1",
	"0x7784343f49be147516329d175098430f08da3d89" : "EGEMSTAKE1",
	"0xd29c637d62bb056c2e85f9b146b0e87451008613" : "EGEMSTAKE1",
	"0x3c6d158687718f24e9f0bd159c52b7c608d00b6b" : "EGEMSTAKE1",
	"0xaa2b129c8beb6ea9d974059f43659af22b1a41cb" : "POS",
	"0xba445f153c644ce5ab5519b23448b4d2721ba142" : "EGEMSTAKE1",
	"0xb779e74c3c2e07024d4dfb248db6736137f68fee" : "EGEMSTAKE1",
	"0x0842511951e520d7accc672175a173ffb1e179e4" : "EGEMSTAKE1",
	"0x16e46a65b6bef602f8ceebbf5e90c07692426174" : "EGEMSTAKE1",
	"0x526ce7efa21f81cbda54e7dbc5d35c3435a9bb31" : "EGEMSTAKE1",
	"0x3650dca09b5a77c2e6449e2b932dcc740fd48fff" : "EGEMSTAKE1",
	"0x56cca152f6f841aef3a6f91c8554f6acd0c99d40" : "EGEMSTAKE1",
	"0xe41de4267126ff64cf3930797193050995c6853d" : "EGEMSTAKE1",
	"0x656b956f72a7adedb4ed647794bfcdb98b6e78c6" : "EGEMSTAKE1",
	"0xa1f9bc6597127868ae4d1928cf3fc6bc99a2b35e" : "EGEMSTAKE1",
	"0x79092cce5250e614c2c8c693dff8e3f3b7c363bd" : "EGEMSTAKE1",
	"0x5eee439f0b831c13a91dd116848b0ac2cedacda4" : "EGEMSTAKE1",
	"0x51eb7be0282c8569cfc36b71b4adc4591daeafbd" : "EGEMSTAKE1",
	"0xea5e9e8aa6bb1c4270555c5088faa1f612307fe2" : "EGEMSTAKE1",
	"0xea3ba9a5c29c52f68f48e1802467eb717716a540" : "EGEMSTAKE1",
	"0x8b0d3fd518864f2b6bc0ac3c02fcaca1cc7bfdf8" : "EGEMSTAKE1",
	"0x2a8c595a44c3ba8ef13b8282b0b1f0867b87e60e" : "EGEMSTAKE1",
	"0x58590fa4edba0877c3134046574c8926f03b88a5" : "EGEMSTAKE1",
	"0xaa815a530d57a4f4d58ab32a47f3dd398120dd6d" : "EGEMSTAKE1",
	"0x0df501988859f93980feaa195d21673630ccc5e5" : "EGEMSTAKE1",
	"0x5ac20c706961c1aabb96bed54e6504f64dac6247" : "EGEMSTAKE1",
	"0x6a85842671e0c4ace2f55cc2fa7002241ad2f90a" : "EGEMSTAKE1",
	"0xcb644cccaddc48ce48187a9f18ee53a668b0d1e1" : "EGEMSTAKE1",
	"0x249c44be4fc1c60ab3e4130d249ef46034a108c0" : "EGEMSTAKE1",
	"0x7188b9ad51e3ede1d8b10aa76ff853586a0f26d1" : "EGEMSTAKE1",
	"0x684d61f586e007c249035d4116189e2698349fb0" : "EGEMSTAKE1",
	"0x7dc01bbb14873c85157474d26750a041bc48e057" : "EGEMSTAKE1",
	"0xaeb942ad9f9592cda563f01669d2480f82557b6b" : "EGEMSTAKE1",
	"0x23bf619dd30c7001f0a58ab8397e05d8ad4cde52" : "EGEMSTAKE1",
	"0x726221b7f0f35d66ed69626f4df34bf92c16ecef" : "EGEMSTAKE1",
	"0xb16854bbda067c57206b573bbe46ea64744e4902" : "EGEMSTAKE1",
	"0xe232ed00390fa77815d48eaf00cf6f0258bce748" : "EGEMSTAKE1",
	"0xa6777b27c5434deeb6decb90585007840e39af20" : "EGEMSTAKE1",
	"0xf36a920249fd57b0e30f906a10d648a2115a203e" : "EGEMSTAKE1",
	"0x733f9679699dcd15052dca32cdb163ab70015f94" : "EGEMSTAKE1",
	"0x3c7996073601dd96e238ac83a8d52a2c5cd2a126" : "EGEMSTAKE1",
	"0xe105bb16b9981eaeffd7e3c69a7dd448fad2c71d" : "EGEMSTAKE1",
	"0x62323482097f703adf70cf76a06318aed00a1cf9" : "EGEMSTAKE1",
	"0x08155500d93405684af906e18c8f1160e9fcf072" : "EGEMSTAKE1",
	"0xe92628b9b2b48b2ce5a48f791a3cc4ed74f904a1" : "EGEMSTAKE1",
	"0x8fef0e247f4498ddd42f8181f42354dcebcbadfd" : "EGEMSTAKE1",
	"0x432d7f45567122a68321ac7a552077bce88ef2e8" : "EGEMSTAKE1",
	"0x1fb637f5a596a54609c4278d45126b59ed94f771" : "EGEMSTAKE1",
	"0x9acd0c5bfeadef935dc2c403cd295cdb17e46ee8" : "EGEMSTAKE1",
	"0x3c01996be1cec5bff33f952762f172e80fe7bf52" : "EGEMSTAKE1",
	"0xe31f6117eb02ca2e34307e8bd0a1676414b0fab9" : "EGEMSTAKE1",
	"0x7105574be8da4c7e0b960055823a510943b84f81" : "EGEMSTAKE1",
	"0x94176d3083126095f2503168ddd7a264f6ad77ee" : "EGEMSTAKE1",
	"0x743e02a4ff7f959a81bf06356565d5401fa7727f" : "EGEMSTAKE1",
	"0xafff975ac7d09bb132a354b81edf233dbdf251cc" : "EGEMSTAKE1",
	"0x135397c1de46ba0e5d2ccef7808fe01df903c494" : "EGEMSTAKE1",
	"0xa415ef917e3a518908855101c093d5cdc82d79fb" : "EGEMSTAKE1",
	"0xf9584b4723af3c039044c63bd0a36d8e1cb35304" : "EGEMSTAKE1",
	"0x3b111fd7134c59994bcdc34f8f712cd01c1f1bba" : "EGEMSTAKE1",
	"0xcbffc19bb38cd8634c379f3515435df84fd0baeb" : "FIXED",
	"0x9bff190d807b64307298d42893be8ad541ecc2f9" : "EGEMSTAKE1",
	"0xd13f1e4ba5a631cb0dc53cb31ff05218864f861e" : "JAL",
	"0x4468b3be5295a22f446f02af72545df367bc92b8" : "EGEMSTAKE1",
	"0xd0542f0f9053a9f1350cc303bff0823d665f75ee" : "FIXED",
	"0xfaf62eece9be3ad9b56647606aa911b94428c286" : "EGT",
	"0x0bdf46a5628522479032146ea26aba33644d1ff4" : "EGEMSTAKE1",
	"0xcc78f87d9ddd139eaa414068f7289d7116974432" : "EGEMSTAKE1",
	"0x659b22c4c44474495788b88bb6b02ab1fce977d1" : "FIXED",
	"0x75e3aead9d360b683d27fdd2f0d3fcac094ae70f" : "EGEMSTAKE1",
	"0xc682935c53498cecfecc5042b777efaa796b3b44" : "EGEMSTAKE1",
	"0xe4622e61f02ce1ca979f7cf7d619e1245fa707a7" : "EGEMSTAKE1",
	"0x775e0f5e295afadb747d4c893fbfc6b60cc644c3" : "EGEMSTAKE1",
	"0x85b21e03786b4975d7ecd9d4e0f8fd818d26d025" : "EGEMSTAKE1",
	"0xe174ec02bdc77a1ddcf6609d5f9727792a3bd0cd" : "EGEMSTAKE1",
	"0xaa9b8ce8d84a53880bd55980edff2aba94c44527" : "EGEMSTAKE1",
	"0xa24ef11765dec469a0e7b1b4b8af33000bcae208" : "EGEMSTAKE1",
	"0x1b0c1f3aceb98ef9fb7e1200298ca115d2c64081" : "EGEMSTAKE1",
	"0x08d0e9f2bf81ef79bb1aabbc78fbdc913063c138" : "EGEMSTAKE1",
	"0xf826d588d1d77fa0d5646b1dcb3a5e12ca250be3" : "EGEMSTAKE1",
	"0xb3714d90375b05ab271632aeb3afb9e55b5f0bd8" : "EGEMSTAKE1",
	"0xf034679b897dde1f8309b42f1de30bcb74ce7701" : "EGEMSTAKE1",
	"0xac6316e16e9b57940a96292d73bbe472e2c05e42" : "EGEMSTAKE1",
	"0x9359d55c315855b0e61ff29fe258fa318d871c66" : "EGEMSTAKE1",
	"0x83324f6bee616c15c43aa9805834012b9230e69a" : "EGEMSTAKE1",
	"0x7f51cb2f6480c78005a5de5c3459a27b35cbf7a0" : "EGEMSTAKE1",
	"0x6e98f58dc062773336af98038857ec50d9476850" : "EGEMSTAKE1",
	"0x9f56977c697db8dd4a6ff1efb079b476a3bbd5d0" : "EGEMSTAKE1",
	"0x35c98ccd701cf53fe0f2e203638dd5208785d49a" : "EGEMSTAKE1",
	"0x501564ef8a5ba9118bb928dc39ebce55377d8ee6" : "EGEMSTAKE1",
	"0x132648e5c20cb14c8ca1ba55c4f644bed88efe58" : "EGEMSTAKE1",
	"0x920683447785153c05cccf9c9daac572fe4cf031" : "EGEMSTAKE1",
	"0x3c50055c80c489b92aa16cfaf25e172ce16b7f58" : "EGEMSTAKE1",
	"0x63b4a9d5d3134761a43a81c70ea95896dfcce638" : "EGEMSTAKE1",
	"0x8054271ebab5972a8f009bdc31e259d696e5db42" : "EGEMSTAKE1",
	"0x4c50ca4f3eae66431e6316f5a77241741e09b5cb" : "EGEMSTAKE1",
	"0xf7f14972a2658acaa590cfea2c14a3e0c3e91013" : "EGEMSTAKE1",
	"0x3fb89cc4b96bdd60ba871a4dd13e28568d25babc" : "EGEMSTAKE1",
	"0xaa41283d896b60ebfa1ca41a14eb37b3f8b7b28a" : "EGEMSTAKE1",
	"0xaeaffec42e1bd69ce364af694f96abdd44c2d467" : "EGEMSTAKE1",
	"0x751b16ef91c2adb2d460bb8cd0ef807a481c02d6" : "EGEMSTAKE1",
	"0x2b3ac48c996b116be65d33b011be0d6148bd2bd1" : "EGEMSTAKE1",
	"0x52e720aad15effbd752e5f92918de17b36eb9f84" : "EGEMSTAKE1",
	"0x36af553cec8b9fa93edf8294469842f44fbcc0fc" : "EGEMSTAKE1",
	"0xb1c8d6087be456459021c7f27363babb4790aed9" : "EGEMSTAKE1",
	"0xd6d4650262a00c6dd400a6066a7c33d823bf1842" : "EGEMSTAKE1",
	"0xabcf9d5f757dab77b3abf545ba2579cb2b0eff20" : "EGT",
	"0x07dbddf2ab49107e2dff52dd5e3034ab79b6672e" : "EGT",
	"0x2a3fbf1daadcadc7c4ceb98497d31a142c3a48b7" : "EGEMSTAKE1",
	"0x0e13576b5af685fcff32daab61caedea04bbfb8c" : "EGEMSTAKE1",
	"0x64733d74ef649a8ae79762268007b6594c020eaf" : "EGEMSTAKE1",
	"0xad0057514442d85927f4ef8bdb31f1dacd5221af" : "EGEMSTAKE1",
	"0xce35b3f8c963a6476689b11a56cb33b462c5271e" : "EGEMSTAKE1",
	"0xfd8a0e25821a90338c39d572baeeda278f57d38b" : "EGEMSTAKE1",
	"0x20fddc81b38c4d912764763d44a31fbb21de915f" : "EGEMSTAKE1",
	"0x3bef1ae112e407c9d3dbf85fac2caf5775df6b45" : "EGEMSTAKE1",
	"0x27a61f69a63a2efa88a1a17da4894e22d87a54fe" : "EGEMSTAKE1",
	"0x44755efe07ab91fffa55a76d72d90a891697efe6" : "EGEMSTAKE1",
	"0x9c62d97dd6e9dd88b56bec39a95fd178b5c99dc9" : "EGEMSTAKE1",
	"0x9db163aa4cc4f1d3717ebd4396573c8577575db5" : "EGEMSTAKE1",
	"0x3b8c270385c5267e2c7c94096385e9a7bdbee433" : "EGEMSTAKE1",
	"0xe25bf6b4714b1f17f2eefb0f28392e01c3a94c6f" : "EGEMSTAKE1",
	"0xf5750987363661d03d8c77d109a37f6bd000cc26" : "EGEMSTAKE1",
	"0x9b9c964ff8c066eb953b551b896cb8f7d6b32636" : "EGEMSTAKE1",
	"0x18b10dbeb6fd8f5823c800c364c4211edaceb1c2" : "EGEMSTAKE1",
	"0x8c74b5065f1c0b7e6586e4e6d115235746e6a6cb" : "EGEMSTAKE1",
	"0x752437d2a7c2d264b586093660ec4c38a7565d86" : "EGEMSTAKE1",
	"0x3a2686e8557c4b88a2fde000de6f61ca3b543f89" : "EGEMSTAKE1",
	"0xbbcfef3e2d9fafabc6c762980de9fd9cc040d13f" : "EGEMSTAKE1",
	"0xdfcf282648c54f7c87bce280584fb746ec60b391" : "EST",
	"0x7260b2b71f53a07dc4558b042b7004b9a10c7ede" : "EGEMSTAKE1",
	"0xe5f6f0579bf9f9343610e9f67e2f07d487543946" : "EST",
	"0x2e7e97c4a940dc475741250ab882a16e9f164060" : "EST",
	"0x254e663ff78ef451df01d743d33fdcd4ea97a1ad" : "EST",
	"0x70e0c1afccd65f5dcb9305ade401c6f051234ccc" : "EST",
	"0x7a0c1a435960c08d1159df78a02e383d315158fd" : "EST",
	"0x8d7ca347f5ba7ae849048519c20e045f2305a97d" : "EST",
	"0xec9870a1fdfb41459fc06a00a72beab9c440b4ea" : "EST",
	"0xd924e1cc8699d573d8aa80db37f4f5d690d433fa" : "EST",
	"0xb3edaab1f411277d9f1793b96902697fe1aaebe5" : "EST",
	"0x5c1bb93ba3cbc39e877785154b4760a6daf755e5" : "EST",
	"0xf51cf787d07faa8bf88598ec99ab6fdf6b9055d3" : "EST",
	"0x5a07c55054a5028d0c6c6cd3a3832373583228c3" : "EST",
	"0x4109ec64912d2232db058712869ed73fdd60ca61" : "EST",
	"0xc5514b0cc45a9aa37f21edaa44ea9fbf7725ba4c" : "EST",
	"0xad47f72d272006c1cbf1283b61dcaf931f25df4f" : "EST",
	"0x6afd8fe45942456b25c8a0a99642228f50f9d608" : "EST",
	"0xea0b75b0a6eaf0554ce61851bb9f1f3c471bb143" : "EST",
	"0xbfad1fef04d6079e8dce0ac1786b6c5ef665aa5c" : "EST",
	"0x209caf465786343fedf5bb4d2a5215943f3c207a" : "EST",
	"0x97f6e3599a44b5bd4cd4fee6357ddc21356b46a6" : "EST",
	"0x4244a461aa0f3ae8cdfd1e5c97a0d5125688471c" : "EST",
	"0x65ccb199843e9e392110cee5481da4de028ac197" : "EST",
	"0x5a8537509db6138916341807ae8f5caa423fe23b" : "EST",
	"0x16505b7e21a7e6673ce746e75ebf90b98107786b" : "EST",
	"0x5fcc0b98185caad33058b608aa8653e9e39adfe4" : "EST",
	"0x9f230efc0f77922cf44a8b7929a70ec4f5f168f3" : "EGT",
	"0xc1d0d69aba63f8db63bbf41ee826fa1bb2053035" : "tyu",
	"0x072d097ae9cadae292fbac4dc25c25de8affadb6" : "EGT",
	"0xfff1a4d3cc13dd47b4c7dcfbc7b4bfd59fb4ca88" : "EGT",
	"0x6903c69fe03e3b6e285d630b378a822437a33f10" : "EGT",
	"0x42e08795b52c82883e6bcb134a6d154d8e23cdf6" : "ECT",
	"0xb6bd73e2afe9c610527731e65eb78e6349435d71" : "ECT",
	"0xcf7a713140c3d7d05059870fb9480e67d9fa4d9b" : "ECT",
	"0x311b2b536667046c8a437742938c7f441d7023dd" : "DEMO",
	"0xf10945f86912e34c3f36a2b05026c187574afeb8" : "DX",
	"0xd7d2f21774e5c1c3502678be869bb0323241b925" : "DX",
	"0xa1c036a1b083dd9d9ea8427dca4c1d53f089be57" : "0xBTC",
	"0x0c5106dc60033c5ac6ec3d504883c451265e7560" : "NDR",
	"0x58d0a32a5680b2bf6364ca68ae181ce5fa4eaf57" : "ELLA",
	"0xc1ff97815505c4331ad3d6c737a6d63cbab27b39" : "1337",
	"0xd98f2112b41ca111a6265eac81b5497bbf1db9b0" : "SHIT",
	"0xb85433c5719bb05fd4bad25fad734629c78fe512" : "SHT",
	"0x79f9133098e0824e60ccd27b6fcaef07eb1b677c" : "NRGM",
	"0xb8489fbaa4e56858ba529f10667bd17333c6a0b5" : "VLDY",
	"0xb0702df32de0371f39a98cc911a2dd69c3a13e6f" : "VLDY",
	"0x3dbdc750207ff7c9ca157c71ade6057aa32e3cc1" : "JILL",
	"0x2144aceaec70c0dcccc90fe8aff2ce9c983ab775" : "JILL",
	"0x59fe86c2878b5385015e413077e3f98e9e3a235a" : "ETTT",
	"0x37a270f23a7bd7938465ffb7f90985ed0cdf13e5" : "DAPP",
	"0x1eab0ef3ee6b43feb94b73fa69a12bff98d0fdb6" : "ETTT",
	"0xb482d6d4e5623b51a0b923f8ebda63a420b3e74a" : "ETTT",
	"0x4fb1bc3e2613b159b1690cae662895256c609772" : "JILL",
	"0x921ee2a83d104a772b148d775633df3df33efb87" : "JILL",
	"0xb7eafb3e1a191ffe6e21e5f5e0e262e46862cdb5" : "ETTT",
	"0xb4eac2b9abaf776f7473ff745f452281f577c4b9" : "JACK",
	"0x076478959ab61d4d4c0371d7c0632aebd2c9654a" : "ETTT",
	"0xb3b3ac664dd96da1ca86a4dffbd627b6b773ff8c" : "ETTT",
	"0x5a67432e892eed079c26eaf307e281dc106c582b" : "ETTT",
	"0x82e00728095e4a99eddb6711714143e1aa94353b" : "ETTT",
	"0x435f699b6cc2338d65490a9f312af80b3c8247d0" : "ETTT",
	"0xfe05e1715a3ab7556f703a1e44e26cb18cc252b6" : "ETTT",
	"0x09925344416dca1112f6320c1e20af16688e6e3a" : "ETTT",
	"0xf20e2e9adf5124a4865eddbe0fa4e542862c956f" : "ETTT",
	"0x49a8e0798dde576325323a97292a194000d842ca" : "ETTT",
	"0xef975e9c43e95d04d20854cee705228ffb11fac6" : "ETTT",
	"0x7f866e285f0dfd8973432b32f58ba0d685f32252" : "ETTT",
	"0xaf8bd64cd7814d2df8e9be3943bde9b4c5d9d9fd" : "ETTT",
	"0xd1f2bd092f71d12d634a48ad13b939ec415a4239" : "ETTT",
	"0x0d9671daf93af25075d0ce2f508f1f26168863ec" : "ETTT",
	"0xd8efd8f9526c6787e8f2308776d180d7108e989e" : "ETTT",
	"0x176c6a5ca426c925e5cbc037554a5df8d7dab41e" : "ETTT",
	"0xd614c9eabf121dcf24e0e40aef4919358040f20d" : "ETTT",
	"0x651211ba04491e717ba3c0bd57e36f69d7b79315" : "ETTT",
	"0x97093d13503d3075c28c13ef41f080a1a11ec69b" : "ETTT",
	"0xc73eddf3e704f87461a8a6b05a4d14849ca1b0f6" : "ETTT",
	"0xa1bfc80eadf0f29a3b975ceedf7ce71217ca0bf4" : "ETTT",
	"0xbb6f1e9327f2e532a279bfb572e638a63ee0d3b1" : "ETTT",
	"0xb7ec829d70af236c41bc034112b026695a3f736a" : "ETTT",
	"0x6e2b7bdf8ed2026f27b75cf5d16a211899ef0989" : "ETTT",
	"0x864e8582d98cf20678ebb80cb12388e68475b7d7" : "ETTT",
	"0x7d437afcdf9d31c18014a2d6d61457e21d11f0cc" : "ETTT",
	"0xc1b2cd2d6dfee6c2b79540ca2c1916199265a927" : "ETTT",
	"0x9250af2a8fa661536426a27afabdfa2b5da8b87a" : "ETTT",
	"0xe79fd457c5234de79fccf29a709a6972f6269f6b" : "ETTT",
	"0xff6d5105e0b5b7b4cf0b04ff3bee997bbc1d1998" : "ETTT",
	"0x9a2343941b675222ed34e4f34c52cb49b24140b8" : "ETTT",
	"0x8696c9b72239a7e42cca93bd32a5ba253aa66580" : "ETTT",
	"0x48c34f68d911e4c82747f8fa9eb55ca6613dfb7a" : "ETTT",
	"0x77008d140686c2e4307001383e96190bbcb31a03" : "ETTT",
	"0x3ffba95461d5a4a742b40d39e70549a5ed282177" : "ETTT",
	"0x3b3f4fe00c80878dcc718a02afad9e713349f50e" : "ETTT",
	"0x060174a7984e651afaa25f1e1a61051956603ed4" : "ETTT"
	}

#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


def hotlist(hotlist):


	if hotlist in known_address_contract:
			x = str(hotlist)
			known = known_address_contract[x]
			return known
	else :
			return hotlist

#-----------------------------------------------------------------------------------------------------------


def MNPAYOUT(to_address):

	address 						= Web3.toChecksumAddress(to_address)
	web3 							= connect_geth()
	mydb 							= database()
	myBlock 						= mydb["blocks"]
	myCol 							= mydb["transactions"]
	
	
	
	for x in myCol.find({"to_address": to_address, "input": '0xc885bc58'}):

		block_number 				= x["block_number"]
		post_reward 				= Web3.fromWei(web3.eth.getBalance(address, block_number),'Ether')
		block_number 				= int(block_number)
		block_number 				= block_number - 1
		pre_reward 					= Web3.fromWei(web3.eth.getBalance(address, block_number),'Ether')
		reward 						= pre_reward - post_reward
		result						= reward
	

		return result


#-----------------------------------------------------------------------------------------------------------


def systemPing(receivedInput):

	DESCRIPTOR = "System Ping"

	value                           = Web3.fromWei(receivedInput['value'], 'Ether')
	description                     = f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	
	result							= {

	"descriptor"                    : DESCRIPTOR,
	"hash"                          : receivedInput['hash'],
	"nonce"                         : receivedInput['nonce'],
	"block_hash"                    : receivedInput['block_hash'],
	"block_number"                  : receivedInput['block_number'],
	"transaction_index"             : receivedInput['transaction_index'],
	"from_address"                  : receivedInput['from_address'],
	"to_address"                    : receivedInput['to_address'],
	"value"                         : value,
	"gas"                           : receivedInput['gas'],
	"gas_price"                     : receivedInput['gas_price'],
	"block_timestamp"               : timestamp(receivedInput['block_timestamp']),
	"description"					: description
						
	}


	return result




#----------------INPUTS-------HERE-----------------------------------------------------------------



def interHalo(receivedInput):
	
	DESCRIPTOR = "Interhalo Transaction"

	#value					= Web3.fromWei(receivedInput['value'], 'Ether')

	value 					= receivedInput['value'] / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')

	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	

	result					={

	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description

	}

	
	return result
	

def etherOneTx(receivedInput):
	
	DESCRIPTOR = "Ether-1 Transaction"

	#value					= Web3.fromWei(receivedInput['value'], 'Ether')

	value 					= receivedInput['value'] / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')

	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	

	result					={

	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: onetimestamp(receivedInput['block_timestamp']),
	"description"			: description

	}

	
	return result	

def TwoTx(receivedInput):
	
	DESCRIPTOR = "EGEM Transaction"

	#value					= Web3.fromWei(receivedInput['value'], 'Ether')

	value 					= receivedInput['value'] / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')

	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	

	result					={

	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: onetimestamp(receivedInput['block_timestamp']),
	"description"			: description

	}

	
	return result	

def bot_tip(receivedInput):
	
	DESCRIPTOR = "Tip Bot"

	#value					= Web3.fromWei(receivedInput['value'], 'Ether')

	value 					= receivedInput['value'] / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')

	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	

	result					={

	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: onetimestamp(receivedInput['block_timestamp']),
	"description"			: description

	}

	
	return result		
#---------------------------------------------------------------------------------------------------

def Burn(receivedInput):
	
	DESCRIPTOR = "Token Burned"

	result = parse(receivedInput["input"])
	value					= Web3.fromWei(int(result[0]), 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	



	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result
	
#---------------------------------------------------------------------------------------------------

def ContractDeploy(receivedInput):
	
	DESCRIPTOR = "CONTRACT DEPLOY"
	value					= Web3.fromWei(receivedInput['value'], 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description

							}

	
	return result
	
#---------------------------------------------------------------------------------------------------


def SmartContract(receivedInput):
	
	DESCRIPTOR = "Smart Contract Interaction"

	value					= Web3.fromWei(receivedInput['value'], 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result
	
#---------------------------------------------------------------------------------------------------

def payout(receivedInput):
	
	DESCRIPTOR = "MN Payout"

	value					= Web3.fromWei(receivedInput['value'], 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result
	
#---------------------------------------------------------------------------------------------------
def CommitToSharedContract(receivedInput): #"0x726c4d6f": 	,
	
	DESCRIPTOR = "Commit To MN Contract"

	#value					= Web3.fromWei(receivedInput['value'], 'Ether')
	value 					= receivedInput['value'] / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result

#-----------------------------------------------------------------------------------------------------------

def noInfo(receivedInput):

	DESCRIPTOR = "PLEASE REPORT BLOCK NUMBER AND A BREIF SUMMARY OF WHAT YOU THINK THIS IS"
	description = f'Unknown At the Current Time'

	#value					= Web3.fromWei(receivedInput['value'], 'Ether')
	value 					= receivedInput['value'] / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')
	
	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description

							}

	
	return result
#------------------------------------------------------------------------------------------------------------


def ERCDeposit(receivedInput):

	DESCRIPTOR = "ERC20 Deposited"
	description = "nil"

	#value					= Web3.fromWei(receivedInput['value'], 'Ether')
	value 					= receivedInput['value'] / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description

							}

	
	return result
#------------------------------------------------------------------------------------------------------------
#MASTERNODES



def DepositEth(receivedInput):

	mydb 		= 	database()
	myETH		= 	mydb["ethereum"]


	DESCRIPTOR = "Ether Deposited"
	timestampCheck   = receivedInput["block_timestamp"]

	try:
		for x in myETH.find({ "block_timestamp" : timestampCheck }):
			x['value'] = int(x['value'])
			#value			= Web3.fromWei(x['value'], 'Ether')
			value 					= x['value'] / 1000000000000000000
			value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')
			description 	= f'Databased ETH Deposit'
		
			result={
			"descriptor"			: DESCRIPTOR,
			"hash" 					: x['hash'],			
			"nonce"					: x['nonce'],
			"block_hash"			: x['block_hash'],
			"block_number"			: x['block_number'],
			"transaction_index"		: x['transaction_index'],
			"from_address"			: x['from_address'],
			"to_address"			: x['to_address'],
			"value"					: value,
			"gas" 					: x['gas'],
			"gas_price"				: x['gas_price'],
			"block_timestamp"		: timestamp(x['block_timestamp']),
			"description"			: description
			}
			

			y = result
			
			return y

	except:
			receivedInput['value'] = int(x['value'])
			#value			= Web3.fromWei(x['value'], 'Ether')
			value 					= x['value'] / 1000000000000000000
			value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')
			description 	= f'Calculated ETH Deposit'
		
			result={
			"descriptor"			: DESCRIPTOR,
			"hash" 					: receivedInput['hash'],			
			"nonce"					: receivedInput['nonce'],
			"block_hash"			: receivedInput['block_hash'],
			"block_number"			: receivedInput['block_number'],
			"transaction_index"		: receivedInput['transaction_index'],
			"from_address"			: receivedInput['from_address'],
			"to_address"			: receivedInput['to_address'],
			"value"					: value,
			"gas" 					: receivedInput['gas'],
			"gas_price"				: receivedInput['gas_price'],
			"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
			"description"			: description
			}
				

			y = result
				
			return y

	
#------------------------------------------------------------------------------------------------------------

def masternodePayout(receivedInput):

	mydb 		= 	database()
	myMN		= 	mydb["masternodes"]

	DESCRIPTOR = "Claimed MN Reward"
	to_address = receivedInput["to_address"]
	checkHash  = receivedInput["block_timestamp"]

	try:
		for x in myMN.find({ "timestamp" : checkHash }):
			reward = x["reward"]

			description = f'Masternode {receivedInput["to_address"]} Payout'
		
		result={
		"descriptor"			: DESCRIPTOR,
		"hash" 					: receivedInput['hash'],			
		"nonce"					: receivedInput['nonce'],
		"block_hash"			: receivedInput['block_hash'],
		"block_number"			: receivedInput['block_number'],
		"transaction_index"		: receivedInput['transaction_index'],
		"from_address"			: receivedInput['from_address'],
		"to_address"			: receivedInput['to_address'],
		"value"					: reward,
		"gas" 					: receivedInput['gas'],
		"gas_price"				: receivedInput['gas_price'],
		"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
		"description"			: description,
		"reward"				: reward
		}
		

		y = result
		
		return y

	except:
		reward = MNPAYOUT(to_address)

		description = f'Masternode {receivedInput["to_address"]} Payout'
		
		result={
		"descriptor"			: DESCRIPTOR,
		"hash" 					: receivedInput['hash'],			
		"nonce"					: receivedInput['nonce'],
		"block_hash"			: receivedInput['block_hash'],
		"block_number"			: receivedInput['block_number'],
		"transaction_index"		: receivedInput['transaction_index'],
		"from_address"			: receivedInput['from_address'],
		"to_address"			: receivedInput['to_address'],
		"value"					: reward,
		"gas" 					: receivedInput['gas'],
		"gas_price"				: receivedInput['gas_price'],
		"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
		"description"			: description,
		"reward"				: reward
		}
		

		y = result
		return y

#---------------------------------------------------------------------------------------------------------------

def HaloWalletToDex(receivedInput): #0xd0e30db0

	DESCRIPTOR = "Wallet --> HaloDex"
	#value                                   = Web3.fromWei(receivedInput['value'], 'Ether')
	value 					= receivedInput['value'] / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')

	description = f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	#to_address_known = hotlist(receivedInput["to_address"])
	#from_address_known = hotlist(receivedInput["from_address"])

	result={
	"descriptor"                    : DESCRIPTOR,
	"hash"                          : receivedInput['hash'],
	"nonce"                         : receivedInput['nonce'],
	"block_hash"                    : receivedInput['block_hash'],
	"block_number"                  : receivedInput['block_number'],
	"transaction_index"             : receivedInput['transaction_index'],
	"from_address"                  : receivedInput['from_address'],
	"to_address"                    : receivedInput['to_address'],
	"value"                         : value,
	"gas"                           : receivedInput['gas'],
	"gas_price"                     : receivedInput['gas_price'],
	"block_timestamp"               : timestamp(receivedInput['block_timestamp']),
	"description"                   : description
	}

	return result


#---------------------------------------------------------------------------------------------------------------



	
def haloFromDexToWallet(receivedInput): #"0x2e1a7d4d"

	DESCRIPTOR = "HaloDex --> Wallet"

	scrape = parse(receivedInput["input"])
	scrape = int(scrape[0])
	#value      = str(Web3.fromWei(scrape, 'Ether'))
	value 					= scrape / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')

	description = f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result={
	"descriptor"                    : DESCRIPTOR,
	"hash"                          : receivedInput['hash'],
	"nonce"                         : receivedInput['nonce'],
	"block_hash"                    : receivedInput['block_hash'],
	"block_number"                  : receivedInput['block_number'],
	"transaction_index"             : receivedInput['transaction_index'],
	"from_address"                  : receivedInput['from_address'],
	"to_address"                    : receivedInput['to_address'],
	"value"                         : value,
	"gas"                           : receivedInput['gas'],
	"gas_price"                     : receivedInput['gas_price'],
	"block_timestamp"               : timestamp(receivedInput['block_timestamp']),
	"description"                   : description
	}

	return result


#----------------------------------------------------------------------------------------------------------


def masternodeSell(receivedInput): #0xd4444da6
	
	DESCRIPTOR = "Masternode Sell Order on Marketplace"
	data = receivedInput["input"]

	answer = parse(data)
	masternode = dectohex(answer[0])
	

	shares_for_sale = int(answer[2])
	shares_for_sale = Web3.fromWei(shares_for_sale, 'Ether')
	asking_price = int(answer[3])
	asking_price = Web3.fromWei(asking_price, 'Ether')
	ratio = "{:.2f}".format(shares_for_sale/asking_price)
	
	result={
    "descriptor"                    : DESCRIPTOR,
    "hash"                          : receivedInput['hash'],
    "nonce"                         : receivedInput['nonce'],
    "block_hash"                    : receivedInput['block_hash'],
    "block_number"                  : receivedInput['block_number'],
    "transaction_index"             : receivedInput['transaction_index'],
    "from_address"                  : receivedInput['from_address'],
    "to_address"                    : receivedInput['to_address'],
    "value"                         : f' {shares_for_sale} For {asking_price} / {ratio}',
    "gas"                           : receivedInput['gas'],
    "gas_price"                     : receivedInput['gas_price'],
    "block_timestamp"               : timestamp(receivedInput['block_timestamp'])
    }

	return result

	#COMPLETED

#----------------------------------------------------------------------------------------------------

def masternodeCreate(receivedInput):

	tier = receivedInput["input"]
	tier = tier[73]
	DESCRIPTOR = f'Masternode Created Tier {tier}'

	#value					= Web3.fromWei(receivedInput['value'], 'Ether')
	value 					= receivedInput['value'] / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')

	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result

#------------------------------------------------------------------------------------------------------

def masternodeTerminate(receivedInput):
	DESCRIPTOR = "MASTERNODE Terminated"


	value					= Web3.fromWei(receivedInput['value'], 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: "Terminated",
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result



#------------------------------------------------------------------------------------------------------------

def masternodeSuspend(receivedInput):
	DESCRIPTOR = "MASTERNODE Suspended"


	value					= Web3.fromWei(receivedInput['value'], 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	
	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: "Suspended",
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result



#------------------------------------------------------------------------------------------------------------
#DEX

def dexPlaceOrder(receivedInput):
	DESCRIPTOR = "Dex Order Placed"

	data = receivedInput["input"]
	answer = parse(data)
	orderNumber = str(answer[4])
	Wanting =  tokenType(dectohex(answer[0]))
	shares_wanted = int(answer[1])
	shares_wanted2 = str(Web3.fromWei(shares_wanted, 'Ether'))
	giveCoin = int(answer[3])
	giveCoin2 = str(Web3.fromWei(giveCoin, 'Ether'))
	Giving = tokenType(dectohex(answer[2]))
	
	

	result={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: Web3.fromWei(receivedInput['value'], 'Ether'),
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp'])
	#"input"					: {"orderNumber": answer[4], "amountWanted": shares_wanted2, "wantCoin": Wanting,  "amountGiving": giveCoin2, "giveCoin": Giving }
	}

	

	return result


def dexOrderCancelled(receivedInput):

	DESCRIPTOR = "HaloDex Order Cancelled"

	value					= "Cancelled Order"
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result

#------------------------------------------------------------------------------------------------------------



def ethOffNetwork(receivedInput): #"0xb36c2acc": 	ethOffNetwork

	DESCRIPTOR = "H-ETH sent to ETH Chain"

	data = receivedInput["input"]
	answer = parse(data)


	value					= int(answer[1])
	value 					= value / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')
	description 			= "H-ETH sent to ETH Chain"
	eth 					= data[34:74]
	eth_address = 			"0x" + eth

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: eth_address,
	"value"					: value,
	"gas" 					: eth_address,
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description,
	"external"				: "https://etherscan.io/address/{}".format(eth_address)
							}

	
	return result


#------------------------------------------------------------------------------------------------------------


def ERCtoChain(receivedInput): 

	inputs = receivedInput['input']
	contract = receivedInput["to_address"]
	token = tokenType(contract)
	
	DESCRIPTOR = (f'{token} --> ETH Network')

	#DESCRIPTOR = "ERC20 to ETH Chain"

	data = receivedInput["input"]
	answer = parse(data)


	value					= int(answer[1])
	value 					= Web3.fromWei(value, 'ETHER')
	description 			= "H-ETH sent to ETH Chain"
	eth 					= data[34:74]

	eth_address = 			"0x" + eth

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: eth_address,
	"value"					: value,
	"gas" 					: eth_address,
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description,
	"external"				: "https://etherscan.io/address/{}".format(eth_address)
							}

	
	return result


#------------------------------------------------------------------------------------------------------------
#ETH

def ethTransferWallettoDex1(receivedInput): #"0x095ea7b3"
	
	inputs = receivedInput['input']
	contract = parse(inputs)
	realvalue = int(contract[1])
	token = tokenType(receivedInput["to_address"])
	DESCRIPTOR = f'{token} --> HaloDex SC'
	
	value					= Web3.fromWei(realvalue, 'Ether')
	description = f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	if token == "FCT" :
            balance = value * 10000000000
            value = '{0:.20f}'.format(balance).rstrip('0').rstrip('.')

	result={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description	
	}

	return result
#------------------------------------------------------------------------------------------

def ethTransferWallettoDex2(receivedInput):

	inputs = receivedInput['input']
	contract = parse(inputs)
	token2 = dectohex(contract[0])
	token = tokenType(token2)
	
	DESCRIPTOR = (f'{token} Deposit --> HaloDex')
	realvalue = int(contract[1])
	value					= Web3.fromWei(realvalue, 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	if token == "FCT" :
            balance = value * 10000000000
            value = '{0:.20f}'.format(balance).rstrip('0').rstrip('.')
            

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result

#---------------------------------------------------------------------------------------------

def hethToEth(receivedInput): #0x9e281a98
	
	inputs = receivedInput['input']
	contract = parse(inputs)
	token2 = dectohex(contract[0])
	token = tokenType(token2)
	DESCRIPTOR = (f' {token} Withdrawl From HaloDex')
	
	realvalue = int(contract[1])
	value					= Web3.fromWei(realvalue, 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result

#------------------------------------------------------------------------------------------------	
def dexPlaceOrder1(receivedInput): #"0x0b927666": 	dexPlaceOrder,
	DESCRIPTOR = "Dex Order Placed "

	value					= Web3.fromWei(receivedInput['value'], 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	value					= "Order Placed"

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result





def dexFilledOrder(receivedInput): #"0x31663639": 	dexFilledOrder,
	DESCRIPTOR = "Dex Order Filled "

	inputs = parse(receivedInput["input"])
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	value					= "Order Filled"
	giveCoin = tokenType(dectohex(inputs[1]))
	values = int(inputs[11])
	weis	= dectohex(inputs[5])
	giveValue = Web3.fromWei(values, 'ETHER')
	receivedCoin = tokenType(dectohex(inputs[3]))
	value2 = int(inputs[4])
	receivedValue = Web3.fromWei(value2 , 'ETHER')
	tradePartner = dectohex(inputs[7])
	price = giveValue/receivedValue

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
	#"input"					: f' {giveValue} {giveCoin} For {receivedValue} {receivedCoin} Buyer/Seller = {tradePartner} Price = {price}',
							}

	
	return result


#GAMES

def gamesDeposit(receivedInput):
	
	DESCRIPTOR = "Block And Chain Deposit"

	value					= Web3.fromWei(receivedInput['value'], 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	
	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}
							

	
	return result


def WrappedTokenTransfer(receivedInput):
	
	inputs = receivedInput['input']
	contract = parse(inputs)
	toAddress = dectohex(contract[0])
	token = tokenType(receivedInput["to_address"])
	 

	DESCRIPTOR = (f' {token} Transfer Between Halo Wallets')
	amount = int(contract[1])
	value					= Web3.fromWei(amount, 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: toAddress,
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result



def boughtMarketplace(receivedInput):
	
	DESCRIPTOR = "Marketplace MN Purchase"

	value					= Web3.fromWei(receivedInput['value'], 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result


def serviceFee(receivedInput):
	

	fee = parse(receivedInput["input"])
	fee = int(fee[3])
	value = "Fee"
	DESCRIPTOR = "SF"
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result


def bcwithdrawl(receivedInput):

	bandc = parse(receivedInput["input"])
	to_address = dectohex(bandc[3])
	value = int(bandc[2])
	DESCRIPTOR = "Block And Chain Withdraw" 

	value					= Web3.fromWei(value, 'Ether')

	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['to_address'],
	"to_address"			: to_address,
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result




def nodeActivate(receivedInput):
	
	DESCRIPTOR = "Node Activated"

	value					= Web3.fromWei(receivedInput['value'], 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: "Activated",
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result

def contractDeployment(receivedInput):
	
	DESCRIPTOR = "Contract Deployed"

	value					= Web3.fromWei(receivedInput['value'], 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: "Deploment",
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: timestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result




Inputs	= {
	
	"0x": 			interHalo, #Done
	"0x0029185b": 	noInfo,	
	"0x00e77545": 	bcwithdrawl,	
	"0x0309bebc": 	noInfo,	
	"0x03e985d9": 	noInfo,	
	"0x04e27777": 	noInfo,	
	"0x06862706": 	noInfo,	
	"0x095ea7b3": 	ethTransferWallettoDex1,
	"0x338b5dea":   ethTransferWallettoDex2,
	"0x0b927666": 	dexPlaceOrder,
	"0x0c8e8326":	noInfo,
	"0x0c8e8326": 	ERCtoChain,
	"0x13a30791": 	noInfo,
	"0x19f7ae27": 	noInfo,
	#"0x2a95599f": 	MarketplaceCancelOrder,
	"0x2e1a7d4d": 	haloFromDexToWallet,
	"0x31663639": 	dexFilledOrder,
	"0x44811585": 	serviceFee,
	"0x4b67e07f": 	noInfo,
	"0x4d4ea199": 	noInfo,
	"0x4e656f5f": 	noInfo,
	"0x5848e444": 	noInfo,
	"0x5bd05f7f": 	noInfo,
	"0x60606040": 	contractDeployment,
	"0x61443a5f": 	noInfo,
	"0x65863672": 	noInfo,
	"0x68627069": 	noInfo,
	"0x6d69fcaf": 	noInfo,
	"0x6f0ef949": 	noInfo,
	"0x726c4d6f": 	CommitToSharedContract,
	"0x749726fe": 	noInfo,
	"0x76319190": 	noInfo,
	"0x763819ea": 	masternodeCreate,
	"0x792fa508": 	masternodeSuspend,
	"0x7c325d0e": 	masternodeTerminate,
	"0x7f746573": 	noInfo,
	"0x8255069d": 	dexOrderCancelled,
	"0x9407ea98": 	noInfo,
	"0x976640e2": 	noInfo,
	"0x98ca05eb": 	ERCDeposit,
	"0x99404220": 	noInfo,
	"0x9e281a98": 	hethToEth,
	"0x9f8a89ba": 	nodeActivate,
	"0xa9059cbb": 	WrappedTokenTransfer,
	"0xb214faa5": 	gamesDeposit,
	"0xb36c2acc": 	ethOffNetwork,
	"0xb5ec9999": 	noInfo,
	"0xc885bc58": 	masternodePayout,
	"0xc94ee098": 	noInfo,
	"0xcbb0f029": 	boughtMarketplace,
	"0xceeb7066": 	noInfo,
	"0xd0e30db0": 	HaloWalletToDex,
	"0xd4444da6": 	masternodeSell,
	"0xdf6c39fb": 	payout,
	"0xea115fdb": 	DepositEth,
	"0xf612f5ce": 	noInfo,
	"0xff3252a1": 	noInfo,
	"0x68627069":   systemPing,
	"0xd28c25d4":	SmartContract,
	"0x60806040": 	ContractDeploy,
	"0x42966c68" : Burn


}
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ETHER _ 1 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#MMMMMMMMMMMMMMMMm/mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMh/-.hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMy:/-..yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMs///:---sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMNs///+:::::oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMmooo+++/::///oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMhyMMMMM/ NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN--+MMMM
#MMMMMMd++ooo+o+/////+omMMMMMMMMMMMMMMMMMMMMMMMMMMM:"MMMMM/ NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM""MMMM
#MMMMMh//+oosoo++++++++omMMMMMMMMMMMMMs+++++++sNMM+. +omMM/ Nho///+sMMMNs+++++++sNMMMNs+++MMMMMMMMMMM""MMMM
#MMMMs://+oossso+oooooooodMMMMMMMMMMMo sNNNNNs oMMm-'mmNMM/ :smNNNs sMMo sNNNNNs oMMMo sNNMMMMMMMMMMM""MMMM
#MMMo-://+oossssoooossssssdMMMMMMMMMMo dMMMMMm +MMM:'MMMMM/ NMMMMMd oMM+ dMMMMMm +MMM+ mMMMMMMMMMMMMM''MMMM
#MMMMNhs++oossysssssssydmMMMMMMMMMMMMo +ooooo+ +MMM:'MMMMM/ NMMMMMd oMM+ +ooooo+ +MMM+ mMMMMh:::+MMMM""MMMM
#MMMNmmMMNdyssyyssyhmNMNmmNMMMMMMMMMMo ydddddddmMMM:'MMMMM/ NMMMMMd oMM+ ydddddddmMMM+ mMMMMMMMMMMMMM""MMMM
#MMMMMdhhdmMMNmdmNMMNdhhdMMMMMMMMMMMMo dMMMMMNshMMM:'MMMMM/ NMMMMMd oMM+ dMMMMMNshMMM+ mMMMMMMMMMMMMM""MMMM
#MMMMMMdyyyoshmMmdhyyyymMMMMMMMMMMMMMy /hhhhh+ sMMM/ ohdMM/ NMMMMMd oMMs /hhhhh/ sMMy: sdMMMMMMMMMMMs""sMMM
#MMMMMMMmsoo+++NsssssyNMMMMMMMMMMMMMMMdyyyyyyydMMMMMdyyhMMdhMMMMMMNhmMMMdyyyyyyydMMMhhhhmMMMMMMMMMMMhhhhMMM
#MMMMMMMMNs+///N++++yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMy/::N///hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMd:-N-/mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMN/m+NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

import codecs
def EthoFuse(receivedInput):
	
	DESCRIPTOR = "Etho-Fuse Game"

	#value					= Web3.fromWei(receivedInput['value'], 'Ether')

	value 					= receivedInput['value'] / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')

	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	

	result					={

	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: onetimestamp(receivedInput['block_timestamp']),
	"description"			: description

	}

	
	return result	


def OneWrappedTokenTransfer(receivedInput):
	
	inputs = receivedInput['input']
	contract = parse(inputs)
	toAddress = dectohex(contract[0])
	token = OnetokenType(receivedInput["to_address"])
	 

	DESCRIPTOR = (f' {token} Transfer Between Ether-1 Wallets')
	amount = int(contract[1])
	value					= Web3.fromWei(amount, 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: toAddress,
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: onetimestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result

def TwoWrappedTokenTransfer(receivedInput):
	
	inputs = receivedInput['input']
	contract = parse(inputs)
	toAddress = dectohex(contract[0])
	token = Twotokentype(receivedInput["to_address"])
	 

	DESCRIPTOR = (f' {token} Transfer Between Ether-1 Wallets')
	amount = int(contract[1])
	value					= Web3.fromWei(amount, 'Ether')
	description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'

	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: toAddress,
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: onetimestamp(receivedInput['block_timestamp']),
	"description"			: description
							}

	
	return result

def blockMined(receivedInput):
	
	
	myclient 	= 	pymongo.MongoClient("mongodb://localhost:27017/")
	web3 		= 	one_connect_geth()
	db 			= 	"ether1-explorer-mainnet"
	mydb 		= 	myclient[db]
	myCol 		= 	mydb["temp"]
	myCol2 		= 	mydb["block_rewards"]
	bn 			= 	receivedInput['number']

	reward = "Unknown Not DB"
	try:
		for x in myCol2.find({"block_number": bn}):
			reward = " {} ETHO".format(x["reward"][:5])
	except:
		reward = "Unknown"

	DESCRIPTOR = "New Block Mined"
	try:
		extra_data			= receivedInput['extra_data'][2:]
		value 					= codecs.decode(extra_data, "hex").decode('utf-8')

		#value 					= receivedInput['value'] / 1000000000000000000
		#value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')
	except:
		value = "Miner Unknown"

		#description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	

	result					={

	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_number"			: receivedInput['number'],
	"from_address"			: receivedInput['miner'],
	"value"					: value,
	"reward" 				: reward,
	"block_timestamp"		: onetimestamp(receivedInput['timestamp']),
	"description"			: "BlockMined",
	"difficulty"			: receivedInput['difficulty'] / 1000000000

	}

	
	return result	


def TwoblockMined(receivedInput):
	
	
	myclient 	= 	pymongo.MongoClient("mongodb://localhost:27017/")
	web3 		= 	two_connect_geth()
	db 			= 	"egem-explorer-mainnet"
	mydb 		= 	myclient[db]
	myCol 		= 	mydb["temp"]
	myCol2 		= 	mydb["block_rewards"]
	bn 			= 	receivedInput['number']

	reward = "Unknown Not DB"
	try:
		for x in myCol2.find({"block_number": bn}):
			reward = " {} ETHO".format(x["reward"][:5])
	except:
		reward = "Unknown"

	DESCRIPTOR = "New Block Mined"
	try:
		extra_data			= receivedInput['extra_data'][2:]
		value 					= codecs.decode(extra_data, "hex").decode('utf-8')

		#value 					= receivedInput['value'] / 1000000000000000000
		#value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')
	except:
		value = "Miner Unknown"

		#description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	

	result					={

	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_number"			: receivedInput['number'],
	"from_address"			: receivedInput['miner'],
	"value"					: value,
	"reward" 				: reward,
	"block_timestamp"		: onetimestamp(receivedInput['timestamp']),
	"description"			: "BlockMined",
	"difficulty"			: receivedInput['difficulty'] / 1000000000

	}

	
	return result	


def onenoInfo(receivedInput):

	DESCRIPTOR = "PLEASE REPORT BLOCK NUMBER AND A BREIF SUMMARY OF WHAT YOU THINK THIS IS"
	description = f'Unknown At the Current Time'

	#value					= Web3.fromWei(receivedInput['value'], 'Ether')
	value 					= receivedInput['value'] / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')
	
	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: onetimestamp(receivedInput['block_timestamp']),
	"description"			: description

							}

	
	return result
#------------------------------------------------------------------------------------------------------------



def Masternode(receivedInput):

	DESCRIPTOR = "Masternode Related. No Further Details"
	description = f'Unknown At the Current Time'

	#value					= Web3.fromWei(receivedInput['value'], 'Ether')
	value 					= receivedInput['value'] / 1000000000000000000
	value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')
	
	result					={
	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_hash"			: receivedInput['block_hash'],
	"block_number"			: receivedInput['block_number'],
	"transaction_index"		: receivedInput['transaction_index'],
	"from_address"			: receivedInput['from_address'],
	"to_address"			: receivedInput['to_address'],
	"value"					: value,
	"gas" 					: receivedInput['gas'],
	"gas_price"				: receivedInput['gas_price'],
	"block_timestamp"		: onetimestamp(receivedInput['block_timestamp']),
	"description"			: description

							}

	
	return result
OneInputs	= {
	'blockmined':   blockMined,
	'0xa6f2ae3a':	onenoInfo,
	'0x2f54bf6e':	onenoInfo,
	'0x43214675':	onenoInfo,
	'0x1986a58c':	onenoInfo,
	'0xc4d66de8':	onenoInfo,
	'0xb61d27f6':	onenoInfo,
	'0x60806040':	onenoInfo,
	'0xa1adbb25':	onenoInfo,
	'0x2e1a7d4d':	onenoInfo,
	'0x3ccfd60b':	onenoInfo,
	'0x793cd71e':	onenoInfo,
	'0xcb1fa1d8':	onenoInfo,
	'0xcc9ab267':	onenoInfo,
	'0xb18759de':	onenoInfo,
	'0x486579'	:	onenoInfo,
	'0xb75c7dc6':	onenoInfo,
	'0x06ab5923':	onenoInfo,
	'0xf05834d6':	onenoInfo,
	'0xa9059cbb':	OneWrappedTokenTransfer, #-TokenTransfer,
	'0x6dd5e67c':	onenoInfo,
	'0x746970' 	:	bot_tip,
	'0xccb726b1':	onenoInfo,
	'0x57618e1d':	onenoInfo,
	'0xf2fde38b':	onenoInfo,
	'0xfdb5a03e':	EthoFuse,
	'0x19b667da':	onenoInfo,		
	'0x60606040':	onenoInfo,
	'0x797af627':	onenoInfo,
	'0x467fba0f':	onenoInfo,
	'0x424c4f43':	onenoInfo,
	'0x6703777d':	onenoInfo,
	'0x604c602c':	onenoInfo,
	'0x48657920':	onenoInfo,
	'0x507ffba5':	onenoInfo,
	'0x29ff4f53':	onenoInfo,
	'0x8d036731':	onenoInfo,
	'0x49ade46d':	onenoInfo,
	'0x60748060':	onenoInfo,
	'0xfdacd576':	onenoInfo,
	'0x0a9ef927':	onenoInfo,
	'0x4e71d92d':	EthoFuse,
	'0x'		:	etherOneTx,
	'0x04fc7c6d':	onenoInfo,
	'0x230d6ed8':	onenoInfo,
	'0xd65ab5f2':	onenoInfo,
	'0xd420a7e6':	onenoInfo,
	'0xc375c2ef':	Masternode,
	'0xd0e30db0':	onenoInfo,
	'0x55c081d4':	onenoInfo,
	'0x6102cb61':	onenoInfo,
	'0x940c70f3':	onenoInfo
}


def TwoblockMined(receivedInput):
	
	
	myclient 	= 	pymongo.MongoClient("mongodb://localhost:27017/")
	web3 		= 	two_connect_geth()
	db 			= 	"egem-explorer-mainnet"
	mydb 		= 	myclient[db]
	myCol 		= 	mydb["temp"]
	myCol2 		= 	mydb["block_rewards"]
	bn 			= 	receivedInput['number']

	reward = "Unknown Not DB"
	try:
		for x in myCol2.find({"block_number": bn}):
			reward = " {} EGEM".format(x["reward"][:5])
	except:
		reward = "Unknown"

	DESCRIPTOR = "New Block Mined"
	try:
		extra_data			= receivedInput['extra_data'][2:]
		value 					= codecs.decode(extra_data, "hex").decode('utf-8')

		#value 					= receivedInput['value'] / 1000000000000000000
		#value 					= '{0:.20f}'.format(value).rstrip('0').rstrip('.')
	except:
		value = "Miner Unknown"

		#description 			= f'From {receivedInput["from_address"]} To  {receivedInput["to_address"]}'
	

	result					={

	"descriptor"			: DESCRIPTOR,
	"hash" 					: receivedInput['hash'],			
	"nonce"					: receivedInput['nonce'],
	"block_number"			: receivedInput['number'],
	"from_address"			: receivedInput['miner'],
	"value"					: value,
	"reward" 				: reward,
	"block_timestamp"		: onetimestamp(receivedInput['timestamp']),
	"description"			: "BlockMined",
	"difficulty"			: receivedInput['difficulty'] / 1000000000

	}

	
	return result	


TwoInputs	= {
	'blockmined':   TwoblockMined,
	'0xa6f2ae3a':	onenoInfo,
	'0x2f54bf6e':	onenoInfo,
	'0x43214675':	onenoInfo,
	'0x1986a58c':	onenoInfo,
	'0xc4d66de8':	onenoInfo,
	'0xb61d27f6':	onenoInfo,
	'0x60806040':	onenoInfo,
	'0xa1adbb25':	onenoInfo,
	'0x2e1a7d4d':	onenoInfo,
	'0x3ccfd60b':	onenoInfo,
	'0x793cd71e':	onenoInfo,
	'0xcb1fa1d8':	onenoInfo,
	'0xcc9ab267':	onenoInfo,
	'0xb18759de':	onenoInfo,
	'0x486579'	:	onenoInfo,
	'0xb75c7dc6':	onenoInfo,
	'0x06ab5923':	onenoInfo,
	'0xf05834d6':	onenoInfo,
	'0xa9059cbb':	TwoWrappedTokenTransfer, #-TokenTransfer,
	'0x6dd5e67c':	onenoInfo,
	'0x746970' 	:	bot_tip,
	'0xccb726b1':	onenoInfo,
	'0x57618e1d':	onenoInfo,
	'0xf2fde38b':	onenoInfo,
	'0xfdb5a03e':	EthoFuse,
	'0x19b667da':	onenoInfo,		
	'0x60606040':	onenoInfo,
	'0x797af627':	onenoInfo,
	'0x467fba0f':	onenoInfo,
	'0x424c4f43':	onenoInfo,
	'0x6703777d':	onenoInfo,
	'0x604c602c':	onenoInfo,
	'0x48657920':	onenoInfo,
	'0x507ffba5':	onenoInfo,
	'0x29ff4f53':	onenoInfo,
	'0x8d036731':	onenoInfo,
	'0x49ade46d':	onenoInfo,
	'0x60748060':	onenoInfo,
	'0xfdacd576':	onenoInfo,
	'0x0a9ef927':	onenoInfo,
	'0x4e71d92d':	EthoFuse,
	'0x'		:	TwoTx,
	'0x04fc7c6d':	onenoInfo,
	'0x230d6ed8':	onenoInfo,
	'0xd65ab5f2':	onenoInfo,
	'0xd420a7e6':	onenoInfo,
	'0xc375c2ef':	Masternode,
	'0xd0e30db0':	onenoInfo,
	'0x55c081d4':	onenoInfo,
	'0x6102cb61':	onenoInfo,
	'0x940c70f3':	onenoInfo
}
