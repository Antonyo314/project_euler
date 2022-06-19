import os
import re

for name in os.listdir("."):
    pattern = r"(?P<g1>\D*)(\d+)(.py)"

    m = re.match(pattern, name)

    if m is not None:
        n = int(m.group(2))
        n_f = "{0:03}".format(n)

        # named backreference is used to avoid a bug with incorrect
        # number of the first group, ex:
        # "\103\3" must be "(\1)03(\3)"
        repl = r"\g<g1>{0}\3".format(n_f)

        name_new = re.sub(pattern, repl, name)

        os.rename(name, name_new)

        print(name, "changed to")
        print(name_new)
