"""
Programming Language
Estimate: 15 minutes
Actual:   17 minutes
"""
class ProgrammingLanguage:
    def __init__(self, name, type, reflection, year):
        self.name = name
        self.type = type
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.type} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        return self.type == "Dynamic"
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
print(python)