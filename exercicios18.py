jogo = {
    'time1' : '',
    'time2' : '',
    'point1' : 0,
    'point2' : 0
}
parar  = False
while not parar:
    if jogo['time1'] == '':
        jogo['time1'] = input("Digite o nome do primeiro time: ")
        jogo['time2'] = input("Digite o nome do segundo time: ")
        jogo['point1'] = int(input(f"Quantidade de gols marcardos pelo time {jogo['time1']}"))
        jogo['point2'] = int(input(f"Quantidade de gols marcardos pelo time {jogo['time2']}"))
    parar = True

if jogo['point1'] > jogo['point2']:
    print(f"O vencedor é {jogo['time1']}")
elif jogo['point2'] > jogo['point1']:
    print(f"O vencedor é {jogo['time2']}")
else:
    print("EMPATE")