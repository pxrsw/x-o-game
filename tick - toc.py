

##besmellah ...
def get_name():
    first_name = input ("ENTER FIRST NAME\n")
    second_name =input ("ENTER SECOND NAME\n")
    print("WELCOME " +first_name +"  "+second_name)
#----------------------------------------------------------
def insert_item(item , index):
    list[int(index)] = item
#----------------------------------------------------------
def specify(round):
    if round%2 == 0:
        return "X"
    else :
        return "*"
#----------------------------------------------------------
def get_item ():
    item = input("ENTER A INDEX FOR YOUR SIGN\n")
    print (str(list[int(item)]))
    if str(list[int(item)]) == "0":
        return item
        print("HELOOOOO")
    else : 
        print(" SORRY \n THIS INDEX IS FULL !\n")
        get_item()
#---------------------------------------------------------
def printing (list):
    print("\n")
    print ("     "+str(list[0]) + "     |" + "     "+str(list[1])+"     " + "|" + "     "+str(list[2]) )
    print("\n")
    print("-----------------------------------------------------------------------")
    
    
    print("\n")
    print ("     "+str(list[3]) + "     |" + "     "+str(list[4])+"     " + "|" + "     "+str(list[5]) )
    print("\n")
    print("-----------------------------------------------------------------------")
    
    print("\n")
    print ("     "+str(list[6]) + "     |" + "     "+str(list[7])+"     " + "|" + "     "+str(list[8]) )
    print("\n")
        
#------------------------------------------------------------------------------------------
def check_winning():
    
    if  list[0]  == list[1] == list[2]  == "X"  or  list[3]  == list[4] == list[5]   =="X" or list[6]  == list[7] == list[8]  =="X"  or list[0]  == list[3] == list[6]  =="X"  or list[1]  == list[4] == list[7]   =="X"  or list[2]  == list[5] == list[8]   =="X"    or list[0]  == list[4] == list[8]   =="X"  or list[3]  == list[4] == list[6]  =="X" :
        print("\n")
        print("          AFARIIIIIIIIIIN   XX    ")
        print("\n")
        return True
    return False


    if  list[0]  == list[1] == list[2] =="*"   or  list[3]  == list[4] == list[5] =="*" or list[6]  == list[7] == list[8] =="*"  or list[0]  == list[3] == list[6] =="*"  or list[1]  == list[4] == list[7]  =="*"  or list[2]  == list[5] == list[8]  =="*"    or list[0]  == list[4] == list[8]  =="*"   or list[3]  == list[4] == list[6] =="*" :
        print("\n")
        print("          AFARIIIIIIIIIIN   **    ")
        print("\n")
        return True
    return False


def game():
     list = [0,0,0,0,0,0,0,0,0]

     round =0
     get_name()
    
     while True :
        
        insert_item(specify(round) , get_item())
        printing(list)
        if check_winning():
            break
        round = round +1