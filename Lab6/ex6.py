import re

def ex_6(text):
    words = re.findall('[aeiou][a-z]+[aeiou]', text, flags=re.IGNORECASE)
    new_text = '' + text + ''
    for word in words:
        censure = ''+word[0]
        censure+='*'*(len(word)-2)
        censure+=word[-1]
        censure+=''

        to_find =''+word+''
        new_text=new_text.replace(to_find, censure)
    return new_text[1:-1]


if __name__ == '__main__':
    print(ex_6("absefgei ara ara cha"))
