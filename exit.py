from main1 import swg1
def exit():
    try :
        x1 = int(input("\nDo you want to continue or exit\nPress 1 to continue and 0 to exit :"))
        if (x1 == 1):
         print("\n\n")
         
         swg1()
        if (x1 == 0):
         print("OK you are exited\n\nThankyou")
        #  breakpoint
        # else :
        #   print("Please input properly")
        #    
        #   exit()
    except ValueError :
        print("Please input properly")
        swg1()
    except KeyError :
        print("Please input properly")
        swg1()
# exit()