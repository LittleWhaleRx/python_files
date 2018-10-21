print('red','yello','green')
for red in range(1,4):
    for yello in range(1,4):
        for green in range(2,8):
            if red+yello+green==8:
                print('red='+str(red),'yello='+str(yello),'green='+str(green))