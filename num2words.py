ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten','Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
tens = ['Twenty', 'Thirty','Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
misc = ['', 'Thousand', 'Million', 'Billion', 'Trillion', 'Quadrillion', 'Quintillion', 'Sextillion', 'Septillion', 'Octillion', 'Nonillion', 'Decillion', 'Undecillion', 'Duodecillion', 'Tredecillion', 'Quattuordecillion', 'Quindecillion', 'Sexdecillion', 'Septendecillion', 'Octodecillion', 'Novemdecillion', 'Vigintillion', 'Centillion']
def get_text(amount, text=''):
    text += ones[amount] if amount < 20 else get_text(amount%10, tens[amount//10-2]+ ' ') if amount >= 20 and amount < 100 else get_text(amount%100, ones[amount//100] + ' Hundred ')
    return(text)
def amount_in_words(amount, text=''):
    amount = amount.zfill(3*(-(-len(amount)//3)))
    for i in range(len(amount)//3):
        text += (get_text(int(amount[0+3*i:3+3*i])) + ' ' + misc[(len(amount)//3)-i-1] + ' ') 
    return(' '.join(text.split()))
print(amount_in_words(str(input('Enter amount: '))))