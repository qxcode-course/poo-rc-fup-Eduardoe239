class Towel:
    def _init_(self,color: str,size: str):
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0

    def dry(self,amount: int)-> None:
        self.wetness += amount
        if self.wetness >= self.isMaxWetness():
            self.wetness = self.isMaxWetness()
            print("toalha encharcada")
    
    def isDry(self):
        return self.wetness == 0
    
    def wringOut(self):
        self.wetness = 0

    def isMaxWetness(self) -> int:
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0
    def _str_(self) -> str:
        return f"Cor:{self.color}, Tamanho: {self.size}, Umidade: {self.wetness}"

