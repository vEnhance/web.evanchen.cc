import csv
from git import Repo
from pathlib import Path
import datetime
import os

repo = Repo(Path(__file__).parent, search_parent_directories = True)
tree = repo.heads.main.commit.tree

GITHUB_BASE = 'https://github.com/vEnhance/web.evanchen.cc' # /commit/cc6b6aeac80981bc84077ba1f303784150c141d8

def handout_link(name, filename=None):
	filename = filename or name
	return '<a href="handouts/%s/%s.pdf">(pdf)</a> '\
			'<a href="handouts/%s/%s.tex">(tex)</a><br>' %(name, filename, name, filename)

def page_footer(page) -> str:
	input_name : str = page['url'].replace('.html', '.mkd')
	input_path = Path('input') / input_name
	try:
		blob = tree[str(input_path)]
	except:
		return '<div class="text-muted">View the <a href="{GITHUB_BASE}">source repository</a>.</div>' \
				'<div class="font-italic text-muted">This hidden page not under public version control.</div>'
	else:
		commit = next(repo.iter_commits(paths=blob.path, max_count=1))
		last_update_dt = datetime.datetime. utcfromtimestamp(commit.committed_date)
		last_update_str = last_update_dt.strftime('%a %-d %b %Y, %H:%M:%S UTC')
		return \
				f'<div>' \
				f'<a href="{GITHUB_BASE}">Source repository (git)</a> &bullet; ' \
				f'<a href="{GITHUB_BASE}/commits/main/{input_path}">Revision history</a> &bullet; ' \
				f'<a href="{GITHUB_BASE}/edit/main/{input_path}">Suggest edit</a>' \
				f'</div>' \
				f'<div class="text-muted">Updated {last_update_str} by ' \
				f'<a href="{GITHUB_BASE}/commit/{commit.hexsha}"><code>{commit.hexsha[0:12]}</code></a>' \
				f'</div>'


def get_twitch_table():
	tsv_path = os.path.expanduser("~/ProGamer/Writeups/data.tsv")
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
		filename = os.path.join(os.path.expanduser("~"), "youtube-tex", basename_tex)

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

def tshirt(year, alt = None, ext = '.png'):
	location = f'static/mop/shirts/{year}{ext}'
	if alt is None:
		alt = f'{year}.'
	return f'<a href="{location}" title="{alt}" class="tshirt-link">'\
			f'<img src="{location}" alt="{alt}" class="tshirt" /></a>'
