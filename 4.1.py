class Example:
    staticVar1 = 5
    staticVar2 = 10

    def __init__(self):
        self.dynamicVar1 = 2
        self.dynamicVar2 = 3

    def create_and_print_variable(self):
        new_variable = 7
        print("New Variable:", new_variable)


    @staticmethod
    def get_sum_of_global_variables():
        return Example.staticVar1 + Example.staticVar2

    def power_of_dynamic_variables(self):
        return self.dynamicVar1 ** self.dynamicVar2

example_object = Example()

example_object.create_and_print_variable()
sum_of_globals = Example.get_sum_of_global_variables()
power_result = example_object.power_of_dynamic_variables()

print("Sum of global variables:", sum_of_globals)
print("Power of dynamic variables:", power_result)