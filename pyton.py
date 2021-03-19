def fibonachi(n):
    numb = 1
    if n > 2:
        numb = fibonachi(n - 1) + fibonachi(n - 2)
    return numb

number = input('Enter the number: ')
number = int(number)
answer = fibonachi(number)
print(' sequence element = ' + str(answer))