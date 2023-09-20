import itertools

letters = ('W', 'X', 'Y', 'Z')
n=0
for perm in itertools.permutations(letters):
	n += 1
	bold = [perm[i] == letters[i] for i in xrange(4)]
	tup = [
			r'\textbf{\color{red} %s}' %perm[i]
			if bold[i]
			else perm[i]
			for i in xrange(4)
			]
	print n,
	print '&',
	print ' & '.join(tup),
	print '&',
	print bold.count(True),
	print r'\\'

