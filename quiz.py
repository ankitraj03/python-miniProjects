import pyinputplus as pyip
import random, time
time_limit=5
numberofq=10
correct=0
question={'A':"Yes",'B':"Yes",'C':"No",'D':"Yes",'E':"Yes",'F':"No",'G':"No",'H':"Yes",'I':"No",'J':"No"}

for i in range(numberofq):
    n=random.choice(list(question.keys()))
    print("What is the answer of "+n+" (Yes/No)")

    start_time=time.time()
    ans=pyip.inputYesNo()
    elapsed_time=time.time()-start_time

    if elapsed_time>time_limit:
        print("Time's up!")
        continue
    if ans.lower()==question[n].lower():
        correct+=1
    else:
        correct-=0.25

print("Your score is "+ str(correct)+ "Out of 10 marks")
