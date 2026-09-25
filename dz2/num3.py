a = input()
palind = a == a[::-1]
a2 = a.replace('E', 'a').replace('J', 'b').replace('S', 'c').replace('Z', 'd')
a2 = a2.replace('L', 'J').replace('2', 'S').replace('3', 'E').replace('5', 'Z')
a2 = a2.replace('a', '3').replace('b', 'L').replace('c', '2').replace('d', '5')
mirror = a == a2[::-1]
for el in a:
    if el not in 'AHIMOTUVWXY18EJLSZ235':   
        mirror = False
if palind and mirror:
    print(a + " is a mirrored palindrome.")
elif palind:
    print(a + " is a regular palindrome.")
elif mirror:
    print(a + " is a mirrored string.")
else:
    print(a + " is not a palindrome.")
