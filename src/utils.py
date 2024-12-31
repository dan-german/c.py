tab = "    "
space = " "
nl = "\n"

class Peeker[T]: 
    def __bool__(self): return self.i < len(self.list)
    def __repr__(self): return f"index: {self.i}, item: {self.list[self.i]}"
    def __init__(self, list: list[T]): 
        self.list = list
        self.i = 0
    def peek(self, n = 0) -> T: 
        if not self.list or self.i + n >= len(self.list): return None
        return self.list[self.i + n]
    def next(self, n = 1) -> T:
        temp = self.peek()
        self.i += n
        return temp
    def back(self, n = 1): self.next(-n)