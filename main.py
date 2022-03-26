def palindrom(a):
    if all((a[-1 * i] == a[i-1]) for i in range((len(a)//2))):
        print('Слово является палиндромом!')
    else:
        print('Слово не является палиндромом!')

palindrom(input('Введите слово: '))