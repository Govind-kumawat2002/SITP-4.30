name = input("Plz Enter your Name:-")
print(f"Hello {name}")
print("How may i help you","\n")
message = """please select any of them option
Type 1 >>>>>>>>>> Check Balance, 
Type 2 >>>>>>>>>> Deposit, 
Type 3 >>>>>>>>>> Withdrawl"""

print(message,"\n")
task=int(input("Enter your option:-"))

avaiable_amount = 10000
if(task>=1) & (task<=3):
    if task ==1:
        ##### ye program check balance
        balance_message = f"Thank for visiting ! your avaiable balance is:-INR{avaiable_amount}"
        print(balance_message)
    elif task ==2:
        ###  program for deposit
        deposit_amount=int(input("Enter your deposit ammount")) 
        if deposit_amount>0:
            avaiable_amount+=deposit_amount    ##### x+=3 = x+3
            deposit_message = f"You have successfully deposit your money {deposit_amount}"
            balance_message= f"Thanks for visiting ! your availabe balance is :INR{avaiable_amount}"
            print(deposit_message)
            print("\n")
            print(balance_message)
        else:
            print("plz enter valid number")
    else:
        ###program for withrawl
        withdrwl_amount=int(input("Enter amount"))  ### 5000 av = 10000
        if withdrwl_amount<=avaiable_amount:
            if withdrwl_amount>0:
                avaiable_amount-=withdrwl_amount
                withdrwl_amount_message = f"You have successfully Withdrwl your money {withdrwl_amount}"
                balance_message= f"Thanks for visiting ! your availabe balance is :INR{avaiable_amount}"
                print(withdrwl_amount_message)
                print("\n")
                print(balance_message)
            else:
                print("Plz enter valid number")
        else:
            withdrwl_messsage_warning="ki bhai aapke pass ete pese nhi"
            balance_message=f"Thank for visiting ! your available balance {avaiable_amount}"
            print(withdrwl_messsage_warning)
            print("\n")
            print(balance_message)
else:
    print("plz correct input")
