import re

class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0

        delimiter = ","
        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            delimiter = re.escape(parts[0][2:])
            numbers = parts[1]

        numbers = numbers.replace("\n", delimiter)
        number_list = re.split(delimiter, numbers)

        negatives = [int(num) for num in number_list if int(num) < 0]
        if negatives:
            raise ValueError(f"Negatives not allowed: {', '.join(map(str, negatives))}")

        return sum(int(num) for num in number_list if int(num) <= 1000)
