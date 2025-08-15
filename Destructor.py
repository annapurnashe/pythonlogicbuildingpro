class person:
    def __init__(self,name):
        self.name=name
        print(f"hello,my name is {self.name}.")

    def __del__(self):
        print(f"Goodbye from {self.name}.")

p=person("Alice")





