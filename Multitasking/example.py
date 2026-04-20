import threading
import time
class ThreadExample:
    def __init__(self,name):
        self.name = name
    def player(self):
        for i in range(1,11):
            print(f'{self.name} Played at {i} time')
            time.sleep(3)
            
t1 = ThreadExample('vijay')
t2 = ThreadExample('kiran')
 
t3 = ThreadExample('Raj')

th1 = threading.Thread(target=t1.player,name='First') # unstarted state of a thread
th2 = threading.Thread(target=t2.player,name="Second") 
th3 = threading.Thread(target=t3.player,name="third") 
th1.start() #Ready state or runable state
th1.join(15)
th2.start()
th3.start()






# Demon threads ThreadScheduler(Predfined thread)