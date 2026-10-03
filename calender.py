import calender
from datetime import datetime

def my_calender():
    abhi = datetime.now()
    saal = abhi.year
    mahina = abhi.month

    print(f"--- {saal} ka calender ---\n")
    cal = calender.textcalender()
    cal.prmonth(saal, mahina)

    print("\npoora saal dekhna hain?")
    choice = input("y / n likho: ")
    if choice.lower() == "y":
        print(calender.calender(saal))
        my_calender()