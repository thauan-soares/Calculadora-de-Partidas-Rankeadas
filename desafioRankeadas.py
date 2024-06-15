while True:
        #define uma função para calcular o saldo de vitórias do Herói
        def calcSaldo(v,d):
            try:
                v = int(input("Quantidade de Vitórias: "))
                d = int(input("Quantidade de Derrotas: "))
                saldo = v-d
                return saldo

            except ValueError:
                print("valor inválido, tente novamente...")
        #define o nível de acordo com o saldo de vitórias
        def rankear():
            if saldo < 10:
                rank = "Ferro"
            elif saldo >= 11 and saldo <= 20:
                rank = "Bronze"
            elif saldo >= 21 and saldo <= 50:
                rank = "Prata"
            elif saldo >= 51 and saldo <= 80:
                rank = "Ouro"
            elif saldo >= 81 and saldo <= 90:
                rank = "Diamante"
            elif saldo >= 91 and saldo <= 100:
                rank = "Lendário"
            elif saldo >= 101:
                rank = "Imortal"

            print(f"O Herói tem o saldo de {saldo} e está no nível de {rank}")
        
        #executa a função calcSaldo() e atribui a retorno a variável saldo
        saldo = calcSaldo(0,0)
        rankear()
        break


