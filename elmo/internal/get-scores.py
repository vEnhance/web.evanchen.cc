import yaml

# Script constants
YEARS = [2012, 2013, 2014, 2015, 2016]
PREV_URL = "http://artofproblemsolving.com/community/c5h1095553"
NEXT_URL = "http://nyan.cat"


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
	def total(self): return sum([student.score for student in self.students])
	@property
	def average(self):
		return self.total / float(len(self.students))
	@property
	def scores(self): return [sum([s.scores[i] for s in self.students])\
			for i in xrange(self.year.num_problems)]
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
		if not kwargs.has_key("num_problems"):
			self.num_problems = 6
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

for year_num in YEARS:
	filename = "{}.yaml".format(year_num)
	with open(filename, 'r') as f:
		data = list(yaml.load_all(f))
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

	ELMO.append(year)
# }}}


# Now print things
for year in ELMO:
	N = len(year.students)
	for student in year.students:
		if student.name == "?": continue
		student.percentile = int(100 * (N+1-student.rank) / float(N))
		print "{s.name}\t{s.score}\t{s.percentile}\t{y}".format(s=student, y=year.year_num)
