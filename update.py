#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

intro = """# @qxcode

Lista de Exercícios
=========================
"""


base = [x[0] for x in os.walk("./base")]
tags = {'aux':[], 'vet':[], 'rec':[], 'lst':[], 'sta':[], 'cha':[], 'str':[], 'mat':[], 'arq':[]}

output = intro
for i in range(1,len(base)):
    with open(base[i] + "/Readme.md", "r") as readme:
        texto = readme.readlines()
        tags[re.compile(".*?((?:[a-z][a-z]+))", re.IGNORECASE|re.DOTALL).search(texto[0]).group(1)].append((("- [Link](%s/Readme.md#qxcode) %s\n" % (base[i], texto[0].strip()[3:]))))

for tag in tags:
    tags[tag] = sorted(tags[tag], key=lambda x : int(re.compile(".*?(?:[a-z][a-z]*[0-9]+[a-z0-9]*).*?((?:[a-z][a-z]*[0-9]+[a-z0-9]*))",re.IGNORECASE|re.DOTALL).search(x).group(1)[1]))
    
    if tags[tag]:
        output += "\n\n"
        output += "## %s\n" % tag
        for questao in tags[tag]:
            print(questao, end="")
            output += questao

with open("./Readme.md", "w+") as saida:
    saida.write(output)
with open("./base/Readme.md", "w+") as saida:
    output = output.replace("./base/", "./")
    saida.write(output)
