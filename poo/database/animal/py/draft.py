class Animal:
    def __init__(self, specie: str, sound: str):  # construtor
        self.specie: str = specie
        self.sound: str = sound
        self.age: int = 0

    def __str__(self) -> str:  # toString
        return f"{self.specie}:{self.age}:{self.sound}"

    def ageBy(self, increment: int) -> None:
        if self.age == 4:
            print(f"warning: {self.specie} morreu")
            return

        self.age += increment
        if self.age >= 4:
            self.age = 4
            print(f"warning: {self.specie} morreu")

    def makeSound(self) -> str:
        if self.age == 0:
            return "---"
        elif self.age < 4:
            return self.sound
        else:
            return "RIP"


def main():
    animal: Animal = Animal("", "")
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":
            specie: str = args[1]
            sound: str = args[2]
            animal = Animal(specie, sound)
        elif args[0] == "show":
            print(animal)
        elif args[0] == "grow":
            increment: int = int(args[1])
            animal.ageBy(increment)
        elif args[0] == "noise":
            print(animal.makeSound())


if __name__ == "__main__":
    main()
