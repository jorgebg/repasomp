import os

from ExportKahoot import ExportKahoot

doc = []
export = ExportKahoot(os.getenv("KH_USER"), os.getenv("KH_PASS"))
with open("_index.md", "r") as f:
    for line in f:
        doc.append(line)
        if line.startswith("https://create.kahoot.it/share"):
            print(line)
            kid = line[-37:-1]
            text = export.export(kid)
            with open(f"kahoot/{kid}.md", "w") as kf:
                kf.write(text)
                doc.append(f"\n[solution](/kahoot/{kid})")


with open("index.md", "w") as f:
    f.writelines(doc)
