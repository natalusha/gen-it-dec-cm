class FancyIterator:
    def __init__(self, end):
        self.current = 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        fancy_str = "🌷" * self.current
        fancy_val = f"fancy iterator was called {fancy_str} time(s)"
        self.current += 1
        return fancy_val

    @staticmethod
    def print_task_name(name):
        print("=" * 40)
        print(f"THAT`S HOW {name} WORKS")
