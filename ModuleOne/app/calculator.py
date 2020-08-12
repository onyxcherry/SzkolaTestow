class StringCalculator:
    """
    Add given numbers as text line, separated by a comma.
    Spaces are allowed.
    """
    @staticmethod
    def add(user_input: str) -> int:
        if user_input is None or user_input.strip() == '':
            return 0
        else:
            numbers = user_input.split(',')
            result = 0
            for number in numbers:
                result += int(number)
            return result
