class Stack:
    stack: list[str]

    def __init__(self) -> None:
        self.stack = []

    def push(self, item: str) -> None:
        self.stack.append(item)

    def push_only(self, item: str) -> None:
        self.stack = [item]

    def pop(self) -> str:
        return self.stack.pop()

    def top(self) -> str:
        return self.stack[-1]

    def bottom(self) -> str:
        return self.stack[0]

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def clear(self) -> None:
        self.stack = []

    def squish(self, operator: str) -> None:
        if operator == '=': return
        if len(self.stack) < 2: return
        self.stack = [eval(f"{self.bottom()}{operator}{self.top()}")]

    def __str__(self) -> str:
        return str(self.stack)
