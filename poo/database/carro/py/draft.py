class Carro:
    def __init__(self, passa: int = 0, gas: int = 0, km: int = 0):
        self.passa = passa
        self.gas = gas
        self.km = km

    def __str__(self) -> str:
        return f"pass: {self.passa}, gas: {self.gas}, km: {self.km}"
    
    def enter(self):
        if self.passa < 2:
            self.passa += 1
        else:
            print("fail: limite de pessoas atingido")

    def leave(self):
        if self.passa == 0:
            print("fail: nao ha ninguem no carro")
        else:
            self.passa -= 1
    
    def fuel(self, amount: int):
        self.gas += amount
        if self.gas > 100:
            self.gas = 100
    
    def drive(self, distance: int):
        if self.passa == 0:
            print("fail: nao ha ninguem no carro")
        elif self.gas == 0:
            print("fail: tanque vazio")
        else:
            if distance > self.gas:
                print(f"fail: tanque vazio apos andar {self.gas} km")
                self.km += self.gas
                self.gas = 0
            else:
                self.km += distance
                self.gas -= distance


def main():
    carro = Carro()

    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "enter":
            carro.enter()
        elif args[0] == "show":
            print(carro)
        elif args[0] == "leave":
            carro.leave()
        elif args[0] == "fuel":
            increment = int(args[1])
            carro.fuel(increment)
        elif args[0] == "drive":
            increment = int(args[1])
            carro.drive(increment)

main()
