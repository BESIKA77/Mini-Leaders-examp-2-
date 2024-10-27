# 8 kyu
def century(year):
    return (year + 99) // 100
    

def quarter_of(month):
    if month in range(1, 4):
        return 1
    elif month in range (4, 7):
        return 2
    elif month in range(7, 10):
        return 3
    elif month in range(10, 13):
        return 4
    


# 7 kyu
def number(bus_stops):
    sum = 0
    for i in bus_stops:
        sum+=i[0]-i[1]
    return sum



def alphabet_war(fight):
    clash = sum('sbpw'.find(e) - 'zdqn'.find(e) for e in fight)
    
    if clash > 0:
        return 'Left side wins!'
    elif clash < 0:
        return 'Right side wins!'
    else:
        return "Let's fight again!"
    


# 6 kyu
def high(x):
    words = x.split()
    highest_score = 0
    highest_word = ""
    
    for word in words:
        score = sum(ord(char) - ord('a') + 1 for char in word)
        if score > highest_score:
            highest_score = score
            highest_word = word
            
    return highest_word