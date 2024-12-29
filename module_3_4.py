"""def  single_root_words (root_word,*other_words):
    same_words = []
    for i in other_words:
        if i.endswith(("est","cum","ies","Able","sable")):
            same_words.append(i)
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')

result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)

print(result2)"""

def  single_root_words (root_word,*other_words):
     same_words = []
     root_word = root_word.lower()
     for i in other_words:
         if i.lower() in root_word or root_word in i.lower():
             same_words.append(i)
     return same_words

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))