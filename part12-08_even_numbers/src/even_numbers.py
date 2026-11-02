def even_numbers(beginning: int, maximum: int):
    start = beginning + 1 if beginning & 1 else beginning
    end = maximum - 1 if maximum & 1 else maximum

    while start <= end:
        yield start
        start += 2