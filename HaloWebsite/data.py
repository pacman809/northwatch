import pymongo
import json
from datetime import datetime
from web3 import Web3
import requests
#--------------------CONFIG--------------------------------#

#RPC NODE URL
GethUrl 		= "http://192.168.0.58:8545" #HALO
OneGethUrl 		= "http://192.168.0.58:8585" #ETHER1
TwoGethUrl      = "http://192.168.0.58:8645" #EGEM

#DATABASE NAME
DataBaseName 		= "halo-explorer-mainnet"
OneDataBaseName 	= "ether1-explorer-mainnet"
TwoDataBaseName		= "egem-explorer-mainnet"
#

#COIN CONTRACTS ORDER DETERMINES THE DISPLAY ON BALANCES PAGE
all_coin_contract_addresses =  [
"0xd314d564c36c1b9fbbf6b440122f84da9a551029",
"0xc8481effc60fa765ccf8286ba346233ed113b024",
"0x59195ebd987bde65258547041e1baed5fbd18e8b",
"0xb8648f065205b9c31055653d668723f4b840e4c0",
"0x14d01e64f0573925e28d69dc3846b2f0986ab8b8",
"0x280750ccb7554faec2079e8d8719515d6decdc84",
"0x0792fe820e7f65da788ac002ce88c74816b59142",
"0xdc14c317abf4fca7ac2255f0da73b39f63598c76",
"0x0343350a2b298370381cac03fe3c525c28600b21",
"0xb70b02222c53abf4e9ccac8fb701425db2ec4de1",
"0x200941b46e8cbb645fe85cdd526e48826acfd8fa",
"0x72649f2a739f2ed7454ca146fb9ba589747287f2", 
"0x1793bc201acbb64f3925ae5cb4355e78864a2597",
"0xbc77c9ae443940b8ca147870063ee2213264d8b6",
"0x5f2786097350e9d0a0cbba233774631991dc5e40",
"0xdfd55110016251c7537d7645f35f92afcfc468ed",
"0xa6002d6df526683b528f87f95b4903f3c76cb7de",
"0x9c9b95ed2123c3d7e8e7b65c7cd7b302bc26a13a"
]

ether1_all_coin_contract_addresses = [
"0xf69bc54fda5d2689a4d4fe8c1e6a5cbc25f6dc59",	#VOTE
"0x92e6c6eee2d4de4585ffe101e1e3288fb4e28330",	#KOT
"0xa888fbc3f9ca63776913d807804fc31c5ebda6d7",	#KOT
"0xc715e66000ceaee350c82c34b9b153c3c52f295b"	#BTC
]

egem_all_coin_contract_addresses = [
#"0xf3fe5bf46525577ca16980aecfacaf0a7a0e8970", 
#"0x037148f537e3e46db9ee7d71d050f0865fdc36df", #
#"0xd2fd37ef18910f6ed4fd7d60ab5179902a4a5e9b", #: 
#"0x954e6c333a6415a6ed3d5cf4057824b23a3a2cc2", #: AKE1",
#"0xd50537325faab2e09b6c5f2d2661e6e6d8273f1b", #: AKE1",
#"0xc302c5c09387f0584318048b02e8f80f09f20fc4", #: AKE1",
"0x5c87e1c5867365a41fc1deff56d4d554db38bd8c", #:
#"0xb0aad95e4ca0afdde25b936a0a9133d801a301f9", #:AKE1",
#"0x8288649dae790ae0326dc784685a531b9e7d32c0", #:AKE1",
"0x7b90ace6081e04eaa3595716c01c3a2bb8c93908", #: AKE1",
#"0x7784343f49be147516329d175098430f08da3d89", #: "EGEMSTAKE1",
#"0xd29c637d62bb056c2e85f9b146b0e87451008613", #: "EGEMSTAKE1",
#"0x3c6d158687718f24e9f0bd159c52b7c608d00b6b", #: "EGEMSTAKE1",
"0xaa2b129c8beb6ea9d974059f43659af22b1a41cb", # "POS",
#"0xba445f153c644ce5ab5519b23448b4d2721ba142", # "EGEMSTAKE1",
#"0xb779e74c3c2e07024d4dfb248db6736137f68fee", # "EGEMSTAKE1",
#"0x0842511951e520d7accc672175a173ffb1e179e4", # "EGEMSTAKE1",
#"0x16e46a65b6bef602f8ceebbf5e90c07692426174", # "EGEMSTAKE1",
#"0x526ce7efa21f81cbda54e7dbc5d35c3435a9bb31", # "EGEMSTAKE1",
#"0x3650dca09b5a77c2e6449e2b932dcc740fd48fff", # "EGEMSTAKE1",
#"0x56cca152f6f841aef3a6f91c8554f6acd0c99d40", # "EGEMSTAKE1",
#"0xe41de4267126ff64cf3930797193050995c6853d", # "EGEMSTAKE1",
#"0x656b956f72a7adedb4ed647794bfcdb98b6e78c6", # "EGEMSTAKE1",
#"0xa1f9bc6597127868ae4d1928cf3fc6bc99a2b35e", # "EGEMSTAKE1",
#"0x79092cce5250e614c2c8c693dff8e3f3b7c363bd", # "EGEMSTAKE1",
#"0x5eee439f0b831c13a91dd116848b0ac2cedacda4", # "EGEMSTAKE1",
#"0x51eb7be0282c8569cfc36b71b4adc4591daeafbd", # "EGEMSTAKE1",
#"0xea5e9e8aa6bb1c4270555c5088faa1f612307fe2", # "EGEMSTAKE1",
#"0xea3ba9a5c29c52f68f48e1802467eb717716a540", # "EGEMSTAKE1",
#"0x8b0d3fd518864f2b6bc0ac3c02fcaca1cc7bfdf8", # "EGEMSTAKE1",
#"0x2a8c595a44c3ba8ef13b8282b0b1f0867b87e60e", # "EGEMSTAKE1",
#"0x58590fa4edba0877c3134046574c8926f03b88a5", # "EGEMSTAKE1",
#"0xaa815a530d57a4f4d58ab32a47f3dd398120dd6d", # "EGEMSTAKE1",
#"0x0df501988859f93980feaa195d21673630ccc5e5", # "EGEMSTAKE1",
#"0x5ac20c706961c1aabb96bed54e6504f64dac6247", # "EGEMSTAKE1",
#"0x6a85842671e0c4ace2f55cc2fa7002241ad2f90a", # "EGEMSTAKE1",
#"0xcb644cccaddc48ce48187a9f18ee53a668b0d1e1", # "EGEMSTAKE1",
#"0x249c44be4fc1c60ab3e4130d249ef46034a108c0", # "EGEMSTAKE1",
#"0x7188b9ad51e3ede1d8b10aa76ff853586a0f26d1", # "EGEMSTAKE1",
#"0x684d61f586e007c249035d4116189e2698349fb0", # "EGEMSTAKE1",
#"0x7dc01bbb14873c85157474d26750a041bc48e057", # "EGEMSTAKE1",
#"0xaeb942ad9f9592cda563f01669d2480f82557b6b", # "EGEMSTAKE1",
#"0x23bf619dd30c7001f0a58ab8397e05d8ad4cde52", # "EGEMSTAKE1",
#"0x726221b7f0f35d66ed69626f4df34bf92c16ecef", # "EGEMSTAKE1",
#"0xb16854bbda067c57206b573bbe46ea64744e4902", # "EGEMSTAKE1",
#"0xe232ed00390fa77815d48eaf00cf6f0258bce748", # "EGEMSTAKE1",
#"0xa6777b27c5434deeb6decb90585007840e39af20", # "EGEMSTAKE1",
#"0xf36a920249fd57b0e30f906a10d648a2115a203e", # "EGEMSTAKE1",
#"0x733f9679699dcd15052dca32cdb163ab70015f94", # "EGEMSTAKE1",
#"0x3c7996073601dd96e238ac83a8d52a2c5cd2a126", # "EGEMSTAKE1",
#"0xe105bb16b9981eaeffd7e3c69a7dd448fad2c71d", # "EGEMSTAKE1",
#"0x62323482097f703adf70cf76a06318aed00a1cf9", # "EGEMSTAKE1",
#"0x08155500d93405684af906e18c8f1160e9fcf072", # "EGEMSTAKE1",
#"0xe92628b9b2b48b2ce5a48f791a3cc4ed74f904a1", # "EGEMSTAKE1",
#"0x8fef0e247f4498ddd42f8181f42354dcebcbadfd", # "EGEMSTAKE1",
#"0x432d7f45567122a68321ac7a552077bce88ef2e8", # "EGEMSTAKE1",
#"0x1fb637f5a596a54609c4278d45126b59ed94f771", # "EGEMSTAKE1",
#"0x9acd0c5bfeadef935dc2c403cd295cdb17e46ee8", # "EGEMSTAKE1",
#"0x3c01996be1cec5bff33f952762f172e80fe7bf52", # "EGEMSTAKE1",
#"0xe31f6117eb02ca2e34307e8bd0a1676414b0fab9", # "EGEMSTAKE1",
#"0x7105574be8da4c7e0b960055823a510943b84f81", # "EGEMSTAKE1",
#"0x94176d3083126095f2503168ddd7a264f6ad77ee", # "EGEMSTAKE1",
#"0x743e02a4ff7f959a81bf06356565d5401fa7727f", # "EGEMSTAKE1",
#"0xafff975ac7d09bb132a354b81edf233dbdf251cc", # "EGEMSTAKE1",
#"0x135397c1de46ba0e5d2ccef7808fe01df903c494", # "EGEMSTAKE1",
#"0xa415ef917e3a518908855101c093d5cdc82d79fb", # "EGEMSTAKE1",
#"0xf9584b4723af3c039044c63bd0a36d8e1cb35304", # "EGEMSTAKE1",
#"0x3b111fd7134c59994bcdc34f8f712cd01c1f1bba", # "EGEMSTAKE1",
#"0xcbffc19bb38cd8634c379f3515435df84fd0baeb", # "FIXED",
#"0x9bff190d807b64307298d42893be8ad541ecc2f9", # "EGEMSTAKE1",
"0xd13f1e4ba5a631cb0dc53cb31ff05218864f861e", # "JAL",
#"0x4468b3be5295a22f446f02af72545df367bc92b8", # "EGEMSTAKE1",
#"0xd0542f0f9053a9f1350cc303bff0823d665f75ee", # "FIXED",
"0xfaf62eece9be3ad9b56647606aa911b94428c286", # "EGT",
#"0x0bdf46a5628522479032146ea26aba33644d1ff4", # "EGEMSTAKE1",
#"0xcc78f87d9ddd139eaa414068f7289d7116974432", # "EGEMSTAKE1",
"0x659b22c4c44474495788b88bb6b02ab1fce977d1", # "FIXED",
#"0x75e3aead9d360b683d27fdd2f0d3fcac094ae70f", # "EGEMSTAKE1",
#"0xc682935c53498cecfecc5042b777efaa796b3b44", # "EGEMSTAKE1",
#"0xe4622e61f02ce1ca979f7cf7d619e1245fa707a7", # "EGEMSTAKE1",
#"0x775e0f5e295afadb747d4c893fbfc6b60cc644c3", # "EGEMSTAKE1",
#"0x85b21e03786b4975d7ecd9d4e0f8fd818d26d025", # "EGEMSTAKE1",
#"0xe174ec02bdc77a1ddcf6609d5f9727792a3bd0cd", # "EGEMSTAKE1",
#"0xaa9b8ce8d84a53880bd55980edff2aba94c44527", # "EGEMSTAKE1",
#"0xa24ef11765dec469a0e7b1b4b8af33000bcae208", # "EGEMSTAKE1",
#"0x1b0c1f3aceb98ef9fb7e1200298ca115d2c64081", # "EGEMSTAKE1",
#"0x08d0e9f2bf81ef79bb1aabbc78fbdc913063c138", # "EGEMSTAKE1",
#"0xf826d588d1d77fa0d5646b1dcb3a5e12ca250be3", # "EGEMSTAKE1",
#"0xb3714d90375b05ab271632aeb3afb9e55b5f0bd8", # "EGEMSTAKE1",
#"0xf034679b897dde1f8309b42f1de30bcb74ce7701", # "EGEMSTAKE1",
#"0xac6316e16e9b57940a96292d73bbe472e2c05e42", # "EGEMSTAKE1",
#"0x9359d55c315855b0e61ff29fe258fa318d871c66", # "EGEMSTAKE1",
#"0x83324f6bee616c15c43aa9805834012b9230e69a", # "EGEMSTAKE1",
#"0x7f51cb2f6480c78005a5de5c3459a27b35cbf7a0", # "EGEMSTAKE1",
#"0x6e98f58dc062773336af98038857ec50d9476850", # "EGEMSTAKE1",
#"0x9f56977c697db8dd4a6ff1efb079b476a3bbd5d0", # "EGEMSTAKE1",
#"0x35c98ccd701cf53fe0f2e203638dd5208785d49a", # "EGEMSTAKE1",
#"0x501564ef8a5ba9118bb928dc39ebce55377d8ee6", # "EGEMSTAKE1",
#"0x132648e5c20cb14c8ca1ba55c4f644bed88efe58", # "EGEMSTAKE1",
#"0x920683447785153c05cccf9c9daac572fe4cf031", # "EGEMSTAKE1",
#"0x3c50055c80c489b92aa16cfaf25e172ce16b7f58", # "EGEMSTAKE1",
#"0x63b4a9d5d3134761a43a81c70ea95896dfcce638", # "EGEMSTAKE1",
#"0x8054271ebab5972a8f009bdc31e259d696e5db42", # "EGEMSTAKE1",
#"0x4c50ca4f3eae66431e6316f5a77241741e09b5cb", # "EGEMSTAKE1",
#"0xf7f14972a2658acaa590cfea2c14a3e0c3e91013", # "EGEMSTAKE1",
#"0x3fb89cc4b96bdd60ba871a4dd13e28568d25babc", # "EGEMSTAKE1",
#"0xaa41283d896b60ebfa1ca41a14eb37b3f8b7b28a", # "EGEMSTAKE1",
#"0xaeaffec42e1bd69ce364af694f96abdd44c2d467", # "EGEMSTAKE1",
#"0x751b16ef91c2adb2d460bb8cd0ef807a481c02d6", # "EGEMSTAKE1",
#"0x2b3ac48c996b116be65d33b011be0d6148bd2bd1", # "EGEMSTAKE1",
#"0x52e720aad15effbd752e5f92918de17b36eb9f84", # "EGEMSTAKE1",
#"0x36af553cec8b9fa93edf8294469842f44fbcc0fc", # "EGEMSTAKE1",
#"0xb1c8d6087be456459021c7f27363babb4790aed9", # "EGEMSTAKE1",
#"0xd6d4650262a00c6dd400a6066a7c33d823bf1842", # "EGEMSTAKE1",
#"0xabcf9d5f757dab77b3abf545ba2579cb2b0eff20", # "EGT",
"0x07dbddf2ab49107e2dff52dd5e3034ab79b6672e", # "EGT",
#"0x2a3fbf1daadcadc7c4ceb98497d31a142c3a48b7", # "EGEMSTAKE1",
#"0x0e13576b5af685fcff32daab61caedea04bbfb8c", # "EGEMSTAKE1",
#"0x64733d74ef649a8ae79762268007b6594c020eaf", # "EGEMSTAKE1",
#"0xad0057514442d85927f4ef8bdb31f1dacd5221af", # "EGEMSTAKE1",
#"0xce35b3f8c963a6476689b11a56cb33b462c5271e", # "EGEMSTAKE1",
#"0xfd8a0e25821a90338c39d572baeeda278f57d38b", # "EGEMSTAKE1",
#"0x20fddc81b38c4d912764763d44a31fbb21de915f", # "EGEMSTAKE1",
#"0x3bef1ae112e407c9d3dbf85fac2caf5775df6b45", # "EGEMSTAKE1",
#"0x27a61f69a63a2efa88a1a17da4894e22d87a54fe", # "EGEMSTAKE1",
#"0x44755efe07ab91fffa55a76d72d90a891697efe6", # "EGEMSTAKE1",
#"0x9c62d97dd6e9dd88b56bec39a95fd178b5c99dc9", # "EGEMSTAKE1",
#"0x9db163aa4cc4f1d3717ebd4396573c8577575db5", # "EGEMSTAKE1",
#"0x3b8c270385c5267e2c7c94096385e9a7bdbee433", # "EGEMSTAKE1",
#"0xe25bf6b4714b1f17f2eefb0f28392e01c3a94c6f", # "EGEMSTAKE1",
#"0xf5750987363661d03d8c77d109a37f6bd000cc26", # "EGEMSTAKE1",
#"0x9b9c964ff8c066eb953b551b896cb8f7d6b32636", # "EGEMSTAKE1",
#"0x18b10dbeb6fd8f5823c800c364c4211edaceb1c2", # "EGEMSTAKE1",
#"0x8c74b5065f1c0b7e6586e4e6d115235746e6a6cb", # "EGEMSTAKE1",
#"0x752437d2a7c2d264b586093660ec4c38a7565d86", # "EGEMSTAKE1",
#"0x3a2686e8557c4b88a2fde000de6f61ca3b543f89", # "EGEMSTAKE1",
#"0xbbcfef3e2d9fafabc6c762980de9fd9cc040d13f", # "EGEMSTAKE1",
#"0xdfcf282648c54f7c87bce280584fb746ec60b391", # "EST",
#"0x7260b2b71f53a07dc4558b042b7004b9a10c7ede", # "EGEMSTAKE1",
#"0xe5f6f0579bf9f9343610e9f67e2f07d487543946", # "EST",
#"0x2e7e97c4a940dc475741250ab882a16e9f164060", # "EST",
#"0x254e663ff78ef451df01d743d33fdcd4ea97a1ad", # "EST",
#"0x70e0c1afccd65f5dcb9305ade401c6f051234ccc", # "EST",
#"0x7a0c1a435960c08d1159df78a02e383d315158fd", # "EST",
#"0x8d7ca347f5ba7ae849048519c20e045f2305a97d", # "EST",
#"0xec9870a1fdfb41459fc06a00a72beab9c440b4ea", # "EST",
#"0xd924e1cc8699d573d8aa80db37f4f5d690d433fa", # "EST",
#"0xb3edaab1f411277d9f1793b96902697fe1aaebe5", # "EST",
#"0x5c1bb93ba3cbc39e877785154b4760a6daf755e5", # "EST",
#"0xf51cf787d07faa8bf88598ec99ab6fdf6b9055d3", # "EST",
#"0x5a07c55054a5028d0c6c6cd3a3832373583228c3", # "EST",
#"0x4109ec64912d2232db058712869ed73fdd60ca61", # "EST",
#"0xc5514b0cc45a9aa37f21edaa44ea9fbf7725ba4c", # "EST",
#"0xad47f72d272006c1cbf1283b61dcaf931f25df4f", # "EST",
#"0x6afd8fe45942456b25c8a0a99642228f50f9d608", # "EST",
#"0xea0b75b0a6eaf0554ce61851bb9f1f3c471bb143", # "EST",
#"0xbfad1fef04d6079e8dce0ac1786b6c5ef665aa5c", # "EST",
#"0x209caf465786343fedf5bb4d2a5215943f3c207a", # "EST",
#"0x97f6e3599a44b5bd4cd4fee6357ddc21356b46a6", # "EST",
#"0x4244a461aa0f3ae8cdfd1e5c97a0d5125688471c", # "EST",
#"0x65ccb199843e9e392110cee5481da4de028ac197", # "EST",
#"0x5a8537509db6138916341807ae8f5caa423fe23b", # "EST",
#"0x16505b7e21a7e6673ce746e75ebf90b98107786b", # "EST",
#"0x5fcc0b98185caad33058b608aa8653e9e39adfe4", # "EST",
#"0x9f230efc0f77922cf44a8b7929a70ec4f5f168f3", # "EGT",
"0xc1d0d69aba63f8db63bbf41ee826fa1bb2053035", # "tyu",
#"0x072d097ae9cadae292fbac4dc25c25de8affadb6", # "EGT",
#"0xfff1a4d3cc13dd47b4c7dcfbc7b4bfd59fb4ca88", # "EGT",
#"0x6903c69fe03e3b6e285d630b378a822437a33f10", # "EGT",
#"0x42e08795b52c82883e6bcb134a6d154d8e23cdf6", # "ECT",
#"0xb6bd73e2afe9c610527731e65eb78e6349435d71", # "ECT",
#"0xcf7a713140c3d7d05059870fb9480e67d9fa4d9b", # "ECT",
"0x311b2b536667046c8a437742938c7f441d7023dd", # "DEMO",
#"0xf10945f86912e34c3f36a2b05026c187574afeb8", # "DX",
"0xd7d2f21774e5c1c3502678be869bb0323241b925", # "DX",
"0xa1c036a1b083dd9d9ea8427dca4c1d53f089be57", # "0xBTC",
"0x0c5106dc60033c5ac6ec3d504883c451265e7560", # "NDR",
"0x58d0a32a5680b2bf6364ca68ae181ce5fa4eaf57", # "ELLA",
"0xc1ff97815505c4331ad3d6c737a6d63cbab27b39", # "1337",
"0xd98f2112b41ca111a6265eac81b5497bbf1db9b0", # "SHIT",
"0xb85433c5719bb05fd4bad25fad734629c78fe512", # "SHT",
"0x79f9133098e0824e60ccd27b6fcaef07eb1b677c", # "NRGM",
#"0xb8489fbaa4e56858ba529f10667bd17333c6a0b5", # "VLDY",
"0xb0702df32de0371f39a98cc911a2dd69c3a13e6f", # "VLDY",
#"0x3dbdc750207ff7c9ca157c71ade6057aa32e3cc1", # "JILL",
#"0x2144aceaec70c0dcccc90fe8aff2ce9c983ab775", # "JILL",
#"0x59fe86c2878b5385015e413077e3f98e9e3a235a", # "ETTT",
"0x37a270f23a7bd7938465ffb7f90985ed0cdf13e5", # "DAPP",
#"0x1eab0ef3ee6b43feb94b73fa69a12bff98d0fdb6", # "ETTT",
#"0xb482d6d4e5623b51a0b923f8ebda63a420b3e74a", # "ETTT",
#"0x4fb1bc3e2613b159b1690cae662895256c609772", # "JILL",
"0x921ee2a83d104a772b148d775633df3df33efb87", # "JILL",
#"0xb7eafb3e1a191ffe6e21e5f5e0e262e46862cdb5", # "ETTT",
"0xb4eac2b9abaf776f7473ff745f452281f577c4b9", # "JACK",
#"0x076478959ab61d4d4c0371d7c0632aebd2c9654a", # "ETTT",
#"0xb3b3ac664dd96da1ca86a4dffbd627b6b773ff8c", # "ETTT",
#"0x5a67432e892eed079c26eaf307e281dc106c582b", # "ETTT",
#"0x82e00728095e4a99eddb6711714143e1aa94353b", # "ETTT",
#"0x435f699b6cc2338d65490a9f312af80b3c8247d0", # "ETTT",
#"0xfe05e1715a3ab7556f703a1e44e26cb18cc252b6", # "ETTT",
#"0x09925344416dca1112f6320c1e20af16688e6e3a", # "ETTT",
#"0xf20e2e9adf5124a4865eddbe0fa4e542862c956f", # "ETTT",
#"0x49a8e0798dde576325323a97292a194000d842ca", # "ETTT",
#"0xef975e9c43e95d04d20854cee705228ffb11fac6", # "ETTT",
#"0x7f866e285f0dfd8973432b32f58ba0d685f32252", # "ETTT",
#"0xaf8bd64cd7814d2df8e9be3943bde9b4c5d9d9fd", # "ETTT",
#"0xd1f2bd092f71d12d634a48ad13b939ec415a4239", # "ETTT",
#"0x0d9671daf93af25075d0ce2f508f1f26168863ec", # "ETTT",
#"0xd8efd8f9526c6787e8f2308776d180d7108e989e", # "ETTT",
#"0x176c6a5ca426c925e5cbc037554a5df8d7dab41e", # "ETTT",
#"0xd614c9eabf121dcf24e0e40aef4919358040f20d", # "ETTT",
#"0x651211ba04491e717ba3c0bd57e36f69d7b79315", # "ETTT",
#"0x97093d13503d3075c28c13ef41f080a1a11ec69b", # "ETTT",
#"0xc73eddf3e704f87461a8a6b05a4d14849ca1b0f6", # "ETTT",
#"0xa1bfc80eadf0f29a3b975ceedf7ce71217ca0bf4", # "ETTT",
#"0xbb6f1e9327f2e532a279bfb572e638a63ee0d3b1", # "ETTT",
#"0xb7ec829d70af236c41bc034112b026695a3f736a", # "ETTT",
#"0x6e2b7bdf8ed2026f27b75cf5d16a211899ef0989", # "ETTT",
#"0x864e8582d98cf20678ebb80cb12388e68475b7d7", # "ETTT",
#"0x7d437afcdf9d31c18014a2d6d61457e21d11f0cc", # "ETTT",
#"0xc1b2cd2d6dfee6c2b79540ca2c1916199265a927", # "ETTT",
#"0x9250af2a8fa661536426a27afabdfa2b5da8b87a", # "ETTT",
#"0xe79fd457c5234de79fccf29a709a6972f6269f6b", # "ETTT",
#"0xff6d5105e0b5b7b4cf0b04ff3bee997bbc1d1998", # "ETTT",
#"0x9a2343941b675222ed34e4f34c52cb49b24140b8", # "ETTT",
#"0x8696c9b72239a7e42cca93bd32a5ba253aa66580", # "ETTT",
#"0x48c34f68d911e4c82747f8fa9eb55ca6613dfb7a", # "ETTT",
#"0x77008d140686c2e4307001383e96190bbcb31a03", # "ETTT",
#"0x3ffba95461d5a4a742b40d39e70549a5ed282177", # "ETTT",
#"0x3b3f4fe00c80878dcc718a02afad9e713349f50e", # "ETTT",
"0x060174a7984e651afaa25f1e1a61051956603ed4" # "ETTT"
]
#

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
#---------------------END CONFIG----------------------------#
#############################################################
#CONNECTS TO MONGODB # USE CONFIG ABOVE TO ADJUST

def database():
	
	db 			= DataBaseName
	myclient 	= pymongo.MongoClient("mongodb://localhost:27017/")
	mydb 		= myclient[db]

	return mydb

def Onedatabase():

	db 			= OneDataBaseName
	myclient 	= pymongo.MongoClient("mongodb://localhost:27017/")
	mydb 		= myclient[db]

	return mydb


def Twodatabase():

	db 			= TwoDataBaseName
	myclient 	= pymongo.MongoClient("mongodb://localhost:27017/")
	mydb 		= myclient[db]

	return mydb

#############################################################
#CONVERTS NANOSECOND TIMESTAMP TO REAL TIME LOCAL TO CST

def timestamp(stamp):
			
			dt 						= datetime.fromtimestamp(stamp // 1000000000)
			s 						= dt.strftime('%Y-%m-%d %H:%M:%S')
			
			return s


def onetimestamp(stamp):
			
			dt 						= datetime.fromtimestamp(stamp)
			s 						= dt.strftime('%Y-%m-%d %H:%M:%S')
			
			return s

#############################################################
#CREATES WEB3 INSTANCE TO CONNECT TO 

def connect_geth():

	web3 = Web3(Web3.HTTPProvider(GethUrl))
	
	return web3

def one_connect_geth():

	web3 = Web3(Web3.HTTPProvider(OneGethUrl))
	
	return web3

def two_connect_geth():

	web3 = Web3(Web3.HTTPProvider(TwoGethUrl))
	
	return web3

#############################################################
#HEX TO DECIMAL CONVERSION 
def HexToDec(hex):
	

	x = 	str(int(hex, 16))
	
	return 	x


#############################################################
#DECIMAL TO HEX CONVERSION
def DecToHex(dec):

	x =		hex(int(dec))

	return x

#############################################################
#BREAKS UP THE INPUT AND PARSES IT BASED ON LENGTH 

def inputParse(input):
	
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

def rawParse(input):
	
	try:
		fields =  		int(len(input))
		fieldlenth = 	fields - 10
		fieldNumber = 	fieldlenth/64
		a = 			10 
		x = 			1
		list = 			[input[0:10]]

		while x <= fieldNumber:
			b = 		a + 64
			sector = 	input[a:b]
			a = 		b
			x = 		x + 1
			list.append(sector)

		return list		
	except:
		
		return "No Input"	
#############################################################
#RETURNS BLOCKNUMBER, TIME, BLOCK AVERAGES FOR THE STATS PAGE

def performance():

		
		mydb 		= database()
		myCol 		= mydb["blocks"]

		
		web3 = connect_geth()
		blockNumber2 = web3.eth.blockNumber  #BLOCKNUMBER RESULT
		blockNumber = blockNumber2
		previousBlockNumber = blockNumber - 5
		blockNumber = previousBlockNumber + 1
		averageBlock = blockNumber2 - 1000000

		for x in myCol.find({"number": int(blockNumber)}):
			blockNumber = x["timestamp"]

			for y in myCol.find({"number": previousBlockNumber}):
				previousBlockNumber = y["timestamp"]

				for z in myCol.find({"number": averageBlock}):
					averageBlock = z["timestamp"]
		


		average = blockNumber - averageBlock
		average = average / 1000000
		average = average / 1000000000
		blockTime = blockNumber - previousBlockNumber
		blockTime = blockTime / 1000000000
		times =  datetime.utcnow() 

		#ROUNDING

		performance={
			"BLOCKNUMBER":	blockNumber2,
			"TIME":			times,
			"BLOCKTIME":	blockTime,
			"AVERAGE":		average
		}

		return performance


def Oneperformance(): #ETHER1

		
		mydb 		= Onedatabase()
		myCol 		= mydb["blocks"]

		
		web3 = one_connect_geth()
		blockNumber2 = web3.eth.blockNumber  #BLOCKNUMBER RESULT
		blockNumber = blockNumber2
		previousBlockNumber = blockNumber - 5
		blockNumber = previousBlockNumber + 1
		averageBlock = blockNumber2 - 1000000

		for x in myCol.find({"number": int(blockNumber)}):
			blockNumber = x["timestamp"]

			for y in myCol.find({"number": previousBlockNumber}):
				previousBlockNumber = y["timestamp"]

				for z in myCol.find({"number": averageBlock}):
					averageBlock = z["timestamp"]
		


		average = blockNumber - averageBlock
		average = average #/ 1000000
		average = average #/ 1000000000
		blockTime = blockNumber - previousBlockNumber
		blockTime = blockTime #/ 1000000000
		times =  datetime.utcnow() 

		#ROUNDING

		performance={
			"BLOCKNUMBER":	blockNumber2,
			"TIME":			times,
			"BLOCKTIME":	blockTime,
			"AVERAGE":		average
		}

		return performance


def Twoperformance(): #ETHER1

		
		mydb 		= Twodatabase()
		myCol 		= mydb["blocks"]

		
		web3 = two_connect_geth()
		blockNumber2 = web3.eth.blockNumber  #BLOCKNUMBER RESULT
		blockNumber = blockNumber2
		previousBlockNumber = blockNumber - 5
		blockNumber = previousBlockNumber + 1
		averageBlock = blockNumber2 - 1000000

		for x in myCol.find({"number": int(blockNumber)}):
			blockNumber = x["timestamp"]

			for y in myCol.find({"number": previousBlockNumber}):
				previousBlockNumber = y["timestamp"]

				for z in myCol.find({"number": averageBlock}):
					averageBlock = z["timestamp"]
		


		average = blockNumber - averageBlock
		average = average #/ 1000000
		average = average #/ 1000000000
		blockTime = blockNumber - previousBlockNumber
		blockTime = blockTime #/ 1000000000
		times =  datetime.utcnow() 

		#ROUNDING

		performance={
			"BLOCKNUMBER":	blockNumber2,
			"TIME":			times,
			"BLOCKTIME":	blockTime,
			"AVERAGE":		average
		}

		return performance


#############################################################
# SEND IN AN ADDRESS AND IT RETURNS MASTERNODE RESULTS OR A TOTAL OF "NO MASTERNODES"

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

#############################################################
#RETURNS THE LAST PAYOUT IN HUMAN TIME CST

def payout():

		try:

			myCol 		= database()["transactions"]
			list 		= []
			

			for x in myCol.find({"to_address": "0xc660934ec084698e373ac844ce29cf27b104f696"}).limit(1000).sort('block_number', pymongo.DESCENDING):
				
				payout_input = str(x["input"][0:10])

				if payout_input == "0xdf6c39fb":
					list.append(x["block_timestamp"])

					payout = list[0]
					payout = timestamp(payout)

			return payout

		except:

			payout = "No Data"

			return payout
	

#############################################################
#WHEN THE SEARCH BAR IS ACTIVATED THIS WILL DETERMINE WHETHER ITS AN ADDRESS, BLOCK OR HASH
def query(search):

	search = str(search)
	error = None

	if len(search) == 42:
		search = "/HALO/balance/{}".format(search) # is this an address?
		return search

	if len(search) == 66:
		search = "/HALO/tx/{}".format(search)#is this a transaction?
		return search

	if len(search) <= 8:
		try:
		   val = int(search)
		   search = "/HALO/block/{}".format(search)# is this a block number / invalid at block 100000000 Y2K
		   return search

		except ValueError:
		   return error

#WHEN THE SEARCH BAR IS ACTIVATED THIS WILL DETERMINE WHETHER ITS AN ADDRESS, BLOCK OR HASH
def Onequery(search):

	search = str(search)
	error = None

	if len(search) == 42:
		search = "/ETHER1/balance/{}".format(search) # is this an address?
		return search

	if len(search) == 66:
		search = "/ETHER1/tx/{}".format(search)#is this a transaction?
		return search

	if len(search) <= 8:
		try:
		   val = int(search)
		   search = "/ETHER1/block/{}".format(search)# is this a block number / invalid at block 100000000 Y2K
		   return search

		except ValueError:
		   return error

def Twoquery(search):

	search = str(search)
	error = None

	if len(search) == 42:
		search = "/EGEM/balance/{}".format(search) # is this an address?
		return search

	if len(search) == 66:
		search = "/EGEM/tx/{}".format(search)#is this a transaction?
		return search

	if len(search) <= 8:
		try:
		   val = int(search)
		   search = "/EGEM/block/{}".format(search)# is this a block number / invalid at block 100000000 Y2K
		   return search

		except ValueError:
		   return error

##############################################################
#LOADS CONTRACT BALANCES FOR EACH ITEM IN contract_address PULLS BALANCE

def balanceInfo(personal_address):
    results = {}
    abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]')
    web3 = connect_geth()
    account_checksum = Web3.toChecksumAddress(personal_address)
    balance = web3.eth.getBalance(account_checksum)
    halo3 = web3.fromWei(balance, "ether")
    results.update( {"HALO": halo3} )

    for i in all_coin_contract_addresses:
        address = Web3.toChecksumAddress(i)
        user_clean = Web3.toChecksumAddress(personal_address)
        contract = web3.eth.contract(address=address, abi=abi)
        symbol = contract.functions.symbol().call()
        balance = contract.functions.balanceOf(user_clean).call()
        balance = web3.fromWei(balance,"ether")
        decimals = contract.functions.decimals().call()

        if decimals == 8 and balance != 0 :
            btc_balance = balance * 100000000
            balance = '{0:.20f}'.format(balance).rstrip('0').rstrip('.')
            results.update( {symbol : btc_balance} )
        
        
        if balance != 0:
            results.update( {symbol : balance} )


    return results


#LOADS CONTRACT BALANCES FOR EACH ITEM IN contract_address PULLS BALANCE #ETHER1

def OnebalanceInfo(personal_address):
    results = {}
    abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]')
    web3 = one_connect_geth()
    account_checksum = Web3.toChecksumAddress(personal_address)
    balance = web3.eth.getBalance(account_checksum)
    halo3 = web3.fromWei(balance, "ether")
    results.update( {"ETHO": halo3} )

    for i in ether1_all_coin_contract_addresses:
        address = Web3.toChecksumAddress(i)
        user_clean = Web3.toChecksumAddress(personal_address)
        contract = web3.eth.contract(address=address, abi=abi)
        symbol = contract.functions.symbol().call()
        balance = contract.functions.balanceOf(user_clean).call()
        balance = web3.fromWei(balance,"ether")
        decimals = contract.functions.decimals().call()

        if decimals == 8 and balance != 0 :
            btc_balance = balance * 100000000
            balance = '{0:.20f}'.format(balance).rstrip('0').rstrip('.')
            results.update( {symbol : btc_balance} )
        
        
        if balance != 0:
            results.update( {symbol : balance} )


    return results


def TwobalanceInfo(personal_address): #EGEM EtherGem


	results = {}
	abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]')
	web3 = two_connect_geth()
	account_checksum = Web3.toChecksumAddress(personal_address)
	balance = web3.eth.getBalance(account_checksum)
	halo3 = web3.fromWei(balance, "ether")
	results.update( {"EGEM": halo3} )


	for i in egem_all_coin_contract_addresses :
		try:
			address = Web3.toChecksumAddress(i)
			user_clean = Web3.toChecksumAddress(personal_address)
			contract = web3.eth.contract(address=address, abi=abi)
			symbol = contract.functions.symbol().call()
			balance = contract.functions.balanceOf(user_clean).call()
			balance = web3.fromWei(balance,"ether")
			decimals = contract.functions.decimals().call()

			if decimals == 8 and symbol != "1337" and balance != 0 :
				btc_balance = balance * 100000000
				balance = '{0:.20f}'.format(balance).rstrip('0').rstrip('.')
				results.update( {symbol : btc_balance} )

			if symbol == "1337" and balance != 0 :
				balance = balance * 100000000000
				balance = '{0:.20f}'.format(balance).rstrip('0').rstrip('.')
				results.update( {symbol : balance} )


			if balance != 0:
				results.update( {symbol : balance} )
		except:
			pass

	results.update( {"EGEM": halo3} )	
	return results



##############################################################
#LOADS CONTRACT BALANCES FOR EACH ITEM IN contract_address PULLS BALANCE
def blockResults(id):
	
	mydb 		= 	database()
	myCol 		= 	mydb["blocks"]
	myCol2 		=	mydb["transactions"]
	
	try:
		for x in myCol.find({"number" : id}):
			for y in myCol2.find({"block_hash" : x["hash"] }):
				x.update(y)
			return x
	except:
		return None

def OneblockResults(id):
	
	mydb 		= 	Onedatabase()
	myCol 		= 	mydb["blocks"]
	myCol2 		=	mydb["transactions"]
	
	try:
		for x in myCol.find({"number" : id}):
			for y in myCol2.find({"block_hash" : x["hash"] }):
				x.update(y)
			return x
	except:
		return None

def TwoblockResults(id):
	
	mydb 		= 	Twodatabase()
	myCol 		= 	mydb["blocks"]
	myCol2 		=	mydb["transactions"]
	
	try:
		for x in myCol.find({"number" : id}):
			for y in myCol2.find({"block_hash" : x["hash"] }):
				x.update(y)
			return x
	except:
		return None


##############################################################
##############################################################
#THIS IS SHIT!!!! I HATE IT, NEEDS TO CHANGE
def getType(inpoot):

	answer = inputParse(inpoot)
	
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

##############################################################
#PULLS TRANSACTION DATA FOR TRANSACTIONS.HTML

def transResults(id):
	
	myCol		=	database()["transactions"]
	
	try:
		for x in myCol.find({"hash" : id}):
			
			x["block_timestamp"] 	= timestamp(x["block_timestamp"])
			x["value"]				= '{0:.20f}'.format(x["value"] / 1000000000000000000 ).rstrip('0').rstrip('.')

			return x
	except:
		return None

def OnetransResults(id):
	
	myCol		=	Onedatabase()["transactions"]
	
	try:
		for x in myCol.find({"hash" : id}):
			
			x["block_timestamp"] 	= onetimestamp(x["block_timestamp"])
			x["value"]				= '{0:.20f}'.format(x["value"] / 1000000000000000000 ).rstrip('0').rstrip('.')

			return x
	except:
		return None
