#!/usr/bin/env python3

import time
import tkinter as tk
import random
import xlwt
from tkinter.filedialog import askdirectory



class EntryScreen(object):
    print("Entry Screen Initiating..")

    my_char = str()
    total_time_for_each_trial = int()
    my_reverse = int()
    the_start_num = int()
    the_end_num = int()
    the_steps_num = int()

    def __init__(self, master):

        master.title("Gideon's Behavioral Experiment")
        master.geometry("900x500+200+100")
        self.master = master

        self.frame1 = tk.Frame(master)
        self.frame1.pack(fill="both", expand=True)


        self.symbol_label = tk.Label(self.frame1, text="My Symbol")
        self.total_time_for_each_trial_label = tk.Label(self.frame1, text="Total Time for Trial: ")
        self.Reverse_the_Trial = tk.Label(self.frame1, text="Reverse the Trial? 1 for No, 2 for Yes")
        #schedule_range = tk.Label(self.frame1, text="Schedule Range. 'Starting,Ending,Steps'")
        self.start_label = tk.Label(self.frame1, text="Start number.")
        self.end_label = tk.Label(self.frame1, text="End number(non-inclusive) ")
        self.steps_label = tk.Label(self.frame1, text="Steps")

        self.symbol_label_Entry = tk.Entry(self.frame1)
        self.total_time_Entry = tk.Entry(self.frame1)
        self.Reverse_the_Trial_Entry = tk.Entry(self.frame1)
        self.start_num = tk.Entry(self.frame1)
        self.end_num = tk.Entry(self.frame1)
        self.steps_num = tk.Entry(self.frame1)

        self.packall()
        save_me = tk.Button(self.frame1, text="Ready", command=self.entry_get)
        save_me.pack(side="bottom")
        print("Entry Screen Completed, Ready to run.")


    def packall(self):
        self.symbol_label.pack()
        self.symbol_label_Entry.pack()
        self.total_time_for_each_trial_label.pack()
        self.total_time_Entry.pack()
        self.Reverse_the_Trial.pack()
        self.Reverse_the_Trial_Entry.pack()
        self.start_label.pack()
        self.start_num.pack()
        self.end_label.pack()
        self.end_num.pack()
        self.steps_label.pack()
        self.steps_num.pack()

    def entry_get(self):
        EntryScreen.my_char = self.symbol_label_Entry.get()
        EntryScreen.total_time_for_each_trial = self.total_time_Entry.get()
        EntryScreen.my_reverse = self.Reverse_the_Trial_Entry.get()
        #my_schedule_range = schedule_range_Entry.get()
        EntryScreen.the_start_num = int(self.start_num.get())
        EntryScreen.the_end_num = int(self.end_num.get())
        EntryScreen.the_steps_num = int(self.steps_num.get())

        print("My char: {}".format(self.my_char))
        print("My total time for each trial: {}".format(self.total_time_for_each_trial))
        print("My reverse number: {}".format(self.my_reverse))
        print("My start num: {}".format(self.the_start_num))
        print("My end num: {}".format(self.the_end_num))
        print("My steps num: {}".format(self.the_steps_num))

        self.master.destroy()




class App(EntryScreen):

    print("App Initiating..")
    def __init__(self, master):

        #Master Config
        master.title("Gideon's Behavioral Experiment")
        master.bind('<Left>', self.object_01)
        master.bind('<Right>', self.object_02)
        self.master = master

        #Variables
        self.start = EntryScreen.the_start_num
        self.end = EntryScreen.the_end_num
        self.steps = EntryScreen.the_steps_num
        App.randomnumber(self)
        self.char = EntryScreen.my_char
        self.my_string1 = self.char * self.count
        self.symbol = tk.StringVar()
        self.symbol.set(self.my_string1)
        self.my_string2 = self.char * 1
        self.one_symbol = tk.StringVar()
        self.one_symbol.set(self.my_string2)
        self.total_time_for_each_trial = EntryScreen.total_time_for_each_trial
        self.switch = 1
        self.TrialNumber = 1


        #counters
        self.seconds_elapsed = 0
        self.last_item_pressed = 0
        self.object1_count = 0
        self.object2_count = 0

        #Frames
        self.frame1 = tk.Frame(master)
        self.frame1.pack(side="left", fill="both", expand=True)
        self.frame2 = tk.Frame(master)
        self.frame2.pack(side="right", fill="both", expand=True)

        #CHANGE FILE NAMES HERE___
        if int(EntryScreen.my_reverse) == 1:
            self.object1_file = "ipad_Gideon.gif"
            self.object2_file = "book_Gideon.gif"
        elif int(EntryScreen.my_reverse) == 2:
            self.object1_file = "book_Gideon.gif"
            self.object2_file = "ipad_Gideon.gif"
        else:
            print("ERROR: Something went wrong with picture assignment")
        #__________________________

        self.ipad_photo = tk.PhotoImage(file=self.object1_file)
        self.book_photo = tk.PhotoImage(file=self.object2_file)

        #Photo packing
        self.photo1 = tk.Label(self.frame1, image=self.ipad_photo)
        self.photo1.pack(side="top")
        self.photo2 = tk.Label(self.frame2, image=self.book_photo)
        self.photo2.pack(side="top")

        #symbols
        self.symbol1 = tk.Label(self.frame1, textvariable=self.symbol, font=("Helvetica", 45))
        self.symbol1.pack(side="bottom")
        self.symbol2 = tk.Label(self.frame2, textvariable=self.one_symbol, font=("Helvetica", 45))
        self.symbol2.pack(side="bottom")


        print("App Completed, Ready to run.")
        self.my_TrialNum()
        self.my_start_info()

    def randomnumber(self): #Sets count = to random number in range
        self.results = random.randrange(self.start,self.end,self.steps)
        self.count = self.results
        #print("Random Number of symbol for next trial: {}".format(self.count))



    def my_buffer(self): #Stops multiple key presses
        #self.master.unbind('<Left>')
        #self.master.unbind('<Right>')
        self.my_unbind()
        self.master.update()
        time.sleep(1)
        self.master.update()


    def blackout(self):

        self.my_unbind()
        self.photo1.pack_forget()
        self.photo2.pack_forget()
        self.symbol1.pack_forget()
        self.symbol2.pack_forget()
        self.master.update()
        print("Blackout Initiating..")
        self.blackout_period = int(self.total_time_for_each_trial) - self.seconds_elapsed

        while self.blackout_period > 0:
            print ("My blackout for {} is ending in {}".format(self.last_item_pressed, self.blackout_period))
            time.sleep(1)
            self.blackout_period -= 1


        self.seconds_elapsed = 0
        self.my_unbind()
        self.master.update()


        print("Blackout Completed..")
        #time.sleep(self.blackout_period) #Put timing here


    def change_sides(self): #LEFT/RIGHT arrows stick to respective sides
        self.switch = random.randrange(1,3)
        #print("my switch: " + str(switch))
        if self.switch == 1: #Reverts back to ipad = leftside/ ipad = <Left> key bind

            self.photo1 = tk.Label(self.frame1, image=self.ipad_photo)
            self.photo1.pack(side="top")
            self.photo2 = tk.Label(self.frame2, image=self.book_photo)
            self.photo2.pack(side="top")

            self.symbol1 = tk.Label(self.frame1, textvariable=self.symbol, font=("Helvetica", 45))
            self.symbol1.pack(side="bottom")
            self.symbol2 = tk.Label(self.frame2, textvariable=self.one_symbol, font=("Helvetica", 45))
            self.symbol2.pack(side="bottom")

            my_string = self.char * self.results
            self.symbol.set(my_string)
            my_string2 = self.char * 1
            self.one_symbol.set(my_string2)

            #self.my_binds()
        elif self.switch == 2:  #Ipad = rightside frame / ipad = <Right> key bind


            self.photo1 = tk.Label(self.frame2, image=self.ipad_photo)
            self.photo1.pack(side="top")
            self.photo2 = tk.Label(self.frame1, image=self.book_photo)
            self.photo2.pack(side="top")

            self.symbol1 = tk.Label(self.frame2, textvariable=self.symbol, font=("Helvetica", 45))
            self.symbol1.pack(side="bottom")
            self.symbol2 = tk.Label(self.frame1, textvariable=self.one_symbol, font=("Helvetica", 45))
            self.symbol2.pack(side="bottom")

            my_string = self.char * self.results
            self.symbol.set(my_string)
            my_string2 = self.char * 1
            self.one_symbol.set(my_string2)

            #self.my_binds()

        else:
            print("\nERROR: Change sides went wrong\n")




    def normalize(self):
        #End Actions
        self.randomnumber() #set count = random number
        self.blackout() #turn screen white, uses change side to re-pack
        self.change_sides() #choose random side to pack, re-bind buttons
        self.my_end_info()
        self.xlx_results()

        #Start Actions
        self.TrialNumber += 1
        self.my_TrialNum()
        self.my_start_info()
        self.object1_count = 0
        self.object2_count = 0
        self.my_binds()





    #Object characteristics
    def object_01(self,event):
        self.my_buffer()
        self.count -= 1
        self.seconds_elapsed += 1
        self.object1_count += 1
        print("My object1 count: {}".format(self.object1_count))

        self.my_string = self.char * self.count
        self.symbol.set(self.my_string)
        self.master.update()

        self.last_item_pressed = self.object1_file
        print("My {} was pressed".format(self.object1_file))

        self.my_binds()
        if self.count <= 0:
            self.my_unbind()
            self.normalize()


    def object_02(self, event):
        self.my_buffer()
        self.count = 0
        self.seconds_elapsed += 1
        self.object2_count += 1

        self.my_string = self.char * self.count
        self.one_symbol.set(self.my_string2)

        self.last_item_pressed = self.object2_file
        print("My {} was pressed".format(self.object2_file))

        if self.count <= 0:
            self.normalize()


    def my_binds(self):
        print("BINDED STATE")
        if self.switch == 1:
            #print("Object1 is left")
            self.master.bind('<Left>', self.object_01)
            self.master.bind('<Right>', self.object_02)

        elif self.switch == 2:
            #print("Object1 is right")
            self.master.bind('<Right>', self.object_01)
            self.master.bind('<Left>', self.object_02)

        else:
            print("ERROR: My_binds went wrong")

    def my_unbind(self):
        print("UNBINDED STATE")
        self.master.unbind('<Left>')
        self.master.unbind('<Right>')
        self.master.update()

    def my_TrialNum(self):
        print("___Trial #{}___".format(self.TrialNumber))


    def my_start_info(self):

        #print("___Trial #{}___".format(self.TrialNumber))
        print("Total Time: {}".format(self.total_time_for_each_trial))
        print("FR schedule: {}".format(self.count))
        if int(self.my_reverse) == 1:
            print("Reversed: No ")
        elif int(self.my_reverse) == 2:
            print("Reversed: Yes")
        else:
            print("ERROR: my_start_info Method")
        #Trial per row

        #Metrics in columns going across

        #Exported to excel
        #IPAD Trials
        #total time = 60
        #Effort time = 10

        #Trial 1
        #REQUIRED
        #IPAD 15 Book 1

        #ATTTEMPTED
        #IPAD 6
        #BOOK 1

        #Object earned
        #BOOK
    def my_end_info(self):
        print("{} attempts: {}".format(self.object1_file,self.object1_count))
        print("{} attempts: {}".format(self.object2_file,self.object2_count))
        if self.object2_count > 0:
            print("Object Earned: {}".format(self.object2_file))
        else:
            print("Object Earned: {}".format(self.object1_file))


    #def write(self):
        #trial_number_data = []



    def xlx_results(self):
        if self.TrialNumber == 1:
            self.wb = xlwt.Workbook()
            self.ws = self.wb.add_sheet('Results')
            if int(self.my_reverse) == 1:
                self.ws.write(0, 0, "Reversed: NO")
            elif int(self.my_reverse) == 2:
                self.ws.write(0, 0, "Reversed: YES ")
            self.ws.write(0, 1, "Total Time of Trial")
            self.ws.write(0, 2, "FR schedule")
            self.ws.write(0, 3, "{} responses".format(self.object1_file))
            self.ws.write(0, 4, "{} responses".format(self.object2_file))
            self.ws.write(0, 5, "Object Earned")


        #Iterates for each trial
        i = self.TrialNumber
        self.ws.write(i, 0, "Trial({}): {}".format(self.TrialNumber,self.object1_file))
        self.ws.write(i, 1, int(self.total_time_for_each_trial))
        self.ws.write(i, 2, self.count) #FR SCHEDULE
        self.ws.write(i, 3, self.object1_count)
        self.ws.write(i, 4, self.object2_count)

        if self.object2_count > 0:
            self.ws.write(i, 5, self.object2_file)
        else:
            self.ws.write(i, 5, self.object1_file)


    def xlx_save(self):
        your_dir = tk.filedialog.askdirectory(title= "Where would you like to save this?")
        self.wb.save(str(your_dir) + "/gideon_exp_results.xls")


if __name__ == "__main__":
    root = tk.Tk()
    entryscreen = EntryScreen(root)
    root.mainloop()

    root = tk.Tk()
    app = App(root)
    root.mainloop()
    app.xlx_save()
