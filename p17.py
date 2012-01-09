numdict = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
}
def stringify(num):
    if num < 100:
        if num <= 20:
            return numdict[num]
        remainder = num % 10
        tenny = num - remainder
        return numdict[tenny] + numdict[remainder]
    remainder = num % 100
    hunky = (num - remainder)/100
    if remainder == 0:
        return numdict[hunky] +'hundred'
    return numdict[hunky] +'hundred and ' + stringify(remainder)

strrep = ""
for i in range(1, 1000):
    strrep += stringify(i).replace(" ", "")
strrep += "onethousand"
print len(strrep)
