import random, sys
val=random.randint(1,3)
win=0
lose=0
tie=0
print("Lets play Rock, Paper, Scissors")
print("Choose r for rock, p for paper and s for scissors. If you dont want to play anymore, choose q for quit the game")
while True:
    if val==1:
        comp='r'
    elif val==2:
        comp='p'
    elif val==3:
        comp='s'
    player=input("Enter your choice")
    if player=='q':
        sys.quit()
    if comp=='r' and player=='p':
        win=win+1
    elif comp==player:
        tie=tie+1
    elif comp=='r' and player=='s':
        lose=lose+1
    elif comp=='p' and player=='r':
        lose=lose+1
    elif comp=='p' and player=='s':
        win=win+1
    elif comp=='s' and player=='p':
        lose=lose+1
    elif comp=='s' and player=='r':
        win=win+1
        
print("Won: "+ str(win)+" Lost: "+str(lose)+" Tied: "+{tie})
