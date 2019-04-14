from math import ceil
ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten','Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
tens = ['Twenty', 'Thirty','Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
misc = ['', 'Thousand', 'Million', 'Billion', 'Trillion', 'Quadrillion', 'Quintillion', 'Sextillion', 'Septillion', 'Octillion', 'Nonillion', 'Decillion', 'Undecillion', 'Duodecillion', 'Tredecillion', 'Quattuordecillion', 'Quindecillion', 'Sexdecillion', 'Septendecillion', 'Octodecillion', 'Novemdecillion', 'Vigintillion', 'Centillion']
def get_text(amount, text=''):
    if amount < 20:
        text += ones[amount]
    elif amount >= 20 and amount < 100:
        text += get_text(amount%10, tens[amount//10-2]+ ' ')
    else:
        text += get_text(amount%100, ones[amount//100] + ' Hundred ')
    return(text)
def amount_in_words(amount):
    amount = str(amount)
    j = []
    text = ''
    while amount:
        j.append(amount[-3:])
        amount = amount[:-3]
    for i in range(len(j)):
        text += get_text(int(j[len(j)-i-1])) + ' ' + misc[ceil(len(j)-i-1)] + ' '
    return(text)
amount = int(input('Enter amount: '))
print(amount_in_words(amount))