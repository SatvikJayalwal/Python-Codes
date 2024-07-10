coffee_counter=500
water_counter=540
milk_counter=600
while True:
    
  user_inp=input("""What would you like? (espresso/latte/cappuccino)\nPlease Enter (e/l/c/off/report) : """)
  
  print("The user entered : ",user_inp)

  if user_inp=="report":
    print("Water: 100ml\nMilk: 50ml\nCoffee: 76g\nMoney: $2.5")
    break

  elif user_inp=="off":
    print("The coffee machine is closed")
    break
  
  elif user_inp=="e":

    if water_counter >=50 & coffee_counter >=18:
      user_inp_e=int(input("You have to pay 10$ : "))
      if user_inp_e==10:
        print("Here is your Espresso!")
      elif user_inp_e>10:
        print("Here is your Espresso and :",user_inp_e-10,"$ change")

      elif user_inp_e<10:
        print("Sorry you have to pay ",10-user_inp_e,"$ more!")

    elif user_inp=="l":     

        if water_counter >=200 & coffee_counter >=24 & milk_counter>=150: 

          user_inp_l=int(input("You have to pay 50$ : "))  
          if user_inp_l==50:
            print("Here is your Latte!")

          elif user_inp_l>50:
            print("Here is your Latte and :",user_inp_e-50,"$ change")

          elif user_inp_e<50:
            print("Sorry you have to pay ",50-user_inp_e,"$ more!")
          

    elif user_inp=="c":     

        if water_counter >=250 & coffee_counter >=24 & milk_counter>=100:    
          user_inp_c=int(input("You have to pay 100$ : "))
            
          if user_inp_l==100:
            print("Here is your Cappuccino!")

          elif user_inp_l>100:
            print("Here is your Cappuccino and :",user_inp_e-100,"$ change")

          elif user_inp_e<100:
            print("Sorry you have to pay ",100-user_inp_e,"$ more!")






    

    