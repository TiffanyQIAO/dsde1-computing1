import math
def period():
    while True:
        try:
            argu1=int(input("L:"))
            argu2=int(input("g:"))

   
        
        except TypeError:
            print("Sorry, I didn't understand that.")
            continue
        except ValueError:
            print("Sorry,the equation cannot correctly compute")
            continue
        else:
            break
    
    return 2*math.pi*(argu1/argu2)**(1/2)
print(period())
