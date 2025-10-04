class Towel:
    def __init__(self, color: str, size: str):
        self.color = color
        self.size = size
        self.wetness = 0

    def dry(self, amount: int) -> None:
        self.wetness += amount
        if self.wetness >= self.isMaxWetness():
            self.wetness = self.isMaxWetness()
            print("toalha encharcada")
    
    def isDry(self) -> bool:
        return self.wetness == 0
    
    def wringOut(self) -> None:
        self.wetness = 0

    def isMaxWetness(self) -> int:
        if self.size == "P":
            return 10
        elif self.size == "M":
            return 20
        elif self.size == "G":
            return 30
        return 0

    def __str__(self) -> str:
        return f"Cor: {self.color}, Tamanho: {self.size}, Umidade: {self.wetness}"

def main():
    towel = None
    
    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if not args:
            continue

        command = args[0]

        if command == "end":
            break
        elif command == "criar":
            if len(args) >= 3:
                color = args[1]
                size = args[2]
                towel = Towel(color, size)
            else:
                print("fail: parâmetros insuficientes para criar")
        elif command == "mostrar":
            if towel:
                print(towel)
            else:
                print("fail: nenhuma toalha criada")
        elif command == "seca":
            if towel:
                print("sim" if towel.isDry() else "nao")
            else:
                print("fail: nenhuma toalha criada")
        elif command == "torcer":
            if towel:
                towel.wringOut()
            else:
                print("fail: nenhuma toalha criada")
        elif command == "enxugar":
            if towel:
                if len(args) >= 2:
                    amount = int(args[1])
                    towel.dry(amount)
                else:
                    print("fail: quantidade não informada")
            else:
                print("fail: nenhuma toalha criada")
        else:
            print("fail: comando não encontrado")

main()
