# Write your solution here
import string

def run(program: list) -> list:
    variables = {letter: 0 for letter in string.ascii_uppercase}
    
    locations = {}

    for idx, line in enumerate(program):
        line = line.strip()

        if line.endswith(":"):
            locations[line[:-1]] = idx

    def get_val(token: str) -> int:
        if token in variables:
            return variables[token]
        return int(token)

    def evaluate_condition(val1_str: str, op: str, val2_str: str) -> bool:
        v1 = get_val(val1_str)
        v2 = get_val(val2_str)
        if op == "==":
            return v1 == v2
        elif op == "!=":
            return v1 != v2
        elif op == "<":
            return v1 < v2
        elif op == "<=":
            return v1 <= v2
        elif op == ">":
            return v1 > v2
        elif op == ">=":
            return v1 >= v2
        return False

    output = []
    pc = 0

    while pc < len(program):
        line = program[pc].strip()
        parts = line.split()
        
        if not parts or line.endswith(":"):
            pc += 1
            continue

        cmd = parts[0]

        if cmd == "END":
            break

        elif cmd == "PRINT":
            output.append(get_val(parts[1]))
            pc += 1

        elif cmd == "MOV":
            var, val = parts[1], parts[2]
            variables[var] = get_val(val)
            pc += 1

        elif cmd == "ADD":
            var, val = parts[1], parts[2]
            variables[var] += get_val(val)
            pc += 1

        elif cmd == "SUB":
            var, val = parts[1], parts[2]
            variables[var] -= get_val(val)
            pc += 1

        elif cmd == "MUL":
            var, val = parts[1], parts[2]
            variables[var] *= get_val(val)
            pc += 1

        elif cmd == "JUMP":
            target = parts[1]
            pc = locations[target]

        elif cmd == "IF":
            v1_str, op, v2_str, target = parts[1], parts[2], parts[3], parts[5]
            if evaluate_condition(v1_str, op, v2_str):
                pc = locations[target]
            else:
                pc += 1

    return output