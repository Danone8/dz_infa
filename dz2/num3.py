a = input()
palind = a == a[::-1]
a2 = a.replace('E', 'E1').replace('J', 'L1').replace('S', '21').replace('Z', '51')
a2 = a2.replace('L', 'J').replace('2', 'S').replace('3', 'E').replace('5', 'Z')
a2 = a2.replace('E1', '3').replace('L1', 'L').replace('21', '2').replace('51', '5')
mirror = a == a2[::-1]
for el in a:
    if el not in 'AHIMOTUVWXY18EJLSZ235':   
        mirror = False
if palind and mirror:
    print(a + " is a mirrored palindrome")
elif palind:
    print(a + " is a regular palindrome")
elif mirror:
    print(a + " is a mirrored string")
else:
    print(a + " is not a palindrome")
