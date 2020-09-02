import os
import csv

def hlink(name, filename=None):
	filename = filename or name
	return '<a href="handouts/%s/%s.pdf">(pdf)</a> <a href="handouts/%s/%s.tex">(tex)</a><br>' %(name, filename, name, filename)

def get_twitch_table():
	tsv_path = os.path.expanduser("~/Dropbox/Twitch/Writeups/data.tsv")
	data = []
	with open(tsv_path) as f:
		reader = csv.DictReader(f, delimiter='\t')
		for row in reader:
			data.append(row)

	data.sort(key = lambda row: (-int(row['N']), row['Source']))

	out = ''
	out += r'<table cellpadding="5">' + '\n'
	out += r'<tr><th>Episode</th><th>Problem</th><th>PDF</th><th>TeX</th><th>YouTube</th></tr>' + '\n'

	for row in data:
		n = row['N']
		key = row['Source']
		fail = row['Fail']
		youtube = row['YouTube']

		basename = "Ep%03d" %int(n) + "-" \
				+ key.replace(" ", "-").replace("/", "-").replace(".", "-") \
				+ '-Solution'
		basename_tex = basename + '.tex'
		basename_pdf = basename + '.pdf'
		filename = os.path.join(os.path.expanduser("~"), "youtube-tex", basename_pdf)

		if fail:
			continue

		out += '<tr>'
		out += '<td>Ep. %s</td>' % n
		out += '<td>%s</td>' % key
		if os.path.exists(filename):
			out += '<td><a href="twitch/%s">(pdf)</a></td>' % basename_pdf
			out += '<td><a href="twitch/%s">(tex)</a></td>' % basename_tex
		else:
			out += '<td></td>' * 2
		if youtube:
			out += '<td><a href="%s">(youtube)</a></td>' % youtube
		else:
			out += '<td></td>'
		out += '</tr>' + '\n'
	out += '</table>'

	return out
