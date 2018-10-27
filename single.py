from Arduino import Arduino
import time
board = Arduino('9600')  # plugged in via USB, serial com at rate 9600


board.Servos.attach(2, min = 1000, max = 1000)
board.Servos.attach(3, min = 1000, max = 1000)
board.Servos.attach(4, min = 1000, max = 1000)
board.Servos.attach(5, min = 1000, max = 1000)
board.Servos.attach(6, min = 1000, max = 1000)
board.Servos.attach(7, min = 1000, max = 1000)
board.Servos.attach(8, min = 1000, max = 1000)
board.Servos.attach(9, min = 1000, max = 1000) 
board.Servos.attach(10, min = 1000, max = 1000)
board.Servos.attach(11, min = 1000, max = 1000)

# for i in range(2,12):
#     angle = board.Servos.read(i)
#     while angle <= 70:

#         board.Servos.write(i,++angle)
#         time.sleep(0.01)

gates = [7,10,6,5,4,2,8,3,11,9]


def servoClose(pin):

    if pin in [7,8,9,10]:
        board.Servos.write(pin, 170)

    else:
        board.Servos.write(pin, 10)

def openAllGates():

    for gate in gates:
        board.Servos.write(gate, 90)

def closeAllGates():

    for gate in gates:
        servoClose(gate)

        


# while True:
#     for i in range(0,71,2):
#         for x in range(2,12):
#             board.Servos.write(x,70 - i)
#             time.sleep(0.008)
#         #board.Servos.write(x,10)
#         #time.sleep(2)
#     #time.sleep(1)
    
#     for i in range(0,71,2):
#         for x in range(2,12):
#             board.Servos.write(x,i)
#             time.sleep(0.008)
        
#     time.sleep(1)



while True:
    
    board.Servos.write(0, 90)
    time.sleep(2)
    servoClose(0)
    time.sleep(2)



#to get to x
# while True:
#     x =20
#     for i in range(2,12):
#         board.Servos.write(i,x)                                                                                                               


