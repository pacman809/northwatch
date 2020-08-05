#!/bin/bash
#****************************************************************************************

#Ethereumetl Copyright (c) 2018 Evgeny Medvedev, evge.medvedev@gmail.com, https://twitter.com/EvgeMedvedev

#Copyright (c) 2019 Garth Madden, Email = Garthmadden809@gmail.com

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

#****************************************************************************************



#UHASH DB TO USE---------------------------------

directory=$(pwd)
#------------------------------------------------
#echo $directory
#currentdir=$(pwd)
counter=1

while [ $counter -le 20000000 ]
do
	cd $directory		
	startblock=$(cat lastblock.log) #gets the last block downloaded
	connected=$(./connected.py)
	endblock=$(./blocknumber.py) #gets current Block number
	
	echo $startblock
	echo $endblock
	
	
	if [ "$connected" == "True" ] ; 
		echo
		echo "phase 2"
		then
		   	echo
			echo 'Connection to Web3 Passed'
			mkdir database

			#--------------------------------------------------------------------------------
			# Unhash The Instance You Want To Use. Or Create YouR Own Following The Template
			#--------------------------------------------------------------------------------

			#/home/pacman/environments/py_3.7/bin/ethereumetl export_all -s $startblock -e $startblock -b 10000000 --provider-uri http://192.168.1.231:8545 -o halo-mainnet-csv 
			#/home/pacman/environmnets/py_3.7/bin/ethereumetl export_all --start-block $endblock --end-block $endblock --provider-uri http://mainnet.haloplatform.tech 
			/home/garth/.local/bin/ethereumetl  export_all -s $startblock -e $endblock  -b 1000000 --provider-uri http://192.168.0.58:8545 -o database
			#/home/pacman/environments/py_3.7/bin/ethereumetl export_all -s $startblock -e $endblock -b 10000000 --provider-uri http://mainnet.haloplatform.tech -o halo-mainnet-csv
			
			#--------------------------------------------------------------------------------


			cd database
			echo $directory
			find . -name *.csv -exec mv '{}' "$directory/CSV/" ";"
			cd $directory
			cd $directory/CSV
			echo $endblock
			echo $startblock
			echo transactions_$startblock\_$endblock.csv
			echo 
			echo
			echo Importing Transaction
			find -name '*transactions*'  -exec mv {} transactions.csv \;
			/usr/bin/mongoimport  -d halo-explorer-mainnet -c transactions --type csv --headerline --file transactions.csv ;
			echo
			echo Exporting Transaction to Remote
			echo 
			echo Importing Temporary Files
			/usr/bin/mongoimport  -d halo-explorer-mainnet -c temp --type csv --headerline --file transactions.csv ;
			echo 
			echo Importing Blocks
			find -name '*blocks*'  -exec mv {} blocks.csv \;
			/usr/bin/mongoimport  -d halo-explorer-mainnet -c blocks --type csv --headerline --file blocks.csv ;
			echo
			echo Importing Token Transfers
			find -name '*token_transfers*'  -exec mv {} tokentransfers.csv \;
			/usr/bin/mongoimport  -d halo-explorer-mainnet -c token_transfers --type csv --headerline --file tokentransfers.csv ;
			echo
			echo Importing Tokens
			find -name '*tokens*'  -exec mv {} tokens.csv \;
			/usr/bin/mongoimport  -d halo-explorer-mainnet -c tokens --type csv --headerline --file tokens.csv ;
			echo
			echo Importing Logs
			find -name '*logs*'  -exec mv {} logs.csv \;
			/usr/bin/mongoimport  -d halo-explorer-mainnet -c logs --type csv --headerline --file logs.csv ;
			echo
			echo Importing Contracts
			find -name '*contracts*'  -exec mv {} contracts.csv \;
			/usr/bin/mongoimport  -d halo-explorer-mainnet -c contracts --type csv --headerline --file contracts.csv ;
			echo
			echo Importing Receipts
			find -name '*receipts*'  -exec mv {} receipts.csv \;
			/usr/bin/mongoimport  -d halo-explorer-mainnet -c receipts --type csv --headerline --file receipts.csv
			echo 
			echo 

			rm *.csv
			
			echo ENDBLOCK is $endblock
			placeholder=$(($endblock + 1))
			echo Placeholder is equal to $placeholder
			echo $placeholder > $directory/lastblock.log
			cd $directory
			testblock=$(./blocknumber.py)
			echo 
			echo
			echo $testblock $blocknumber
			echo
			echo
			cd $directory
			echo 
			echo 
			
			./func.py
			./PopulateEthDeposit.py
		
			echo 
			echo

			rm -r database


			while [[ $testblock == $endblock ]] 
			do
				echo Current Block = $testblock
				echo Waiting 1 second
				sleep 1
				testblock=$(./blocknumber.py)
			done

			((counter++))
			echo
			echo Moving On to The Next Block
			echo 
	fi

done

echo 1M Cycles Completed Please Check Blocks For Accuracy And Restart Syncer.
