email = input("Enter your email: ") 
k,j,d = 0,0,0
if (len(email) >= 6):
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if ("." == email[-3]) ^ ("." == email[-4]):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k == 1 or j==1 or d==1:
                    print('Invalid Email')
                else:
                    print('Valid Email')
            else:
                print('Invalid Email')
        else:
            print('Invalid Email')
    else:
        print ('Invalid Email')
else:
    print ("Email must be at least six characters long.")
    
