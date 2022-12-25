def lengthOfLongestSubstring(s):
    k=""
    count=0
    j=0
    while(j<len(s)):
            if s[j] not in k:
                k+=(s[j])
            else:
                count=max(count,len(k))
                k="" 
            j+=1                
    return  max(count,len(k))

print(lengthOfLongestSubstring("_abc"))






