def ficha(jog='<desconhecido>',gol=0):
    print(f'O jogador {jog} fez {gol} gols(s) no campeonato.')

#prog principal
n = str(input("Nome do Jogador: "))
g = str(input("Numero de Gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)