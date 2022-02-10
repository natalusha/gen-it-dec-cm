def square_generator(end):
    current = 0
    while current <= end:
        current += 1
        result = current**2
        yield result
