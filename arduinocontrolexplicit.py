import arduinointerference as ai

while True:
    c=input("Enter the command : ")

    if c == 'states':
        for i in range (0,14):
            if(i<10):
                print(i,'-',ai.state[i],end=' || ')
            else:
                tmp=chr(i+55)
                print(tmp,':',i, '-', ai.state[i], end=' || ')
        print()

    elif len(c) == 2 and (c[0] == 'u' or c[0] == 'd' or c[0] == 's') and (c[1] == '0' or c[1] == '1'
            or c[1] == '2' or c[1] == '3' or c[1] == '4' or c[1] == '5' or c[1] == '6' or c[1] == '7'
            or c[1] == '8' or c[1] == '9' or c[1] == 'A' or c[1] == 'B' or c[1] == 'C' or c[1] == 'D'):
        ai.command(c)

    else:
        print('INVALID COMMAND !!!')
