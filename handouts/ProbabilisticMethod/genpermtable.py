import itertools

letters = ("W", "X", "Y", "Z")
for n, perm in enumerate(itertools.permutations(letters), start=1):
    bold = [perm[i] == letters[i] for i in range(4)]
    tup = [
        rf"\textbf{{\color{{red}} {perm[i]}}}" if bold[i] else perm[i] for i in range(4)
    ]
    print(n, "&", " & ".join(tup), "&", bold.count(True), r"\\")
