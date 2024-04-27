# nested functions calls = function call inside other function calls
#                         innermost function call are resolved first
#                         returned value is used as arguments for the next outer function

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

print(round(abs(float(input("Enter a whole positive number : ")))))

