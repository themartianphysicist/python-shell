print("Welcome to python shell created by Kartikaye Rishi")
run = True
while run:
        x = input(">>> ")
        try:
            exec(x)
        except Exception as e:
            print(e)

