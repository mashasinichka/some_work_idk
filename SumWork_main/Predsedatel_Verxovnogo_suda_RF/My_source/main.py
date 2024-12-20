class Calculation():

    def __init__(self):
        self.greeting = None

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def string_check(self, str_: str):
        return str_.upper()

    def bool_check(self, bool_: bool):
        return bool_

    def div(self, a, b):
        return a / b

    def find_palyndrome(self, arg: input) -> bool:
        arg = input()
        return arg == arg[::-1]

    def check_data_type(self, data_input: int):
        data_input = int(input())
        data_input_2 = int(input())
        return data_input * data_input_2
    def boole(self, arges: bool):
        return arges
class Text_Greeting():
    def greeting(self, name: input) -> str:
        return f"my name {name}"
    def empty_string(self, arg: input) -> bool:
        arg = input()
        return 0 < len(arg)
    def register_check(self, arge: str):
        return arge.upper()
    def long_check(self, syt: input) -> bool:
        syt = input()
        if len(syt) < 10:
            return "passed"
        else:
            return "failed"
    def string_type(self, arg):
        return not isinstance(arg, str)




