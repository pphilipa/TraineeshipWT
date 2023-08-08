#csv bestand van: https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6
#api website van: https://catfact.ninja/facts

import requests



print('Start api read applications')

paginaresults= requests.get('https://catfact.ninja/facts')
print(paginaresults)

feitjes = paginaresults.json()
print(feitjes["data"][0])