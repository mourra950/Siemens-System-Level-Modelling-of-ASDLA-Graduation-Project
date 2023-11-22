from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
import os


template_dir = "./templates"

env = Environment(loader=FileSystemLoader(template_dir))

template_filename = "template.py.jinja"
template = env.get_template(template_filename)

channel = 2
resultfile=template.render(layers=[{'name': 'conva'}, {'name': 'conva'}, {'name': 'conva'}, {'name': 'convb','channels':channel}])

# Create or overwrite a file named train.py in output file and outputs the result from the rendered jinja template

f = open("./output/train.py", "w")
f.write(resultfile)
f.close()