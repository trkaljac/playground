def main():
question = input("What time it is ? ")
 time = time.convert(question)
if time >=7 and time<=8:
    print("brekfest time")
elif time >=12 and time <=13:
    print("lunch time")
elif time>=18 and time <=19:
    print("dinner time")


def convert(time):
    ...
hours, minutes = time.split(":")
hours = float(hours)
con_minutes = float(minutes) / 60
time = hours + con_minutes
return time


if __name__ == "__main__":
    main()