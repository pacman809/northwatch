def Query(search):

	search = str(search)
	error = None

	if len(search) == 42:
		search = "https://www.haloexplorer.com/balance/{}".format(search) # is this an address?
		return search

	if len(search) == 66:
		search = "https://www.haloexplorer.com/tx/{}".format(search)#is this a transaction?
		return search

	if len(search) <= 8:
		try:
		   val = int(search)
		   search = "https://www.haloexplorer.com/block/{}".format(search)# is this a block number / invalid at block 100000000 Y2K
		   return search

		except ValueError:
		   return error