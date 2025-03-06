number_word = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14, 
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'fourty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    # 'hundred': 100,
    # 'thousand': 1000,
    # 'million': 1000000,
}

# Maybe reverse the direction????
# For f string :, get thousand seperators

# teststring = 'Three hundred million'
teststring = input("WHATS DA NUMBER IN WORDS: ")

seperated_string = teststring.lower().split()

# seperated_string.reverse()

print(seperated_string)

total = 0
current = 0


def multfinder(number):
    if number == "million":
       return 1000000
    elif number == "thousand":
        return 1000
    elif number == "hundred":
        return 100
    else: 
        return False

def convert(number):
    value = number_word.get(number)
    return value

for i in seperated_string:
    dope = convert(i)
    if dope:
        current += dope
        continue
        # current = dope

    elif multfinder(i):
        mult = multfinder(i)
        # total += current * mult
        if total == 0:
            total += current * mult
        else:
            total *= mult
        print(f"current value: {current}")
        print(f"current {total}")
        current = 0
    elif i == "and":
        continue
    
total += current


print(f"Total: {total:,}")