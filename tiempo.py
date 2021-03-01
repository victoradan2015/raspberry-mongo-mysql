from datetime import datetime

class tiempo:
    def capturar():
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        return current_time
        #print("Current Time =", current_time)
