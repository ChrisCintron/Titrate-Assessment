#!/usr/bin/env python3


import time
import tkinter as tk
import random
import xlwt
from tkinter.filedialog import askdirectory


class EntryScreen:
    print("Entry Screen Initiating..")


    my_time = int()
    my_choice_time = int()
    my_candy_time = int()
    my_reverse = int()
    num_of_trials = int()

    def __init__(self, master):
        master.title("Gideon's Behavioral Experiment: Titrating Task")
        master.geometry("900x500+200+100")

        self.master = master


        self.frame1 = tk.Frame(master)
        self.frame1.pack(fill="both", expand=True)

        self.number_of_trials_label = tk.Label(self.frame1, text="Number of Trials")
        self.number_of_trials_Entry = tk.Entry(self.frame1)

        self.time_label = tk.Label(self.frame1, text="Initial time for neutral Button")
        self.time_Entry = tk.Entry(self.frame1)

        self.choice_time_label = tk.Label(self.frame1, text="Choice time delay")
        self.choice_time_entry = tk.Entry(self.frame1)

        self.candy_time_label = tk.Label(self.frame1, text="Candy Image time delay")
        self.candy_time_entry = tk.Entry(self.frame1)

        self.Reverse_the_Trial = tk.Label(self.frame1, text="Reverse the Trial? 1 for No, 2 for Yes")
        self.Reverse_the_Trial_Entry = tk.Entry(self.frame1)

        self.packall()
        save_me = tk.Button(self.frame1, text="Ready", command=self.entry_get)
        save_me.pack(side="bottom")
        print("Entry Screen Completed, Ready to run.")

    def packall(self):
        self.number_of_trials_label.pack()
        self.number_of_trials_Entry.pack()
        self.time_label.pack()
        self.time_Entry.pack()
        self.choice_time_label.pack()
        self.choice_time_entry.pack()
        self.candy_time_label.pack()
        self.candy_time_entry.pack()
        self.Reverse_the_Trial.pack()
        self.Reverse_the_Trial_Entry.pack()

    def entry_get(self):
        EntryScreen.my_time = int(self.time_Entry.get())
        EntryScreen.num_of_trials = int(self.number_of_trials_Entry.get())
        EntryScreen.my_choice_time = int(self.choice_time_entry.get())
        EntryScreen.my_candy_time = int(self.candy_time_entry.get())
        EntryScreen.my_reverse = int(self.Reverse_the_Trial_Entry.get())
        self.master.destroy()



class App:

    temp = EntryScreen.my_time
    def __init__(self, master):
        self.global_timer = EntryScreen.my_time
        self.my_titrate = EntryScreen.my_time
        master.geometry("900x500+200+100")
        master.title("Gideon's Behavioral Experiment")

        self.master = master
        self.frame0 = tk.Frame(master)
        self.frame1 = tk.Frame(master)
        self.frame2 = tk.Frame(master)

        #___CHANGE FILE NAMES HERE___
        self.object0_file = "button0.gif"
        if EntryScreen.my_reverse == 1:
            self.object1_file = "blue_button.gif"
            self.object2_file = "red_button.gif"
        elif EntryScreen.my_reverse == 2:
            self.object1_file = "red_button.gif_256"
            self.object2_file = "blue_button.gif_256"
        self.candy_file = "candy.gif"

        #__________________________

        self.button0_photo = tk.PhotoImage(file=self.object0_file)
        self.button1_photo = tk.PhotoImage(file=self.object1_file)
        self.button2_photo = tk.PhotoImage(file=self.object2_file)
        self.candy_photo = tk.PhotoImage(file=self.candy_file)

        #Photo packing
        #self.photo0 = tk.Label(self.frame0, image=self.button0_photo)
        #self.photo1 = tk.Label(self.frame1, image=self.button1_photo)
        #self.photo2 = tk.Label(self.frame2, image=self.button2_photo)

        self.candy1 = tk.Label(self.frame1, image=self.candy_photo)
        self.candy2 = tk.Label(self.frame2, image=self.candy_photo)


        #My controllers
        self.photo0 = tk.Button(self.frame0, image=self.button0_photo, command=self.my_controller_v0)

        self.photo1 = tk.Button(self.frame1, image=self.button1_photo, command=self.my_controller_v1)

        self.photo2 = tk.Button(self.frame2, image=self.button2_photo, command=self.my_controller_v2)

        self.training_trials = 4 #how many total trainings required. Keep this even
        self.trainings_completed = 0

        print("App Completed, Ready to run.")
        self.number_of_trials = EntryScreen.num_of_trials
        self.TrialNumber = 0
        self.count = 0 #Change to 4 to skip training, 0 for normal.
        self.object1_count = str()
        self.object2_count = str()
        self.start_training()

    def start_trial(self):
        self.TrialNumber += 1
        if self.TrialNumber > self.number_of_trials:
            self.master.destroy()
        print("")
        print("_____________________")
        print("Trial({}) is starting".format(self.TrialNumber))

        self.button_packer(0)



    def start_training(self): #The interface before every change
    #Checks the start_training number, and presents user with proper interface
        #print("__Squence start__")
        print("")
        print("")
        print ("Training Session({}):".format(self.trainings_completed + 1))
        self.my_titrate = EntryScreen.my_time

        if (self.trainings_completed < (self.training_trials/2)):
            self.button_packer(1)
        elif (self.trainings_completed < self.training_trials):
            self.button_packer(2)
        elif (self.trainings_completed >= self.training_trials):
            self.start_trial()
        else:
            print("Something in (start_training) went wrong")
        self.trainings_completed += 1


    def my_controller_v0(self):
        self.object_0(self)

    def my_controller_v1(self):
        self.object_1(self)

    def my_controller_v2(self):
        self.object_2(self)


    def button_packer(self, buttonID): #ASK GIDEON about button placement?


        if (buttonID == 0):

            self.frame0.pack()
            self.photo0.pack()
        elif (buttonID == 1):
            self.frame1.pack(side="left")
            self.photo1.pack()
        elif (buttonID == 2):
            self.frame2.pack(side='right')
            self.photo2.pack()
        elif (buttonID == 3):
            self.frame1.pack(side="left", fill="both", expand=True)
            self.frame2.pack(side="right", fill="both", expand=True)
            self.photo1.pack(side="left")
            self.photo2.pack(side='right')
        else:
            print("Error, something went wrong")


    def forget_all(self):

        #frames
        self.frame0.forget()
        self.frame1.forget()
        self.frame2.forget()
        self.master.update()

        #labels
        self.photo0.forget()
        self.photo1.forget()
        self.photo2.forget()
        self.master.update()


    def timed_sleep(self): #Adjust sleep according to the titrate
        print("Button0 asleep for {} seconds: ".format(self.global_timer))
        time.sleep(self.global_timer)

    def normal_sleep(self): #Sleep for the amount of time given.
        print("Main buttons asleep for {} seconds".format(EntryScreen.my_choice_time))
        time.sleep(EntryScreen.my_choice_time)


    def titrate(self, switch):
        self.my_titrate /= 2.0
        if switch == 1:
            self.global_timer += self.my_titrate
            print("My titrate is (+) {}".format(self.my_titrate))

        elif switch == 2:
            self.global_timer -= self.my_titrate
            print("My titrate is (-) {}".format(self.my_titrate))


    def end_trial(self):
        self.forget_all()

        if (self.TrialNumber == 0):
            self.start_training()
        else:

            self.button_packer(0)
            self.xlx_results()
            self.object1_count = str()
            self.object2_count = str()
            self.start_trial()
            self.master.update()



    #MY BUTTON OBJECTS
    def object_0(self,event):
        App.temp = self.global_timer
        self.forget_all()
        self.master.update()
        self.timed_sleep()
        self.master.update()
        self.button_packer(3) # Packs left and right frames and buttons
        #self.button_packer(2)
        self.object1_count, self.object2_count = '',''


    def object_1(self,event):
        #self.unbind_all()
        print("<Left> button was pressed")
        self.titrate(1)
        self.forget_all()
        self.master.update()
        self.normal_sleep()
        self.master.update()
        self.candyobject1() #NEW
        self.object1_count = 'x'
        self.end_trial()


    def object_2(self,event):
        print("<Right> button was pressed")
        self.titrate(2)
        self.forget_all()
        self.candyobject2() #NEW
        self.normal_sleep()
        self.object2_count = 'x'
        self.end_trial()


    def candyobject1(self):

        self.frame1.pack(side='left')
        self.candy1.pack()
        self.master.update()

        print("Candy asleep for {} second(s)".format(EntryScreen.my_candy_time))
        time.sleep(EntryScreen.my_candy_time)

        self.candy1.forget()
        self.forget_all()
        self.master.update()

    def candyobject2(self):

        self.frame2.pack(side='right')
        self.candy2.pack()
        self.master.update()

        print("Candy asleep for {} second(s)".format(EntryScreen.my_candy_time))
        time.sleep(EntryScreen.my_candy_time)
        self.candy2.forget()
        self.forget_all()
        self.master.update()


    def xlx_results(self):
        if self.TrialNumber == 1:
            self.wb = xlwt.Workbook()
            self.ws = self.wb.add_sheet('Results')
            if int(EntryScreen.my_reverse) == 1:
                self.ws.write(0, 0, "Reversed: NO")
            elif int(EntryScreen.my_reverse) == 2:
                self.ws.write(0, 0, "Reversed: YES ")

            self.ws.write(0, 1, "Total Time of Trial")
            self.ws.write(0, 2, "FR schedule")
            self.ws.write(0, 3, "Candy Time")
            self.ws.write(0, 4, "Delay")
            self.ws.write(0, 5, "{} responses".format(self.object1_file))
            self.ws.write(0, 6, "{} responses".format(self.object2_file))


        #Iterates for each trial
        i = self.TrialNumber
        self.ws.write(i, 0, "Trial({})".format(self.TrialNumber))
        self.ws.write(i, 1, float(EntryScreen.my_choice_time) + float(EntryScreen.my_candy_time) + float(App.temp))
        self.ws.write(i, 2, float(App.temp)) #FR SCHEDULE
        self.ws.write(i, 3, float(EntryScreen.my_choice_time))
        self.ws.write(i, 4, float(EntryScreen.my_candy_time))
        self.ws.write(i, 5, self.object1_count)
        self.ws.write(i, 6, self.object2_count)


    def xlx_save(self):
        your_dir = tk.filedialog.askdirectory(title= "Where would you like to save this?")
        self.wb.save(str(your_dir) + "/my_titrate_results.xls")


if __name__ == "__main__":
    root = tk.Tk()
    entryscreen = EntryScreen(root)
    root.mainloop()

    root = tk.Tk()
    app = App(root)
    root.mainloop()
    app.xlx_save()
