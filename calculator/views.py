from django.shortcuts import render


# Create your views here.

def main(request, val1, action, val2):
    print(type(5))
    wrong = None
    ans = None
    if action == '*':
        ans = val1 * val2
    elif action == 'deg':
        ans = val1 / val2
    elif action == '+':
        ans = val1 + val2
    elif action == '-':
        ans = val1 - val2
    else:
        wrong = "Something wrong men"

    return render(request, 'calculator/main.html', {"val1": val1, "action":action, "val2": val2, "ans": ans, "wrong": wrong})
