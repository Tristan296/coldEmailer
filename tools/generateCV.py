import yaml
from jinja2 import Environment, FileSystemLoader
import subprocess
import os

# Load YAML data
with open("resources/resumeData.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

# Setup Jinja2 environment, assuming template is in current directory
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("resources/resume_template.tex")

# Render LaTeX content
latex_content = template.render(**data)

# Write to .tex file
tex_filename = "Tristan_Norbury_Resume.tex"
with open(tex_filename, "w", encoding="utf-8") as f:
    f.write(latex_content)

# Compile to PDF with pdflatex (make sure pdflatex is installed on your system)
subprocess.run(["pdflatex", tex_filename])

# Optional: cleanup auxiliary files
for ext in ['aux', 'log', 'out']:
    try:
        os.remove(f"Tristan_Norbury_Resume.{ext}")
    except FileNotFoundError:
        pass

