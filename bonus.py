password = input("enter a password : ")

result = {}

if len(password) >= 8:
    result["length"]= True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"]=digit

upper = False
for u in password:
    if u.isupper():
        upper = True

result["upperr"] =upper


print(result)
if all (result) == True:
    print("stronfg password")
else:
    print("weak password")

