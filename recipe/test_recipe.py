#!/usr/bin/env python
"""Test that meta.yaml is a valid YAML after being processed by Jinja"""

from hashlib import sha256
from io import StringIO
from urllib.request import urlopen

from jinja2 import Template
import yaml

with open('meta.yaml') as fp:
    t = Template(fp.read())

io = StringIO(t.render(()))
data = yaml.load(io)  # Will fail on invalid YAML

m = sha256()
with urlopen(data['source']['url']) as fp:
    m.update(fp.read())

if m.hexdigest() != data['source']['sha256']:
    print('bad digest')
