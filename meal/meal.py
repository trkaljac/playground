def main():
question = input("What time it is ? ")
    #convert function time = time.convert(question)
    #breakfast7:00 to 8:00   if time >=7 and time<=8:
                            print("brekfest time")
    #lunch12:00 13:00       elif time >=12 and time <=13:
                            print("lunch time")
    #dinner18:00 19:00      elif time>=18 and time <=19:
                            print("dinner time")


def convert(time):
    ...
#get hours and minuts hours, minutes = time.split(":")
#convtr to a float hours = float(hours)
    #minutes = float(minutes) / 60
    #time = hours + minutes
    #return time
#return the resolt to main function

if __name__ == "__main__":
    main()