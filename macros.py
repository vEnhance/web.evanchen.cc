import os
import csv

def handout_link(name, filename=None):
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
		youtube = row['YouTube']

		basename = "Ep%03d" %int(n) + "-" \
				+ key.replace(" ", "-").replace("/", "-").replace(".", "-") \
				+ '-Solution'
		basename_tex = basename + '.tex'
		basename_pdf = basename + '.pdf'
		filename = os.path.join(os.path.expanduser("~"), "youtube-tex", basename_pdf)

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


def get_card_trick():
	option_string = r'''<option value="{value}">{value}</option>'''
	ranks = ["...", "Ace", "2", "3", "4", "5", "6",
			"7", "8", "9", "10", "Jack", "Queen", "King"]
	suits = ["...", "♣Clubs", "♦Diamonds", "♥Hearts", "♠Spades"]
	out = ''
	for n in range(0,4):
		out += f'<h2>Card {n+1}</h2>' + '\n'
		out += r'<div class="container trick-container">' + '\n'
		out += f'<select class="form-select rank-select" id="rank-{n}">' + '\n'
		for r in ranks:
			out += option_string.format(type='rank', name=n, value=r) + '\n'
		out += r'</select>' + '\n'
		out += f'<select class="form-select suit-select" id="suit-{n}">' + '\n'
		for s in suits:
			out += option_string.format(type='suit', name=n, value=s) + '\n'
		out += r'</select>' + '\n'
		out += r'</div>' + '\n'
		out += r'<hr />' + '\n'
			
	out += r'<h2>Card 5</h2>' + '\n'
	out += r'<h1 id="answer">...</h1>' + '\n'
	out += r'<button type="button" class="btn" id="trick-button"></button>' + '\n'
	out += r'<script type="text/javascript" src="/static/trick.min.js"></script>' + '\n'
	out += r'<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/js/select2.min.js"></script>' + '\n'
	out += r'<link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/css/select2.min.css" />'
	return out

def faq(label, question):
	return f'<a id="{label}" href="#{label}" style="color:#004824;">{label}.</a> {question}' \
		f'<a href="#{label}" class="hash-link">#</a>'

def hl(link, text):
	return f'<a id="{link}"></a>{text}<a href="#{link}" class="hash-link">#</a>'

def tshirt(year, ext = 'png'):
	location = f'static/mop/shirts/{year}.{ext}'
	return f'<a href="{location}" class="tshirt-link"><img src="{location}" class="tshirt" /></a>'

