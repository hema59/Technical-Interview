test_cases = { '1' : "This is a test String!!" }
answers = { '1' :  "THIS si A tset STRING!!"}

def modify_odd( s ):
    if len(s) == 0 : return "Invaild"
    string = s.split(" ")
    for idx, word in enumerate(string):
        if idx%2 == 0 :
            string.pop(idx)
            word = list(word)
            string.insert(idx, "".join(word))
        else:
            string.pop(idx)
            string.insert(idx, str.upper(word))
    return " ".join(string)

print(modify_odd(test_cases['1']))