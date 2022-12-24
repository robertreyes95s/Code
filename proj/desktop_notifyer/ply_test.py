import time
from plyer import notification
import plyer

bat_value = 40
while bat_value <= 35: 
    battery = plyer.battery.status
    for name, value in battery.items():
        bat_value = value
        if bat_value == 36: 
            print(bat_value)
            break
    
     
if __name__=="__main__":
 
        notification.notify(
           title = "HEADING HERE",
            message=" DESCRIPTION HERE" ,
           
            # displaying time
            timeout=2
)
        # waiting time
        time.sleep(7)