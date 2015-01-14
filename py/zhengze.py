import re
def expand_abbr(sen, abbr):
    lenabbr = len(abbr)
    ma = '' 
    for i in range(0, lenabbr-1):
        ma += abbr[i] + "[a-z]+" + ' ' + '([a-z]+ )?'
    ma += abbr[lenabbr-1] + "[a-z]+"
    print 'ma:', ma
    ma = ma.strip(' ')
    p = re.search(ma, sen)
    if p:
        return p.group()
    else:
        return ''

print expand_abbr("Welcome to Algriculture Bank of China", 'ABC')
