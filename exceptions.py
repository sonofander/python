tuna = input("whats your fav number?\n")
int(tuna)
print(tuna)

#will error because a person may put "ummm"

while True:
    try:
        tuna = input("whats your fav number?\n")
        int(tuna)/1
        break
        #break to restart the question after exception is thrown
    except ValueError:
        print("that is not a number\n")
    except ZeroDivisionError:
        print("dont pick zero\n")
    except:
        break
    finally:
        ##no matter if the could worked, execute this code no matter what
        print("loop complete")
        
