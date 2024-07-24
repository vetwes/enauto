#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader

templating_language = "Jinja2"

environment = Environment(loader=FileSystemLoader("."))
template = environment.get_template("jinja2-test.txt")

filename = "template-script-output.txt"
content = template.render(file_type=templating_language)

with open(filename, "w", encoding="utf-8") as handle:
    handle.write(content)
    print("Wrote to %s" % filename)
