def smallest_in_numbers(number):
    english_numbers = ""
    if number < 1000 and number >= 100:
        tens = number // 100
        number = number % 100
        number_in_words = numbers_list[tens-1]
        english_numbers += number_in_words + " " + "Hundred "
    if number<100 and number>=20:
        tens = number // 10 
        number = number % 10 
        number_in_words = tens_list[tens-2]
        english_numbers += number_in_words + " "
    if number < 20 and number != 0:
        number_in_words = numbers_list[number-1]
        english_numbers += number_in_words + " "
    return english_numbers
def start_number(number):
    english_numbers = ''
    if number >= 1000000000 and number <= 10000000000:
        req = number // 1000000000
        number = number % 1000000000
        number_in_words = smallest_in_numbers(req)
        english_numbers += number_in_words +"Billion "
    if number >=1000000 and number < 1000000000:
        req = number // 1000000 
        number = number % 1000000
        number_in_words = smallest_in_numbers(req)
        english_numbers += number_in_words + "Million "
    if number < 1000000 and number >= 1000:
        req = number // 1000 
        number = number % 1000 
        number_in_words = smallest_in_numbers(req)
        english_numbers += number_in_words + "Thousand "
    if number < 1000 and number > 0:
        english_numbers +=smallest_in_numbers(number)
    
    return english_numbers

number = int(input())
english_numbers = ''
numbers_list= ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens_list = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
english_numbers = start_number(number)
print(english_numbers)