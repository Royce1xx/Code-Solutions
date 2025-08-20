def reverse_words(s):
    t  = []
    s = s.split()
    l = len(s) - 1
    
    for i in range(len(s)):
        t.append(s[l])
        l = l - 1
        if len(t) == len(s):
            return " ".join(t)