from string import Template

t = Template('Hello, $name!')
print(t.substitute(name='John'))
