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
	out += r'<tr><th>Episode No.</th><th>Write-up</th><th>Youtube</th></tr>' + '\n'

	for row in data:
		n = row['N']
		key = row['Source']
		fail = row['Fail']
		youtube = row['YouTube']

		basename = "Ep%03d" %int(n) + "-" \
				+ key.replace(" ", "-").replace("/", "-").replace(".", "-") \
				+ '-Solution' + '.pdf'
		filename = os.path.join(os.path.expanduser("~"), "youtube-tex", basename)

		if fail:
			continue

		out += '<tr>'
		out += '<td>Ep. %s</td>' % n
		if os.path.exists(filename):
			out += '<td><a href="twitch/%s">%s</a></td>' %(basename, key)
		else:
			out += '<td>%s</td>' % key
		if youtube:
			out += '<td><a href="%s">(youtube)</a></td>' % youtube
		else:
			out += '<td></td>'
		out += '</tr>' + '\n'
	out += '</table>'

	return out
