s=open('24_16388.txt').readline()
k=1
kmax=0
for i in range(0, len(s)):
    if (s[i]=='K' and k%4==0) or  (s[i]=='L' and k%4==1) or (s[i]=='M' and k%4==2) or (s[i]=='N' and k%4==3):
        k=k+1
        kmax = max(k, kmax)
    else:
        if (s[i]=='K'):
            k=1
        else:
            k=1


print(kmax)