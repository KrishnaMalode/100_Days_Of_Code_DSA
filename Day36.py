ip = str(input("Enter a string: "))
n=len(ip)-1
if ip[0].isupper():
    if ip[n].islower():
        print(ip[0].lower()+ip[1:n]+ip[n].upper())
    else:
        print(ip[0].lower()+ip[1:n]+ip[n].lower())
else:
    if ip[n].islower():
        print(ip[0].upper()+ip[1:n]+ip[n].upper()) 
    else:
        print(ip[0].upper()+ip[1:n]+ip[n].lower())

