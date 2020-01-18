def Query(search):

	search = str(search)

	error = None

	if len(search) == 42:
		search = "https://www.haloexplorer.com/balance/{}".format(search)
		return search
	if len(search) == 66:
		search = "https://www.haloexplorer.com/tx/{}".format(search)
		return search
	if len(search) <= 8:
		try:
		   val = int(search)
		   search = "https://www.haloexplorer.com/block/{}".format(search)
		   return search
		except ValueError:
		   return error