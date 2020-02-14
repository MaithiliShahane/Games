impor random

a= random.randint(0,100)
print(a)


while True:
    x=int(input("Enter your guess: "))
   
    if a==x:
        print("You it right !! ")
        break
        
    elif abs(a-x) >10:
        print("You are gettin there....!")
          
    elif abs(a-x) < 5 :
        if abs(a-x) <2 :
             print("Just missed, about to get it")
        else:
            print("You are very close..!")
    
