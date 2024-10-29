"""
Languages
Estimate: 10 minutes
Actual:   11 minutes
"""
from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

languages = [python, ruby]
print("The dynamically typed languages are:")
dynamic_language = [language for language in languages if language.is_dynamic()]
for language in dynamic_language:
    print(language.name)