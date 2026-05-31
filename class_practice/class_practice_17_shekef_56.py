#שאלה 1
def multiply_by_two(number):
    number_result = number * 2
"""
    Accepts a number, multiplies it by 2, and prints the result.

    Args:
        number (int/float): The input number to be multiplied.

    Returns:
        None: This function only prints the output and does not return a value.
    """
user_number = float(input("write number : ")) 
multiply_by_two(user_number)
print(user_number * 2)

#שאלה 2
def double_string_length(text):
    """
    Accepts a string, calculates its length, and returns that length multiplied by 2.

    Args:
        text (str): The input string to measure.

    Returns:
        int: The length of the string multiplied by 2.
    """
    length = len(text)
    return length * 2


user_input = input("write string: ")

final_result = double_string_length(user_input)

print("string length doubled:", final_result)



#שאלה 3
def check_if_char_exist_more_than_once(text: str) -> bool:
 """
 Args:
        text (str): המחרוזת לבדיקה.

    Returns:
        bool: True אם התו האחרון מופיע לפחות עוד פעם אחת במחרוזת, 
              False אחרת (או אם המחרוזת ריקה).

    Examples:
        >>> has_duplicate_last_char("radar")
        True
        >>> has_duplicate_last_char("apple")
        False
    """  
 return text.count(text[-1]) > 1

text = "this is the best text for checking the function"
print("is last char appear more then once ? ",check_if_char_exist_more_than_once)
