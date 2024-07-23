import re  # Add this import at the top of the file

class StringCalculator:
    @staticmethod
    def add(numbers):
        if not numbers:
            return 0
        
        delimiter, numbers = StringCalculator._parse_input(numbers)
        number_list = StringCalculator._split_numbers(numbers, delimiter)
        StringCalculator._check_negatives(number_list)
        
        return StringCalculator._calculate_sum(number_list)

    @staticmethod
    def _parse_input(numbers):
        if numbers.startswith("//"):
            return StringCalculator._extract_custom_delimiter(numbers)
        return ',', numbers

    @staticmethod
    def _extract_custom_delimiter(numbers):
        match = re.match(r"//\[(.+)\]\n(.*)", numbers)
        if match:
            delimiter = match.group(1)
            numbers = match.group(2)
            return delimiter, numbers
        match = re.match(r"//(.)\n(.*)", numbers)
        if match:
            delimiter = match.group(1)
            numbers = match.group(2)
            return delimiter, numbers
        raise ValueError("Invalid format for custom delimiter")

    @staticmethod
    def _split_numbers(numbers, delimiter):
        return [int(num) for num in re.split(f"[{delimiter}\n]", numbers) if num]

    @staticmethod
    def _check_negatives(numbers):
        # Ensure the 'negatives' list is created before it is used
        negatives = [num for num in numbers if num < 0]  # This line defines 'negatives'
        
        if negatives:
            raise ValueError(f"Negatives not allowed: {', '.join(map(str, negatives))}")

    @staticmethod
    def _calculate_sum(numbers):
        return sum(num for num in numbers if num <= 1000)

