import pyttsx3
import random
from gtts import gTTS
import speech_recognition as sr
import os
import csv
import getpass_ak
import datetime


atmpt=0

limit = 10000
minlimit= 100


class er(Exception):
    pass

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)

def inputcommand():
    r= sr.Recognizer()
    with sr.Microphone() as source :
        print("LISTENING....")
        audio = r.listen(source)
        
    try :
        print("recognizing ....")
        said = r.recognize_google(audio, language = "en-in")
        print(f"you said .. : {said}\n",)


    except Exception as e :
        print(e)
        print("CAN YOU PLEASE SAY THAT AGAIN ...")
        said = ("SORRY I DID NOT UNDERSTAND THAT ")
    return said  

#GREETS THE USER ACCORDING TO TIME

def wish () :
    hour = datetime.datetime.now().hour
    
    if hour>=0 and hour<=12 :
        speak("GOOD MORNING" )
    
    elif hour>= 12 and hour< 18 :
        speak("GOOD AFTERNOON " )
        
    else :
        speak("GOOD EVENING ")
    

def speak (text):
    engine.say(text)
    engine.runAndWait() 

def intro():
    print("")
    print("")
    print("\t\t\t\t@ ************************************* @")
    print("\t\t\t\t# ------------------------------------- #")
    print("\t\t\t\t        ATM SYSTEM FOR BLIND   ")
    print("\t\t\t\t# ------------------------------------- #")
    print("\t\t\t\t@ ************************************* @")
    print("")
    print("")
    print("\t\t\t\tBrought To You By:")
    print("\t\t\t\t--PANDA.CO")
    input()

intro()

wish()


"""eng= "TO SELECT ENGLISH AS LANGUAGE PRESS ONE"
obj = gTTS(text= eng , slow = False , lang ='en')
obj.save('eng.mp3')
speak(eng)"""

USER=""

#ENTERING AND CHECKING OF PIN AND ACC. NUMBER

speak("PLEASE ENTER YOUR 16- DIGIT ACCOUNT NUMBER")
flag1=1
flag2=0
while flag1:
    with open("c:\\Users\\avime\\Desktop\\PROJECTS\\ATM FOR BLIND\\Accounts.csv",'r') as file:
        t=1
        reader=csv.reader(file , delimiter=',')
        l=[]
        l1=[]
        l2=[]
        for i in reader:
            l.append(i)
        for i in l:
            i[1]=int(i[1])
            i[2]=float(i[2])     
            l1.append(i[1])
            l2.append(int(i[3]))

        print("{*{ FEW EXAMPLE ACCOUNTS LOADED, PLEASE SELECT ONE FROM BELOW }*}" )    
        print(l)
        div= 0

    while True :
            accno=input("ENTER YOUR 16 - DIGIT ACCOUNT NUMBER :")
            for i in l :
                if i[3] == accno :
                    div= div +1
                    break
            
            if div == 0 :
                print("INVALID ACCOUNT NUMBER , THE ACCOUNT DOESNT EXIST")
                speak("THE ACCOUNT NUMBER IS INVALID ")
                atmpt = atmpt + 1
                if atmpt == 3 :
                    print("YOU HAVE EXCEEDED THE NUMBER OF TRIES , PLEASE TRY AGAIN LATER ")
                    speak("YOU HAVE EXCEEDED THE NUMBER OF TRIALS , PLEASE TRY AGAIN LATER ")
                    exit()
                    
            else :
                USER = i[0]
                print("ACCOUNT EXISTS ")
                break

    if accno.isdigit() and len(accno)==16:                              #IF(compare with file) THEN:
        flag1=0
        speak("PLEASE ENTER YOUR 4 - DIGIT PIN")
        print("ENTER YOUR 4 - DIGIT PIN")
        while flag2<3:
            try :
                pin = getpass_ak.getpass()

            except Exception as error:
                print("ERROR")
                speak("ERROR ")

            if pin.isdigit() and len(pin)==4 and int(pin) in l1:
                if l1.index(int(pin))==l2.index(int(accno)):
                #check with pin in file., AND TO PUT * 
                    flag1=0
                    flag2=3
                    print("ACCEPTED")
                    speak("ACCEPTED  ")
                else:
                    print("PIN DOES NOT MATCH ")
                    speak("PIN DOES NOT MATCH WITH ACCOUNT NUMBER ")
                #continue to regular code
            else:
                print("ENTER CORRECT PIN ")
                speak("ENTER CORRECT PIN ")
                flag2+=1
                if flag2==3 :
                    speak("YOU HAVE EXCEEDED THE NUMBER OF TRIES ")
                    exit()
    
    else:
        speak("PLEASE ENTER A VALID SIXTEEN DIGIT ACCOUNT NUMBER")  
        print("ENTER A CORRECT ACCOUNT NUMBER ")

wish()
speak("HELLO AND WELCOME")
speak(USER)

print("..........................................................CHOOSE FROM OPTIONS BELOW....................................................")
print("")

speak("PLEASE SELECT FROM THE OPTIONS BELOW")
print("\t\t\t\t\t(1)CASH WITHDRAWAL                                (2)CASH DEPOSIT                                                    ")
speak("1. cash withdrawal . 2 cash deposit")
print("\t\t\t\t\t(3)BALANCE INQUIRY                                (4)CHANGE PIN                                                      ")
speak("3. balance inquiry . 4 change pin")
print(".......................................................................................................................................")

said = inputcommand()

#code for withdrawing money

if "cash withdrawal" in said.lower() or "withdraw some cash" in said.lower() or "withdraw cash" in said.lower() :
    speak("YOU HAVE CHOSEN TO WITHDRAW CASH")
    print(" ENTER DENOMINATION :")
    speak("ENTER THE AMOUNT YOU WANT TO WITHDRAW")
    
    with open("c:\\Users\\avime\\Desktop\\PROJECTS\\ATM FOR BLIND\\Accounts.csv",'r') as file:
        t=1
        reader=csv.reader(file , delimiter=',')
        l=[]
        for i in reader:
            l.append(i)
        for i in l :
            i[1]=int(i[1])
            i[2]=float(i[2])
    
    trs=0
    for i in l :
        if i[1]==int(pin):
            print(i[2])
            while True :
                amnt= int(input())
                if amnt > i[2]:
                    speak("THE AMOUNT U WISH TO WITHRDRAW EXCEEDS YOUR BALANCE")
                    speak("PLEASE ENTER A VALID AMOUNT ")
                    trs= trs+1
                    if trs==3 :
                        speak("YOU HAVE EXCEEDED THE NUMBER OF TRIES ")
                        print("EXCEEDED THE LIMIT OF TRIES ")
                        exit()
                elif amnt < i[2]:
                    break    

            i[2]-=amnt
            print(i[2])
            t=0           
    print(l)

    file=open("c:\\Users\\avime\\Desktop\\PROJECTS\\ATM FOR BLIND\\Accounts.csv",'w',newline='')
    writer=csv.writer(file,delimiter=',')
    for i in range(len(l)):
        writer.writerow(l[i])
    file.close() 
    speak("YOUR TRANSACTION HAS BEEN DONE SUCCESSFULLY")

    speak("WOULD YOU LIKE TO KNOW YOUR BALANCE ?")
    rep=inputcommand()

    if "yes" in rep.lower() or "yes please" in rep.lower() or "yes show me my balance" in rep.lower() or "yes show me my balance" in rep.lower() :
        with open("c:\\Users\\avime\\Desktop\\PROJECTS\\ATM FOR BLIND\\Accounts.csv",'r') as file:
            reader=csv.reader(file,delimiter=',')
            a=[]
            for i in reader:
                a.append(i)

            for i in a :
                if i[1]==int(pin):
                    speak("YOUR BALANCE IS ")
                    speak(i[2])
                    print("YOUR BALANCE IS : ",i[2])
                     
    else :
        file.close()
        speak("OK , THANK YOU, COME AGAIN")
        exit()

#CODE FOR DEPOSITING MONEY 

elif "cash deposit" in said.lower() or "deposit some cash" in said.lower() or "deposit cash" in said.lower():
    speak("YOU HAVE CHOSEN TO DEPOSIT CASH ")
    speak("ENTER THE AMOUNT TO BE DEPOSITED")
    depo=int(input("ENTER AMOUNT TO BE DEPOSITED : "))

    with open("c:\\Users\\avime\\Desktop\\PROJECTS\\ATM FOR BLIND\\Accounts.csv",'r') as file:          #enter your own path
        t=1
        reader=csv.reader(file , delimiter=',')
        l=[]
        for i in reader:
            l.append(i)
        for i in l:
            i[1]=int(i[1])
            i[2]=float(i[2])

        for i in l:
            if i[1]==int(pin):
                while True  :
                    if depo > 20000 :
                        print("PLEASE ENTER VALID AMOUNT TO DEPOSIT : ")
                        speak("THE AMOUNT YOU WANT TO DEPOSIT EXCEEDS THE LIMIT")
                        speak("PLEASE ENTER AGAIN")
                        depo=int(input())
                    else :
                        break    
                i[2]+=depo
                t=0
                                

# NEW AND UPDATED BALANCE CHANGE IN THE CSV FILE

    file=open("c:\\Users\\avime\\Desktop\\PROJECTS\\ATM FOR BLIND\\Accounts.csv",'w',newline='')
    writer=csv.writer(file,delimiter=',')
    for i in range(len(l)):
        writer.writerow(l[i])
    file.close()
    
    speak("YOUR TRANSACTION HAS BEEN SUCCESSFULLY DONE")
    speak("WOULD YOU LIKE TO KNOW YOUR BALANCE ?")
    chk = inputcommand()
    if "no" in chk.lower() or "no thank you" in chk.lower() :
        speak("THANK YOU, COME AGAIN")
        exit()
    else:
        with open("c:\\Users\\avime\\Desktop\\PROJECTS\\ATM FOR BLIND\\Accounts.csv",'r') as file:
            reader=csv.reader(file,delimiter=',')
            a=[]            
            for i in reader:
                a.append(i)

            for i in a :
                if i[1]==int(pin):
                    speak("YOUR BALANCE IS ")
                    speak(i[2])
                    print("YOUR BALANCE IS : ",i[2])

        speak("THANK YOU, COME AGAIN")
        exit()    

# BALANCE CHECK CODE        
            
elif "like to know balance" in said.lower() or "balance inquiry" in said.lower() :
    speak("YOU HAVE SELECTED TO CHECK YOU BALANCE ")
    with open("c:\\Users\\avime\\Desktop\\PROJECTS\\ATM FOR BLIND\\Accounts.csv",'r') as file:
            reader=csv.reader(file,delimiter=',')
            a=[]
            for i in reader:
                a.append(i)

            for i in a :
                if i[1]==int(pin) and i[3] == accno :
                    speak("YOUR BALANCE IS ")
                    speak(i[2])
                    print("YOUR BALANCE IS : ",i[2])
    

#CHANGE PIN CODE

elif "i would like to change my pin" in said.lower() or "change pin" in said.lower() :

    speak("YOU HAVE CHOSEN TO CHANGE YOUR PIN")
    speak("PLEASE ENTER YOUR OLD PIN")
    print("PLEASE ENTER YOUR OLD PIN : ")
    div=0
    f=1
    while f==1 :
        olpin= getpass_ak.getpass()
        if int(olpin) != int(pin) :
            speak("YOUR PIN DOES NOT MATCH PLEASE RE-ENTER")
            print("THE PIN YOU ENTERED DOES NOT MATCH")
            div=div+1
            if div==3:
                speak("YOU HAVE EXCEEDED THE NUMBER OF ATTEMPTS ")
                exit()
        else:  
            ptry=0      
            while f==1:        
                print("ENTER YOUR NEW PIN ")
                speak("ENTER YOUR NEW PIN ")
                npin=getpass_ak.getpass()
                if npin.isdigit() and len(npin)==4:
                    speak("RE-ENTER YOUR NEW PIN TO CONFIRM")
                    print("RE-ENTER YOUR NEW PIN TO CONFIRM CHANGE :")
                    n2pin= getpass_ak.getpass()
                    if n2pin.isdigit() and len(n2pin)==4:                      # PIN CHECK
                        if npin == n2pin :
                            
                            with open("c:\\Users\\avime\\Desktop\\PROJECTS\\ATM FOR BLIND\\Accounts.csv",'r') as file:
                                reader=csv.reader(file , delimiter=',')
                                l=[]
                                for i in reader:
                                    l.append(i)
                                for i in l:
                                    i[1]=int(i[1])
                                    i[2]=float(i[2])
                                    if i[1]==int(olpin) and i[3] == accno :                 # WRONG PIN CAN ONLY BE ENETERED MAX 3 TIMES 
                                        i[1]== int(npin)                                    # EXCEEDING 3 TIMES , WILL CAUSE EXIT OF PROGRAM 
                                        f==0
                                        
                                        speak("YOUR PIN HAS BEEN CHANGED ")
                                        print("YOU HAVE SUCCESSFULLY CHANGED YOUT PIN ")
                                        speak("THANK YOU , COME AGAIN !")
                            file=open("c:\\Users\\avime\\Desktop\\PROJECTS\\ATM FOR BLIND\\Accounts.csv",'w',newline='')
                            writer=csv.writer(file,delimiter=',')
                            for i in range(len(l)):
                                writer.writerow(l[i])
                            file.close()
                            exit()            
                                   
                        else :
                            speak("THE PIN DOES NOT MATCH ")
                            speak("PLEASE TRY AGAIN ")
                            ptry = ptry + 1
                            if ptry == 3 :
                                speak("YOU HAVE EXCEEDED THE NUMBER OF TRIES ")
                                print("THE NUMBER OF TRIES HAS EXHAUSTED ")
                                exit()
                            print("THE ENTERED PIN DOES NOT MATCH , PLEASE TRY AGAIN")                

    speak("YOUR PIN HAS BEEN CHANGED ")
    print("YOU HAVE SUCCESSFULLY CHANGED YOUT PIN ")
    speak("THANK YOU , COME AGAIN !")
    
    exit()


else :
    speak("SORRY , THE COMMAND IS NOT RECOGNIZED , YOU WILL BE TAKEN BACK TO THE HOMESCREEN")