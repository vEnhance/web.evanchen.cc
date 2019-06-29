import yaml
import heapq

# Script constants
BASE = r"http://web.evanchen.cc/elmo/"
# BASE = r"file:///home/evan/Dropbox/Documents/www/elmo/"
YEAR_PREV = 2019
YEAR_NEXT = 2020
YEARS = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
PREV_URL = "https://aops.com/community/c5h1838663s1_21st_elmo_2019"
NEXT_URL = "https://www.nyan.cat"

# Create header {{{1
with open("static/header.html") as f:
	HEADER = ''.join(f.readlines())
with open("static/footer.html") as f:
	FOOTER = ''.join(f.readlines())

HEADER = HEADER.format(base = BASE, prev_url=PREV_URL, prev_year=YEAR_PREV,
		next_url=NEXT_URL, next_year=YEAR_PREV+1)
FOOTER = FOOTER

# Create index page
with open("static/homepage.html") as f:
	index_html = HEADER + ''.join(f.readlines()) + FOOTER
index_html = index_html.replace("<script", r'<link href="css/index.css" rel="stylesheet" type="text/css">' + '\n<script', 1)
# lol injects extra index CSS into specifically homepage only

# Change the header elsewhere
with open("static/sidebar.html") as f:
	HEADER += ''.join(f.readlines())

with open("index.html", "w") as f:
	print(index_html, file=f)

# }}}

def link(obj, text):
	return r'<a href="{}">{}</a>'.format(obj.url, text)

class Student:
	def __init__(self, student_string):
		self.name, score_string = student_string.strip().split(',')
		self.name = self.name.strip()
		self.scores = [int(digit) for digit in score_string.strip()]
		self.score = sum(self.scores)
class ELMOStudent(Student):
	@property
	def code(self): return "{}{}".format(self.country.code, self.number)
	@property
	def pcode(self): return link(self.country, self.code)
class AoPSStudent(Student):
	pass

class ELMOCountry:
	def __init__(self, **kwargs):
		for key in kwargs: setattr(self, key, kwargs[key])
	def __len__(self):
		return len(self.students)
	@property
	def total(self):
		return sum([student.score for student in self.students])
	@property
	def sweeps(self):
		if self.year.year_num >= 2018:
			return sum(heapq.nlargest(4,[student.score for student in self.students])) / 4.0
		elif self.year.year_num == 2017:
			return sum(heapq.nlargest(3,[student.score for student in self.students])) / 3.0
		else:
			return sum([student.score for student in self.students]) / float(len(self.students))
	@property
	def scores(self): return [sum([s.scores[i] for s in self.students])\
			for i in range(self.year.num_problems)]
	@property
	def awards(self):
		sorted_students = sorted(self.students, key = lambda s : s.rank)
		return ','.join([s.medal[0] for s in sorted_students if s.medal != ""])
	@property
	def url(self): return "countries/{}_{}.html".format(self.year.year_num, self.code)
	@property
	def pname(self): return link(self, self.name)
	@property
	def pcode(self): return link(self, self.code)


class ELMOYear:
	has_aops = False
	def __init__(self, **kwargs):
		for key in kwargs: setattr(self, key, kwargs[key])
		self.countries = []
		if "num_problems" not in kwargs:
			self.num_problems = 6
		self.problem_headers = ''.join([\
				"<th>P{}</th>".format(i) for i in range(1,self.num_problems+1)]) 
	@property
	def url(self): return "results/{}.html".format(self.year_num)
	@property
	def pyear(self): return link(self, self.year_num)
	@property
	def pname(self): return link(self, self.name)
	@property
	def pnum(self):
		n = self.num
		return str(n) + "<sup>" + {1:"st", 2:"nd", 3:"rd"}.get(n%10, "th") + "</sup>"
	def get_problem_scores(self, i):
		ret = []
		for country in self.countries:
			for student in country.students:
				ret.append(student.scores[i])
		return ret
# Statistics
def stat_avg(S):
	return sum(S) / float(len(S))
def stat_stddev(S):
	mu = stat_avg(S)
	return stat_avg([(s-mu)**2 for s in S])**0.5

# For each year, load data {{{1
ELMO = []
def inplace_rank(students):
	# Rank and medal students
	students.sort(key = lambda s : -s.score)
	rank, prev = 0, -1
	for i, student in enumerate(students):
		if student.score != prev: rank, prev = i+1, student.score # tiebreaking
		student.rank = rank # give ranks
		# award medals
		for medal_type, medal_cutoff in year.cutoffs.items():
			if student.score >= medal_cutoff:
				student.medal = medal_type
				break
		else: # no medal
			student.name = "" # make students who don't medal anon
			student.medal = ""

for year_num in YEARS:
	filename = "internal/{}.yaml".format(year_num)
	with open(filename, 'r') as f:
		data = list(yaml.load_all(f, Loader=yaml.FullLoader))
	country_dicts = data[1:] # all the docs after first have students
	year = ELMOYear(**data[0]) # create a year with properties
	year.year_num = year_num # year_num will always be an int
	# Generate the countries
	students = []
	aopsers = []
	for country_dict in country_dicts:
		if type(country_dict) == type({}): # Ordinary ELMO country
			country_dict['year'] = year
			this_country_obj = ELMOCountry(**country_dict)
			# Convert the list of strings into a list of Student objects
			this_country_students = []
			i = 0
			for student_string in country_dict['members']:
				i += 1
				student = ELMOStudent(student_string)
				student.country = this_country_obj
				student.year = year
				student.number = i
				students.append(student) # for sorting later
				this_country_students.append(student)
			this_country_obj.students = this_country_students
			year.countries.append(this_country_obj)
		elif type(country_dict) == type([]):
			# Special AoPS "country", just list of scores
			for student_string in country_dict:
				student = AoPSStudent(student_string)
				aopsers.append(student)
			inplace_rank(aopsers)
			year.has_aops = True
	inplace_rank(students)
	year.students = students
	year.aopsers = aopsers

	# Rank countries
	rank, prev = 0, -1
	year.countries.sort(key = lambda c : -c.sweeps)
	for i, country in enumerate(year.countries):
		if country.sweeps != prev: rank, prev = i+1, country.sweeps # tiebreaking
		country.rank = rank # give ranks

	ELMO.append(year)
# }}}

# Index pages {{{1
page_start = r'''
<div id="main">
<h2>{title}</h2>
<script>$(function() {{ $("#table_main").tablesorter({{ sortList: {howsort} }}); }} ); </script>
<table id="table_main" class="tablesorter">
{row}
<tbody>'''

with open("timeline/index.html", "w") as f:
	print(HEADER, file=f)
	print(page_start.format(title="Timeline", howsort="[[0,-1]]",
		row=r'<thead><tr><th>#</th><th>Year</th><th>Contest</th><th>Dates</th></thead>'), file=f)
	for year in ELMO:
		row = r'<tr><td>{y.num}</td><td>{y.pyear}</td><td>{y.pname}</td><td>{y.dates}</td></tr>'
		print(row.format(y=year), file=f)
	print("</tbody></table>", file=f)
	print(FOOTER, file=f)

with open("countries/index.html", "w") as f:
	print(HEADER, file=f)
	print(page_start.format(title="Countries", howsort="[[0,-1]]",
		row=r'<thead><tr><th>Year</th><th>Country</th><th>Leaders</th><th>Rank</th><th>Awards</th></thead>'), file=f)
	for year in ELMO:
		for country in year.countries:
			row = r'<tr><td>{c.year.pyear}</td><td>{c.pname}</td><td>{c.leaders}</td><td>{c.rank}</td><td>{c.awards}</td></tr>'
			print(row.format(c=country), file=f)
	print("</tbody></table>", file=f)
	print(FOOTER, file=f)

with open("results/index.html", "w") as f:
	print(HEADER, file=f)
	print(page_start.format(title="Results", howsort="[[0,1]]",
		row=r'<thead><tr><th>Year</th><th>Country</th><th>Name</th><th>Rank</th><th>Award</th></thead>'), file=f)
	for year in ELMO:
		for student in year.students:
			if student.name == "": continue
			row = r'<tr><td>{s.year.pyear}</td><td>{s.pcode}</td><td>{s.name}</td><td>{s.rank}</td><td>{s.medal}</td></tr>'
			print(row.format(s = student), file=f)
	print("</tbody></table>", file=f)
	print(FOOTER, file=f)
#}}}

# Per-year page {{{1
for year in ELMO:
	result_header = r'''
	<div id="main">
	<h2><a class="pointer" href="results/{M}.html">&#9664;</a>&nbsp;&bull;&nbsp;
	<a class="highlight" href="results/{y.year_num}.html">{y.pnum} ELMO {y.year_num}</a>&nbsp;&bull;&nbsp;
	<a class="pointer" href="results/{N}.html">&#9654;</a></h2>
	<h3><a href="results/{y.year_num}.html">{y.name}</a></h3>
	<h3 class="hideprn">
	<a href="results/{y.year_num}_countries.html">Country Results</a>
	&nbsp;&bull;&nbsp;
	<a href="results/{y.year_num}_indvs.html">Individual Results</a>
	&nbsp;&bull;&nbsp;
	<a href="results/{y.year_num}_stats.html">Statistics</a>
	'''
	if year.has_aops:
		result_header += '&nbsp;&bull;&nbsp;\n<a href="results/{y.year_num}_guest.html">Guest Participants</a>\n'
	result_header += '</h3>\n\n'
	result_header = result_header.format(y = year, M = year.year_num-1, N = year.year_num+1)


	with open(year.url, "w") as f:
		print(HEADER, file=f)
		print(result_header, file=f)

		top_country = year.countries[0]
		top_score = year.students[0].score
		top_students = ', '.join([link(s.country, s.name) \
				for s in year.students if s.score == top_score])
		print(r'<h4>Top Team: {c.pname} ({c.pcode})</h4>'.format(c = top_country), file=f)
		print(r'<h4>Top Contestant:  {}</h4>'.format(top_students), file=f)
		print("<h4>Medal Cutoffs</h4>", file=f)
		print("<ul>", file=f)
		for medal, thresh in year.cutoffs.items():
			print("<li><b>{}</b> points for {}</li>".format(thresh,medal), file=f)
		print("</ul>", file=f)
		print("<h4>Data Available</h4>", file=f)
		print("<ul>", file=f)
		print("<li>%d Countries</li>" %(len(year.countries)), file=f)
		print("<li>%d Students</li>" %(len(year.students)), file=f)
		print("</ul>", file=f)
		print(r'<h4><a href="problems.html#n{}">Problems and Solutions</a></h4>'.format(year.year_num), file=f)
		print(FOOTER, file=f)

	jquery_script = lambda n,k : \
			r'<script>' + \
			r'$(function() { $("#table_main").tablesorter({sortList: [[%d,%d]]}); } );' %(n,k) + \
			r'</script>'
	with open("results/{}_countries.html".format(year.year_num), "w") as f:
		print(HEADER, file=f)
		print(result_header, file=f)
		print(jquery_script(3 + year.num_problems, 0), file=f) # Ascending by rank
		print(r'<table id="table_main" class="tablesorter">', file=f)
		print("<thead><tr><th>Country</th>" \
				+ year.problem_headers, file=f)
		if year.year_num == 2018:
			print("<th>Total</th><th>Top 4 Avg</th><th>Rank</th><th>Award</th></tr></thead>", file=f)
		elif year.year_num == 2017:
			print("<th>Total</th><th>Top 3 Avg</th><th>Rank</th><th>Award</th></tr></thead>", file=f)
		else:
			print("<th>Total</th><th>Team Avg</th><th>Rank</th><th>Award</th></tr></thead>", file=f)
		print("<tbody>", file=f)
		for country in year.countries:
			print(r'<tr><td>{c.pname}</td>'.format(c=country), file=f)
			print(''.join(["<td>{}</td>".format(country.scores[i]) for i in range(year.num_problems)]), end=' ', file=f)
			print("<td>{c.total}</td><td>{c.sweeps:.2f}</td><td>{c.rank}</td><td>{c.awards}</td>".format(c=country), file=f)
			print("</tr>", end=' ', file=f)
		print("</tbody></table>", file=f)
		print(FOOTER, file=f)
	with open("results/{}_indvs.html".format(year.year_num), "w") as f:
		print(HEADER, file=f)
		print(result_header, file=f)
		print(jquery_script(3 + year.num_problems, 0), file=f) # Ascending by rank
		print(r'<table id="table_main" class="tablesorter">', file=f)
		print("<thead><tr><th>Contestant</th><th>Name</th>" \
				+ year.problem_headers \
				+ "<th>Total</th><th>Rank</th><th>Award</th></tr></thead>", file=f)
		print("<tbody>", file=f)
		for student in year.students:
			print("<tr><td>{s.pcode}</td><td>{s.name}</td>".format(s=student), end=' ', file=f)
			print(''.join(["<td>%s</td>" %(student.scores[i]) for i in range(year.num_problems)]), end=' ', file=f)
			print("<td>{s.score}</td><td>{s.rank}</td><td>{s.medal}</td></tr>".format(s=student), file=f)
		print("</tbody>", file=f)
		print("</table>", file=f)
		print(FOOTER, file=f)
	if year.has_aops:
		with open("results/{}_guest.html".format(year.year_num), "w") as f:
			print(HEADER, file=f)
			print(result_header, file=f)
			print(jquery_script(1 + year.num_problems, 1), file=f) # Descending by Score
			print(r'<table id="table_main" class="tablesorter">', file=f)
			print("<thead><tr><th>Name</th>" \
					+ year.problem_headers \
					+ "<th>Total</th><th>Award</th></tr></thead>", file=f)
			print("<tbody>", file=f)
			for student in year.aopsers:
				print("<tr><td>{s.name}</td>".format(s=student), end=' ', file=f)
				print(''.join(["<td>%s</td>" %(student.scores[i]) for i in range(year.num_problems)]), end=' ', file=f)
				print("<td>{s.score}</td><td>{s.medal}</td></tr>".format(s=student), file=f)
			print("</tbody>", file=f)
			print("<tfoot>", file=f)
			# Compute average
			print("<tr>", file=f)
			print("<td><b>Average</b></td>", file=f)
			for i in range(year.num_problems):
				print("<td><b>{:.2f}</b></td>".format(\
						stat_avg([student.scores[i] for student in year.aopsers])), file=f)
			print("<td><b>{:.2f}</b></td>".format(\
					stat_avg([student.score for student in year.aopsers])), file=f)
			print("<td></td>", file=f)
			print("</tr>", file=f)
			print("</tfoot>", file=f)
			print("</table>", file=f)
			print(FOOTER, file=f)
	with open("results/{}_stats.html".format(year.year_num), "w") as f:
		print(HEADER, file=f)
		print(result_header, file=f)

		print(r'<table id="table_main" class="tablesorter">', file=f)
		print("<thead><tr><th>Problem</th>" \
				+ year.problem_headers \
				+ "</tr></thead>", file=f)
		print("<tbody>", file=f)
		for score in range(0,8): # for each in 0 to 7
			print("<tr><td>Score = {}</td>".format(score), file=f)
			for i in range(year.num_problems):
				print("<td>{}</td>".format(year.get_problem_scores(i).count(score)), file=f)
			print("</tr>", file=f)
		# Compute average
		print("<tr>", file=f)
		print("<td><b>Average</b></td>", file=f)
		for i in range(year.num_problems):
			print("<td><b>{:.2f}</b></td>".format(stat_avg(year.get_problem_scores(i))), file=f)
		print("</tr>", file=f)
		# Compute standard deviation
		print("<tr>", file=f)
		print("<td><b>StdDev</b></td>", file=f)
		for i in range(year.num_problems):
			print("<td><b>{:.2f}</b></td>".format(stat_stddev(year.get_problem_scores(i))), file=f)
		print("</tr>", file=f)
		print("</tbody>", file=f)
		print("</table>", file=f)

		N = len(year.students)
		print("<h4>Overall Statistics</h4>", file=f)
		print("<ul>", file=f)
		print("<li><b>{:.2f}</b> was the average score</li>".format(\
				stat_avg([student.score for student in year.students])), file=f)
		print("<li><b>{}</b> was the median score</li>".format(year.students[int(N/2)].score), file=f)
		for medal, thresh in year.cutoffs.items():
			print("<li><b>{}</b> points for {}</li>".format(thresh,medal), file=f)
		print("</ul>", file=f)


		print(FOOTER, file=f)

#}}}

# Country pages {{{
for year in ELMO:
	for country in year.countries:
		with open(country.url, "w") as f:
			print(HEADER, file=f)
			print(r'<div id="main">', file=f)
			print(r'<h2>{c.code} at <a href="results/{c.year.year_num}_countries.html" class="highlight">ELMO {c.year.year_num}</a></h2>'.format(c=country), file=f)
			print("<h3>" + country.name + "</h3>", file=f)
			print("<h4>Leaders: " + country.leaders + "</h4>", file=f)
			print(r'<script>$(function() { $("#table_main").tablesorter({sortList: [[0,0]]}); } ); </script>', file=f)
			print('<table id="table_main" class="tablesorter">', file=f)
			print("<thead><tr><th>Contestant</th><th>Name</th>" \
					+ year.problem_headers \
					+ "<th>Total</th><th>Rank</th><th>Award</th></tr></thead>", file=f)
			print("<tbody>", file=f)
			for student in country.students:
				print("<tr>", end=' ', file=f)
				print("<td>{s.code}</td><td>{s.name}</td>".format(s=student), file=f)
				print(''.join(["<td>%s</td>" %(student.scores[i]) for i in range(year.num_problems)]), end=' ', file=f)
				print("<td>{s.score}</td><td>{s.rank}</td><td>{s.medal}</td>".format(s=student), file=f)
				print("</tr>", file=f)
			print("</tbody>", file=f)
			print("<tfoot>", file=f)
			print(r'<tr><td colspan="2"><b>Team Results</b></td>', file=f)
			print(''.join(["<td><b>%2d</b></td>" %country.scores[i] for i in range(year.num_problems)]), end=' ', file=f)
			print("<td><b>%2d</b></td>" %country.total, end=' ', file=f)
			print("<td><b>%s</b></td>" %country.rank, end=' ', file=f)
			print("<td><b>%s</b></td>" %country.awards, end=' ', file=f)
			print("</tr>", file=f)
			print("</table>", file=f)
			print(FOOTER, file=f)
# }}}

# Problems page {{{
with open("problems.html", "w") as f, open("internal/prob_links.yaml") as source:
	print(HEADER, file=f)
	print(r'<div id="main">', file=f)
	prob_data = reversed(sorted(yaml.load(source, Loader=yaml.FullLoader).items()))
	for year, d in prob_data:
		print("<h5>ELMO {}</h5>".format(year), file=f)
		print("<ul>", file=f)
		for k,v in sorted(d.items()):
			print(r'<li><a href="{}">{}</a></li>'.format(v,k), file=f)
		print("</ul>", file=f)
	print(FOOTER, file=f)
# }}}

# General info page {{{
with open("general.html", "w") as f, open("static/general_info.html") as payload:
	print(HEADER, file=f)
	print("<!-- DO NOT EDIT THIS PAGE -->", file=f)
	print(r'<div id="main">', file=f)
	print(''.join(payload.readlines()), file=f)
	print(FOOTER, file=f)
# }}}

# vim:foldmethod=marker
