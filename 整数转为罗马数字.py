def intToRoman(self, num: int)
    dit = {'M' : 1000,
    'CM':900,
    'D':500, 
    'CD':400, 
    'C':100, 
    'XC':90, 
    'L':50, 
    'XL':40, 
    'X' : 10,
    'IX':9, 
    'V': 5, 
    'IV':4, 
    'I':1  }
    st = ''
    for i in dit.items():
        s = i[0]*int(d/i[1])
        d = d - int(d/i[1])*i[1]
        st += s
    return st
    
intToRoman(12)