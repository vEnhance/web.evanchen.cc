def hlink(name, filename=None):
	filename = filename or name
	return '<a href="handouts/%s/%s.pdf">(pdf)</a> <a href="handouts/%s/%s.tex">(tex)</a><br>' %(name, filename, name, filename)
