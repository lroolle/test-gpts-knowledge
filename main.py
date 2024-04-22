import os
import subprocess
import pandas as pd

# Create base directory if it doesn't exist
base_dir = "knowledges"
os.makedirs(base_dir, exist_ok=True)

# Create CSV file
csv_filename = os.path.join(base_dir, "knowledge_data.csv")
csv_data = {"ID": [1, 2, 3], "Name": ["Alice", "Bob", "Charlie"], "Score": [85, 92, 78]}
df = pd.DataFrame(csv_data)
df.to_csv(csv_filename, index=False)

# Dictionary of Pandoc formats and their extensions
file_exts = {
    "asciidoc": "asciidoc",
    "asciidoctor": "adoc",
    "beamer": "tex",
    "biblatex": "bib",
    "bibtex": "bib",
    "chunkedhtml": "html",
    "commonmark": "md",
    "commonmark_x": "md",
    "context": "ctx",
    "csljson": "csljson",
    "djot": "djot",
    "docbook": "docbook",
    "docbook4": "dbk",
    "docbook5": "dbk",
    "docx": "docx",
    "dokuwiki": "wiki",
    "dzslides": "dzslides",
    "epub": "epub",
    "epub2": "epub",
    "epub3": "epub",
    "fb2": "fb2",
    "gfm": "md",
    "haddock": "hs",
    "html": "html",
    "html4": "html",
    "html5": "html",
    "icml": "icml",
    "ipynb": "ipynb",
    "jats": "jats",
    "jira": "jira",
    "json": "json",
    "latex": "tex",
    "man": "man",
    "markdown": "md",
    "markdown_github": "md",
    "markdown_mmd": "mmd",
    "markdown_phpextra": "md",
    "markdown_strict": "md",
    "markua": "markua",
    "mediawiki": "wiki",
    "ms": "ms",
    "muse": "muse",
    "native": "native",
    "odt": "odt",
    "opendocument": "odt",
    "opml": "opml",
    "org": "org",
    "pdf": "pdf",
    "plain": "txt",
    "pptx": "pptx",
    "revealjs": "html",
    "rst": "rst",
    "rtf": "rtf",
    "s5": "s5",
    "slideous": "html",
    "slidy": "html",
    "tei": "tei",
    "texinfo": "texinfo",
    "textile": "textile",
    "typst": "typst",
    "xwiki": "xwiki",
    "zimwiki": "wiki"
}

# Convert CSV to various formats without extra context or highlighting
for fmt, ext in file_exts.items():
    output_filename = os.path.join(base_dir, f"knowledge_data.{ext}")
    try:
        subprocess.run(
            ["pandoc", csv_filename, "--to", fmt, "--data-dir", base_dir, "-o", output_filename],
            check=True,
        )
        print(f"File converted to {fmt} and saved as {output_filename}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting to {fmt}: {e}")
