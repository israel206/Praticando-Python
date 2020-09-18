times = ('Corinthians','Palmeiras','Santos','Gremio',
         'Cruzeiro','Flamengo','Vasco','Chapecoense',
         'Atletico','Botafogo','Atletico-PR','Bahia',
         'Sao paulo','Fluminense','Sport','EC Vitoria',
         'Coritiba','Avai','Ponte Preta','Atletico-GO')
print('-='*15)
print(f'Lista de times: {times}')
'''for t in times:
    print(t)'''
print('-='*15)
print(f'Os 5 primeiros sao {times[0:5]}')
print('-='*15)
print(f'Os 4 ultimos são {times[-4]}')# tuplas pode fatear
print('-='*15)
print(f'Times em Ordem alfabeticas: {sorted(times)}')
print('-='*15)
print(f'Chapecoense esta na posicao {times.index("Chapecoense")+1}ª posicao')

