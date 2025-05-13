def chunk_string(s,k):
    for i in range(0,len(s),k):
        chunk = s[i:i+k]
        result = ""
        for ch in chunk:
            if ch not in result:
                result += ch
        print(result)
s = "AABCAAADA"
k = 3 
chunk_string(s,k)