
def solve(s, k) : 
m = dict.fromkeys(s,0) 
for i in range(len(s)) : 
m[s[i]] += 1
length += 1
if length > k : 
m[s[pos]] -= 1
pos += 1
length -= 1
if length == k and m[s[i]] == length : 
count += 1
    print(count) 
def solve(s, k) : 
count, length, pos = 0, 0, 0
m = dict.fromkeys(s,0) 
for i in range(len(s)) : 
m[s[i]] += 1
length += 1
if length > k : 
m[s[pos]] -= 1
pos += 1
length -= 1
if length == k and m[s[i]] == length : 
count += 1
    print(count) 
              
