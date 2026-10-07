import ast
import sys

print(sys.executable)
print(sys.version)
source = "result = 1 * 2"

print(ast.dump(ast.parse(source), indent=2))

code = compile(source, "<experiment>", "exec")
print(type(code))