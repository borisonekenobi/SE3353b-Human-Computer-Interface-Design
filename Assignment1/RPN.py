from tkinter import *

from stack import Stack

cur_expr: str = ""
stack_expr: Stack = Stack()
equation: StringVar
clear_next: bool = False


def clear():
    global stack_expr
    stack_expr.clear()
    equation.set("")


def press(btn_txt: str):
    global stack_expr
    global cur_expr
    global clear_next

    if btn_txt == "c":
        stack_expr.clear()
        equation.set("")
        return
    elif btn_txt == "b":
        cur_expr = cur_expr[:-1]
        if len(cur_expr) == 0: equation.set(stack_expr.top())
        else: equation.set(cur_expr)
        return
    elif btn_txt == "=":
        stack_expr.push_only(cur_expr)
        clear_next = True
        return
    elif btn_txt in "+-*/":
        stack_expr.push(cur_expr)
        stack_expr.squish(btn_txt)
        equation.set(stack_expr.top())
        clear_next = True
        return

    if clear_next: cur_expr = ""
    cur_expr = cur_expr + btn_txt
    equation.set(cur_expr)
    clear_next = False


def create_buttons(root: Tk, button_texts: list[tuple[str, str]]) -> None:
    for i in range(len(button_texts)):
        if button_texts[i][0] is None: continue
        button = Button(root, text=button_texts[i][0], font=('arial', 20, 'bold'), bd=10, width=5, height=2,
                        command=lambda text=button_texts[i][1]: press(text))
        button.grid(row=i // 4 + 1, column=i % 4)


def main():
    root = Tk()
    root.resizable(False, False)
    root.title("RPN Calculator")
    root.geometry("444x574")

    global equation
    equation = StringVar()
    entry = Entry(root, textvariable=equation, font=('arial', 20, 'bold'), bd=10, insertwidth=4, width=20,
                  justify='right')
    entry.configure(state=DISABLED)
    entry.grid(row=0, column=0, columnspan=4)

    button_texts: list[tuple[str, str]] = [
        (None, None), (None, None), ('C', 'c'), ('⇦', 'b'),
        ('1', '1'), ('2', '2'), ('3', '3'), ('+', '+'),
        ('4', '4'), ('5', '5'), ('6', '6'), ('-', '-'),
        ('7', '7'), ('8', '8'), ('9', '9'), ('×', '*'),
        ('.', '.'), ('0', '0'), ('Enter', '='), ('÷', '/')
    ]
    create_buttons(root, button_texts)

    root.mainloop()


if __name__ == "__main__":
    main()
