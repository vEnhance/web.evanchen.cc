import yaml

print(r"\begin{enumerate}")
with open("omo.yaml") as f:
    probs = yaml.load_all(f, Loader=yaml.SafeLoader)
    for prob in probs:
        if prob is None:
            continue
        print(r"\item", prob["statement"].strip())
        comments = prob.get("comments", "")
        comments = comments.strip()
        if comments != "":
            print(r"\begin{lstlisting}")
            print(comments)
            print(r"\end{lstlisting}")
        print("%" * 30)
        print()
print(r"\end{enumerate}")
