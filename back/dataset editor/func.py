
en_down = "abcdefghijklmnopqrstuvwxyz"
en_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def delete_symbols(text: str , symbols:str ) -> str: #WORK
    ans = ""
    for i in text:
        ok = True
        for b in symbols:
            if i == b :
                ok = False
        if (ok) :
            ans = ans + i
    return ans

def del_double_or_more_spaces(text: str) -> str :
    ans = ""
    was_space = False
    for i in text:
        if i == " ":
            if was_space: 
                continue
            else :
                ans =  ans + i
                was_space = True
        else:
            was_space = False
            ans =  ans + i
    return ans

def deffinition_symb(text: str  , normal_symb : str)->str:
    asn = ""
    for i in text:
        if i not in normal_symb :
            if i not in asn :
                asn = asn + i
    return asn 

def high_reg_to_low(text : str)->str:
    ans = ""
    for i in text:
        if i in en_up:
            ans = ans + en_down[en_up.index(i)]
        else:
            ans = ans + i 
    return ans

def low_reg_to_high(text: str)->str:
    ans = ""
    for i in text:
        if i in en_down:
            ans = ans + en_up[en_down.index(i)]
        else:
            ans = ans + i 
    return ans



