def balanced_brackets(my_string: str) -> bool:
    # Filter out all characters that are not round or square brackets
    brackets = [ch for ch in my_string if ch in "()[]"]
    clean_string = "".join(brackets)

    # Base case: empty string means all brackets were matched correctly
    if len(clean_string) == 0:
        return True

    # Check if the outer pair is a valid matching set
    first = clean_string[0]
    last = clean_string[-1]

    if (first == '(' and last == ')') or (first == '[' and last == ']'):
        # Recurse on the substring without the outermost brackets
        return balanced_brackets(clean_string[1:-1])

    return False