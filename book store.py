
import mysql.connector as mycon
cn = mycon.connect(host='localhost',user='root',password="dav",database="school")
cur = cn.cursor()

def showAllBooks():
    
    global cn
    global cur
    
    
    try:
            query="select * from BookList"
            cur.execute(query)
            results = cur.fetchall()
            print("*****************************************************************")
            print('%5s'%"ID",'%10s'%'NAME','%10s'%'AUTHOR','%10s'%'PRICE','%10s'%'QUANTITY','%10s'%'GENRE')
            print("*****************************************************************")
            count=0
            for row in results:
                print('%5s' % row[0],'%10s'%row[1],'%10s'%row[2],'%10s'%row[3],'%10s'%row[4],'%10s'%row[5])
                count+=1
            print("*************** TOTAL RECORD : ",count,"*********************")
        
    except:
        print("error")
        
def sugBook():
    global cn,cur
    print("*******************GIVE BOOK SUGGESTIONS**************************")
    
    
    en = input("Enter Book name :")
    dp = input("Enter Author :")
    sl = (input("Enter Genre :"))
    
    print("\n ## THANK YOU FOR YOUR SUGGESTION!")
    
def addBook():
    global cn,cur
    e=input("enter password")
    if e=='abc123':
        f=input("DO YOU WANT TO ADD BOOK??")
        print("*******************ADD NEW BOOK**************************")
        k= int(input("Enter Book ID :"))
        d= input("Enter Book name :")
        f= input("Enter Author name :")
        s=int(input("Enter price :"))
        z=int(input("Enter Quantity :"))
        m=input("Enter Genre :")
        query="insert into booklist values({},'{}','{}',{},{},'{}')".format(k,d,f,s,z,m)
        cur.execute(query)
        cn.commit()
        print("\n ## RECORD ADDED SUCCESSFULLY!")
    else:
        print("PASSWORD INCORRECT")
    
def searchBook():
    global cn,cur
    print("*******************SEARCH BOOK FORM **************************")
    en = (input("Enter Book Id to search :"))
    query="select * from booklist where b_id='%s'"%(en,)
    cur.execute(query)
    results = cur.fetchall()
    if cur.rowcount<=0:
        print("\## SORRY! NO MATCHING DETAILS AVAILABLE ##")
    else:
       
        print("**************************************************")
        print('%5s'%"ID",'%10s'%'NAME','%10s'%'AUTHOR','%10s'%'PRICE','%10s'%'QUANTITY','%10s'%'GENRE')
        print("**************************************************")
        for row in results:
            print('%5s' % row[0],'%10s'%row[1],'%10s'%row[2],'%10s'%row[3],'%10s'%row[4],'%10s'%row[5])
    print("-"*50)
                
def delBook():
    global cn,cur
    e=input("enter password")
    if e=='abc1234':
        f=input("DO YOU WANT TO DELETE A BOOK?? ")
        if f=='y' or f=='Y':
            print("*******************DELETE BOOK FORM**************************")
            en = int(input("Enter Book Id to delete :"))
            query="select * from booklist where b_id={}".format(en,)
            cur.execute(query)
            results = cur.fetchall()
            if cur.rowcount<=0:
                print("\## SORRY! NO MATCHING DETAILS AVAILABLE ##")
        print("-"*50)
        ans = input("Are you sure to delete ? (y/n)")
        if ans=="y" or ans=="Y":
            query="delete from booklist where b_id={}".format(en,)
            cur.execute(query)
            cn.commit()
            print("\n## RECORD DELETED  ##")

        
def clear():
      for i in range(1,50):
          print()
          
def generateSlip():

    global cn,cur
    print("******************* RECIEPT **************************")
    w=0
    en = int(input("Enter Book id to print salary slip :"))
    query="select * from booklist where b_id={}".format(en,)
    cur.execute(query)
    results = cur.fetchall()
    print(results)
    if cur.rowcount<=0:
       print("\## SORRY! NO MATCHING DETAILS AVAILABLE ##")
    else:
        clear()
        for i in (results):
            j=int(input('enter no of copies to be taken'))
            print("BOOK ID:",results[0][0]," "*20,"BOOK NAME :",results[0][1])
            print("PRICE :",results[0][3],""*20,'QUANTITY :',j)
            print("*"*50)
            s = int(results[0][3])
            
            da = s * j
            w=w+da
            print("%19s"%"RECIEPT")
            print("-------------------------------------------------")
            print(""*20,"Item purchased :",results[0][1],""*22,"Item Price:",results[0][3])
                    
        

            
        print("-"*50)
        print("     TOTAL PRICE :",w)
    print("-"*50)
    print("=== PRESS ANY KEY ===")
    input()
        
while True:
    print("1. SHOW BOOKLIST")
    print("2. GIVE BOOK SUGGESTION")
    print("3. ADD DATA")
    print("4. SEARCH BOOK ")
    
    print("5. DELETE BOOK ")
    print("6. GENERATE PAY SLIP ")
    print("7. CONTACT US")
    print("0. EXIT")
    ans = int(input("Enter your choice :"))
    if ans==1:
        showAllBooks()
    elif ans==2:
        sugBook()
    elif ans==3:
        addBook()
    elif ans==4:
        searchBook()
    elif ans==5:
        delBook()
   
    elif ans==6:
        generateSlip()
    elif ans==7:
        print("*"*60)
        print(" "*20,"OWNER : Purva & Riya Co. Ltd. ")
        print(" "*20,"EMAIL  : purva&riya@gmail.com")
        print("*"*60)
    elif ans==0:
        print("\nBye!!")
        cn.close()
        break
