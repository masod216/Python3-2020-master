class ShortInputException(Exception):
    pass

text = input('Enter somthing :')
if len(text) <3:
    raise ShortInputException()

