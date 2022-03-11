from datetime import datetime


def todayPren_resp(input_text):
    print("ok")
    user_msg = str(input_text).lower()

    if user_msg in "time":
        now=datetime.now()
        date_time=now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    if user_msg in "prenota":
        print("ok if")
        day = datetime.today().weekday()
        print(f"Oggi è {day}")
        if day in (0, 1, 2):
            print("è il giorno giusto")
            return "aula p1.2"
        else:
            if day in 3:
                return "aula M1.2"
            else:
                return "Lab LINFA P2.6"
    return "Cazzo ne so io!"

