class StringCalculator:

    def add(self, user_input):
    
        if user_input is None:
            return None
        else: 
            numbers = user_input.split(',')
            result = 0
            for number in numbers: 
                result += int(number)
            return result

calculator = StringCalculator()
print(calculator.add('2,3,5'))    
    
