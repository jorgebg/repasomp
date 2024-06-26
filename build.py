import os
from pathlib import Path

from ExportKahoot import ExportKahoot

doc = []
export = ExportKahoot(os.getenv("KH_USER"), os.getenv("KH_PASS"))
with open("_index.md", "r") as f:
    for line in f:
        if line.startswith("https://"):
            url = line[0:-1]
            doc.append(f"[Test]({url})")
        else:
            doc.append(line)
        if line.startswith("https://create.kahoot.it/share"):
            print(line)
            kid = line[-37:-1]
            text = export.export(kid)
            kfilename = f"kahoot/{kid}/index.md"
            Path(kfilename).parent.mkdir(parents=True, exist_ok=True)
            with open(kfilename, "w") as kf:
                kf.write(text)
                doc.append(f" / [Solution](kahoot/{kid})\n\n")


with open("index.md", "w") as f:
    f.writelines(doc)
