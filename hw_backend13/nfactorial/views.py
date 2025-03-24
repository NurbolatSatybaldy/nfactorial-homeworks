from django.shortcuts import render
from django.http import HttpResponse

def hello_nfactorial(request):
    return HttpResponse("Hello, nfactorial school!")

# Create your views here.
def add_numbers(request, first, second):
    result = first + second
    return HttpResponse(str(result))

def upper_case(request, text):
    return HttpResponse(text.upper())

def check_palindrome(request, word):
    is_palindrome = word == word[::-1]
    return HttpResponse(str(is_palindrome))

def calculator(request, first, operation, second):
    if operation == 'add':
        result = first + second
    elif operation == 'sub':
        result = first - second
    elif operation == 'mult':
        result = first * second
    elif operation == 'div':
        if second != 0:
            result = first / second
        else:
            return HttpResponse("Division by zero is not allowed.")
    else:
        return HttpResponse("Invalid operation.")
    return HttpResponse(str(result))
