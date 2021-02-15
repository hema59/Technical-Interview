def find_unique_words( words, chars ):
    max_so_far = dict()
    lens = [len(word) for word in words]
    for i in lens:
        max_so_far[i] = [] 
    max_len = cur_len = 0

    for word in words:
        t_char = chars.copy()
        new_word = []
       
        for letter in word:
            if letter in t_char:
                new_word.append(letter)
                t_char.remove(letter)

            else:
                    continue
        
        new_word = "".join(new_word)
        if new_word!= word:
            return []
        cur_len = len(new_word)
        if cur_len >= max_len :
            max_len = cur_len
            max_so_far[len(word)].append(word)
    
    result_key = max(max_so_far.keys())
    result = max_so_far[result_key]
    return result

test_cases = { "1" : { 'words' :[ "abc" , "baa" , "caan" , "an" , "banc" ],
                      'chars' :[ "a" , "a" , "n" , "c" , "b"] },
                "2": { 'words' :[ "aat" ] ,
                      'chars' : ["a","t"] 
                      }
                }
answers = { 
    '1' : ['caan','banc'],
    '2' : []
}
for key in test_cases.keys():
    result = find_unique_words(test_cases[key]['words'], test_cases[key]['chars'])
    
    if result == answers[key]:
        print("{} passed".format(key))
    else:
        print("{} FAILED".format(key))
