
def A_squ():
    side=int(input("enter length of side"))
    result=side**2
    print("Area of Square is :",result)

def A_tri():
    side1 = int(input("enter length of first side"))
    side2 = int(input("enter length of second side"))
    side3 = int(input("enter length of third side"))
    result=side1+side2+side3
    print("Area of Triangle is:",result)



def A_Para():
    base=int(input("enter length of base"))
    height=int(input("enter height length"))
    result=base*height
    print("Area of Parallelogram is:",result)

def A_Rec():
    l=int(input("enter of rectangle"))
    w=int(input("enter width of rectangle"))
    result=(l*w)
    print("Area of Rectangle is:",result)





def A_Cir():
    radius=int(input("enter diameter of circle"))
    result=(2*3.142*radius)
    print("Area of circle is:",result)

ask2="yes"
print("******WELCOME TO AREA CALCULATOR*******")
def main():
    global ask2
    ask = input("enter name of shape,")

    if ask=="square":
        A_squ()

    if ask=="Rectangle":
        A_Rec()

    if ask=="circle":
        A_Cir()


    if ask=="parallelogram":
        A_Para()

    if ask=="triangle":
        A_tri()

    ask2=input("do you want to calculate other shape area")
while ask2=="yes":
    main()
else:
    print("thank you for using this app")
