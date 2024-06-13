def decodificar(nome, frase, valor_cripto):
    for salto in range(0, 127):
        new_frase = ''
        discrito = open('banco_01.txt', 'r')
        for l in discrito.read():
            if ord(l)+salto > 127:
                new_frase += chr((ord(l)+ salto)% 127)
            else:
                new_frase += chr((ord(l)+ salto))
                
        print(f'Tentativa [{salto}] : {new_frase}\n')
        save = open('result.txt', 'a')
        save.write(new_frase)
        save.close()
        discrito.close()
while True:
    a ='banco_01.txt'
    b =127
    c =input('Digite: ')
    
    decodificar(a,b,c)
