#!/usr/bin/python

from jinja2 import Environment, FileSystemLoader

persona = [
    {'name': 'Amar', 'age': 12},
    {'name': 'Akbar', 'age': 17},
    {'name': 'Anthony', 'age': 22},
    {'name': 'James', 'age': 42},
    {'name': 'Jesse', 'age': 16},
    {'name': 'Walter', 'age': 62}
]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('showminors.txt')

output = template.render(persons=persona)
print(output)


