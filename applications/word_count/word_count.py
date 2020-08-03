
def word_count(s):
    # Your code here
    # words = re.sub(,s)
    # word = s.split()
    # print("arr", word)
    
    # for c in s:
    #     if c in cache:
    #         cache[c]+=1
    #     else:
    #         cache[s]=1
    # return cache
    words = s.lower()
    
    
    ignored_chars =  '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split()
   
    for c in ignored_chars:

        words = words.replace(c, "")
        
    words = words.split()
   
    
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
           
        else:
            word_count[word] = 1
   
    return word_count







if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))