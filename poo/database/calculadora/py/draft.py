class Calculadora:
    def __init__(self, batteryMax: int):
        self.batteryMax: int = batteryMax
        self.battery: int = 0
        self.display: float = 0.0

    def __str__(self):
        return f"display = {self.display:.2f}, battery = {self.battery}"

    def charge(self, increment: int):
        self.battery += increment
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax

    def sum(self, a: float, b: float) -> None:
        if self.battery > 0:
            self.display = a + b
            self.battery -= 1
        else:
            print("fail: bateria insuficiente")

    def div(self, a: float, b: float) -> None:
        if self.battery > 0:
            if b != 0:
                self.display = a / b
            else:
                print("fail: divisao por zero")
            self.battery -= 1
        else:
            print("fail: bateria insuficiente")


def main():
    calc: Calculadora = Calculadora(0)

    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":
            batteryMax: int = int(args[1])
            calc = Calculadora(batteryMax)
        elif args[0] == "show":
            print(calc)
        elif args[0] == "charge":
            increment: int = int(args[1])
            calc.charge(increment)
        elif args[0] == "sum":
            a: float = float(args[1])
            b: float = float(args[2])
            calc.sum(a, b)
        elif args[0] == "div":
            a: float = float(args[1])
            b: float = float(args[2])
            calc.div(a, b)


if __name__ == "__main__":
    main()
