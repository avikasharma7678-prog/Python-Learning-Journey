import random
def game(user,sc):
    ch=random.randint(1,3)
    if ch == 1:
        ran='r'
    elif ch == 2:
        ran ='p'
    elif ch == 3:
        ran = 's'
    print("THE COMPUTER CHOSE : "+ran)
    if ran in 'r':
        if user in 'Pp':
            print("YOU WIN!!")
            sc["You"]=sc["You"]+1
        elif user in 'Ss':
            print("YOU LOSE!!")
            sc["Comp"]=sc["Comp"]+1
        elif user in 'Rr':
            print("Tie!!")
        else:
            print("Enter valid choice")
    elif ran in 'p':
        if user in 'Ss':
            print("YOU WIN!!")
            sc["You"]=sc["You"]+1
        elif user in 'Rr':
            print("YOU LOSE!!")
            sc["Comp"]=sc["Comp"]+1
        elif user in 'Pp':
            print("Tie!!")
        else:
            print("Enter valid choice")
    else:
        if user in 'Rr':
            print("YOU WIN!!")
            sc["You"]=sc["You"]+1
        elif user in 'Pp':
            print("YOU LOSE!!")
            sc["Comp"]=sc["Comp"]+1
        elif user in 'Ss':
            print("Tie!!")
        else:
            print("Enter valid choice")
    print("Score:")
    print("You: ",sc["You"])
    print("Comp: ",sc["Comp"] )
    return sc
sc={"You":0,"Comp":0}
while True:
    ch=input("Do you want to play Rcok,Paper,Scissors(y/n) : ")
    if ch in 'yY':
        us=input("Enter your choice- Rock(r),Scissor(s),Paper(p):")
        game(us,sc)
    else:
        print("Thankyou!!")
        exit()
