from tkinter import *

expression: str = ""
equation: StringVar


def clear():
    global expression
    expression = ""
    equation.set("")


def equal_press():
    global expression

    if expression == "":
        equation.set("0")
        return

    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except ZeroDivisionError:
        equation.set(" Cannot divide by 0 ")
        expression = ""
    except SyntaxError:
        equation.set(" Syntax Error ")
        expression = ""


def press(btn_txt: str):
    global expression

    if btn_txt == "c":
        clear()
        return
    elif btn_txt == "b":
        expression = expression[:-1]
        equation.set(expression)
        return
    elif btn_txt == "=":
        equal_press()
        return

    expression = expression + btn_txt
    equation.set(expression)


def create_buttons(root: Tk, button_texts: list[tuple[str, str]]) -> None:
    for i in range(len(button_texts)):
        if button_texts[i][0] is None: continue
        button = Button(root, text=button_texts[i][0], font=('arial', 20, 'bold'), bd=10, width=5, height=2,
                        command=lambda text=button_texts[i][1]: press(text))
        button.grid(row=i // 4 + 1, column=i % 4)


def main():
    root = Tk()
    root.resizable(False, False)
    root.title("Simple Calculator")
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
        ('.', '.'), ('0', '0'), ('=', '='), ('÷', '/')
    ]
    create_buttons(root, button_texts)

    root.mainloop()


if __name__ == "__main__":
    main()
