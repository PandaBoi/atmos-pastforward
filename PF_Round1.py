from Arduino import Arduino
import time


class PF():

    def __init__(self):
    
        self.board = Arduino('9600', port="/dev/ttyACM0") #plugged in via USB, serial com at rate 9600
        self.board.pinMode(5, "INPUT")#entry gate sensor
       
        self.Round1_time = 0
        self.switches= [5,9,8,1,3,4,6,7,2,10] # pins of switches
        self.doors = [11,13,12,14,15,16,17,18,19,20] #write pins of gates
        
        #self.time = [[]*10]


    def Round1(self):
        
        while True:

            

            val = self.board.digitalRead(5)

            #main working loop
            while(val==0):
            
                    val = self.board.digitalRead(5)
                    Display_Doors()

                   
                      
                       
            break

    def Display_Times(self, time_no = "None"):

        if time_no == "Round_1":
            print("Round1_time: " + str(self.Round1_time) )
   
    def Display_Doors(self):

        for (i,switch) in enumerate(self.switches):
            while(self.board.digitalRead(switch) == HIGH):
                #display switch gate correspondence
                self.board.digitalWrite(self.doors[i]) == HIGH 
                


inst = PF()

#time start
start = time.time()
inst.Round1()
#time stop
end = time.time()

inst.Round1_time = end - start

inst.Display_Times("Round_1")
