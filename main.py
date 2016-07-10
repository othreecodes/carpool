__author__ = 'OTHREE'

from Tkinter import *
import ttk
import tkMessageBox as MSGBOX
import tkSimpleDialog as Input
import datetime
import os

import MySQLdb

import ttkcalender

os.environ['SDL_VIDEO_CENTRED'] = '1'
HOST = "localhost"
DATABASE_USERNAME = "root"
DATABASE = "carpool"

# main class vehicle which contains all code
class Vehicle:
    # constructor


    def __init__(self, parent):
        # initialising the Parent window
        self.parent = parent
        self.parent.title("Vehicle App")
        style = ttk.Style()
        style.theme_use('clam')


def main():
    driverid = "";
    vid = ""

    def setdid(var):
        driverid = var

    def getdid(self):
        return driverid

    drid = ""
    open = False
    root = Tk()
    root.geometry("350x250+500+300")
    frame = LabelFrame(root, relief=RAISED, borderwidth=1, text="LOG IN TO CAR POOL", padx=20, pady=30)

    label_Lname = Label(frame, text="Username")
    label_Lpass = Label(frame, text="Password")
    entry_1 = Entry(frame)
    entry_2 = Entry(frame, show="*")
    label_Lname.grid(column=0, row=5, sticky=W, rowspan=6)
    label_Lpass.grid(column=0, row=11, sticky=W, pady=5)

    entry_1.grid(row=5, rowspan=6, column=1)
    entry_2.grid(row=11, column=1, pady=5)


    # signing up
    def signup():
        valcom = 'Male'
        rot = Tk()
        rot.geometry("400x400+300+200")
        frae = LabelFrame(rot, width=400, height=400, text="USER REGISTRATION PAGE", relief=RAISED, padx=20, pady=30)
        frae.grid(row=0, column=0, sticky='news')
        label_Sname = Label(frae, text="Names")
        label_Saddress = Label(frae, text="Address")
        label_Semail = Label(frae, text="Email")
        label_Smobile = Label(frae, text="Mobile No")
        label_Sender = Label(frae, text="Gender")
        label_Susertype = Label(frae, text="User Type")

        label_Susername = Label(frae, text="Username")
        label_Spassword = Label(frae, text="Password")
        label_Sconfpassword = Label(frae, text="Confirm Password")

        entry_names = Entry(frae, width=30)
        entry_address = Entry(frae, width=30)
        entry_email = Entry(frae, width=30)
        entry_mobile = Entry(frae, width=30)
        entry_username = Entry(frae, width=30)
        entry_password = Entry(frae, width=30, show="*")
        entry_compass = Entry(frae, width=30, show="*")
        cm_gender = ttk.Combobox(frae, width=27, textvariable=valcom)
        cm_gender['values'] = ('Male', 'Female')
        cm_gender.current(0)
        cm_gender.grid(row=5, column=1)

        cm_usertype = ttk.Combobox(frae, width=27)
        cm_usertype['values'] = ('Passenger', 'Driver')
        cm_usertype.current(0)
        cm_usertype.grid(row=6, column=1)

        label_Sname.grid(column=0, row=1, sticky=W, pady=5)
        label_Saddress.grid(column=0, row=2, sticky=W, pady=5)
        label_Semail.grid(column=0, row=3, sticky=W, pady=5)
        label_Smobile.grid(column=0, row=4, sticky=W, pady=5)
        label_Sender.grid(column=0, row=5, stick=W, pady=5)
        label_Susertype.grid(column=0, row=6, stick=W, pady=5)

        label_Susername.grid(column=0, row=7, sticky=W, pady=5)
        label_Spassword.grid(column=0, row=8, stick=W, pady=5)
        label_Sconfpassword.grid(column=0, row=9, stick=W, pady=5)

        entry_names.grid(row=1, column=1, pady=5)
        entry_address.grid(row=2, column=1, pady=5)
        entry_email.grid(row=3, column=1, pady=5)
        entry_mobile.grid(row=4, column=1, pady=5)

        entry_username.grid(row=7, column=1, pady=5)
        entry_password.grid(row=8, column=1, pady=5)
        entry_compass.grid(row=9, column=1, pady=5)

        errorLabel = Label(frae, text="complete the form ", fg="red")
        errorLabel.grid(row=10, columnspan=3)

        def submit():
            date = datetime.datetime.today().isoformat(' ')

            sql = sql = "INSERT INTO users (names, \
            address, email, mobile, gender,user_type,username,password,reg_date) \
            VALUES ('%s', '%s', '%s', '%s', '%s','%s','%s','%s','%s' )" % \
                        (entry_names.get(), entry_address.get(), entry_mobile.get(), entry_email.get(), cm_gender.get(),
                         cm_usertype.get(),
                         entry_username.get(), entry_password.get(), str(date[0:19]))

            succesful = True
            try:
                db = MySQLdb.connect(HOST, DATABASE_USERNAME, "", DATABASE)
                cursor = db.cursor()

                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
                succesful = False
            finally:
                db.close()

            if (succesful == True):
                if (cm_usertype.get() == 'Driver'):
                    window = Tk()
                    window.geometry("450x310+300+200")
                    win = LabelFrame(window, text="Driver Licence Registration")
                    label_name = Label(win, text="Licence Number")
                    label_issuance = Label(win, text="Date of First Issuance")
                    label_name.grid(row=0, column=0)
                    label_issuance.grid(row=1, column=0)

                    entry_name = Entry(win)
                    entry_issuance = ttkcalender.Calendar(win)

                    entry_name.grid(row=0, column=1)
                    entry_issuance.grid(row=1, column=1)

                    def doLicence():
                        date = entry_issuance.selection
                        date = date.date()
                        try:
                            sql="INSERT INTO licence (driver_id, licence_no, iss_date) VALUES ('%s', '%s', '%s')" %(entry_username.get(),entry_name.get(),date)
                            print sql
                            db = MySQLdb.connect(HOST, DATABASE_USERNAME, "", DATABASE)
                            cursor = db.cursor()

                            cursor.execute(sql)
                            db.commit()
                        except:
                            db.rollback()
                            print "jlkjj"
                            succesful = False
                        finally:
                            db.close()
                            MSGBOX.showinfo(title="SUCCESS", message="ACCOUNT FOR " + entry_names.get() + " Successfully created")
                            rot.destroy()
                        window.destroy();


                        pass

                    send = Button(win, text="Submit", command=doLicence)

                    send.grid(row=2, columnspan=2)

                    win.pack()
                    window.mainloop()
                else:
                    MSGBOX.showinfo(title="SUCCESS", message="ACCOUNT FOR " + entry_names.get() + " Successfully created")
                    rot.destroy()
            else:
                MSGBOX.showerror(title="ERROR", message="ACCOUNT NOT CREATED\n Check database connection and try again")

                # print(entry_names.get())
                # print(entry_address.get())
                # print(entry_email.get())
                # print(entry_mobile.get())
                # print(cm_gender.get())
                # print(entry_username.get())
                # print(entry_password.get())
                # print(entry_compass.get())

        but = ttk.Button(frae, text="SUBMIT", command=submit)
        but.grid(row=10, column=0)
        rot.focus_force()

        frae.pack(fill="both", expand="yes")
        app = Vehicle(rot)
        rot.mainloop()

    check = Button(frame, text="SIGN UP", pady=0, relief=RAISED, command=signup)

    check.grid(column=0, row=17, columnspan=1)

    # login Action
    def login():
        name = ""
        sql = "SELECT * FROM users \
        WHERE username = '%s'" % (entry_1.get()) + " AND password = '%s'" % (entry_2.get())
        db = MySQLdb.connect(HOST, DATABASE_USERNAME, "", DATABASE)
        cursor = db.cursor()
        cursor.execute(sql)
        isUser = False
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                real_name = row[1]
                name = row[7]
                password = row[8]
                usertype = row[6]

                isUser = True
        except:
            print("Error: unable to fecth data")

        def doDriverPage():
            root.destroy()
            rootd = Tk()
            rootd.geometry("700x400+300+200")
            frambox = LabelFrame(rootd, width=700, height="600", text="User Profile for " + real_name, relief=RAISED,
                                 padx=20, pady=30)
            # name
            profile_name = Label(frambox, text="NAME:")
            profile_name.grid(row=0, column=0, sticky=W, pady=5)
            profile_name_0 = Label(frambox, text=row[1])
            profile_name_0.grid(row=0, column=1, pady=5)
            # address
            profile_address = Label(frambox, text="ADDRESS:")
            profile_address.grid(row=1, column=0, sticky=W, pady=5)
            profile_address_0 = Label(frambox, text=row[2])
            profile_address_0.grid(row=1, column=1, pady=5)
            # email
            profile_email = Label(frambox, text="EMAIL:")
            profile_email.grid(row=2, column=0, sticky=W, pady=5)
            profile_email_0 = Label(frambox, text=row[3])
            profile_email_0.grid(row=2, column=1, pady=5)
            # mobile
            profile_mobile = Label(frambox, text="MOBILE:")
            profile_mobile.grid(row=3, column=0, sticky=W, pady=5)
            profile_mobile_0 = Label(frambox, text=row[4])
            profile_mobile_0.grid(row=3, column=1, pady=5)
            # gender
            profile_gender = Label(frambox, text="GENDER:")
            profile_gender.grid(row=4, column=0, sticky=W, pady=5)
            profile_gender_0 = Label(frambox, text=row[5])
            profile_gender_0.grid(row=4, column=1, pady=5)
            # usertype
            profile_type = Label(frambox, text="PROFILE TYPE:")
            profile_type.grid(row=5, column=0, sticky=W, pady=5)
            profile_type_0 = Label(frambox, text=row[6])
            profile_type_0.grid(row=5, column=1, pady=5)
            # username
            profile_username = Label(frambox, text="USERNAME:")
            profile_username.grid(row=6, column=0, sticky=W, pady=5)
            profile_username_0 = Label(frambox, text=row[7])
            profile_username_0.grid(row=6, column=1, pady=5)

            profile_date = Label(frambox, text="DATE REGISTERED:")
            profile_date.grid(row=6, column=0, sticky=W, pady=5)
            profile_date_0 = Label(frambox, text=row[9])
            profile_date_0.grid(row=6, column=1, pady=5)
            framboxbtm = Frame(rootd, relief=GROOVE)

            def registerVehicle():

                regwindow = Tk()
                regwindow.geometry("400x400+300+200")
                frambox = LabelFrame(regwindow, width=400, height="600", text="Register Vehicle ", relief=RAISED,
                                     padx=20, pady=30)

                label_vehicle_make = Label(frambox, text="VEHICLE MAKE")
                entry_vehicle_make = Entry(frambox, width=34)
                label_year_of_purchase = Label(frambox, text="YEAR OF PURCHASE")
                choices1 = []
                for i in range(1799, 2017, 1):
                    choices1.append(i)
                entry_year_of_purchase = ttk.Combobox(frambox, width=30)
                entry_year_of_purchase['values'] = choices1
                label_vehicle_model = Label(frambox, text="VEHICLE MODEL")
                entry_vehicle_model = Entry(frambox, width=34)
                entry_year_of_purchase.current(1)

                label_no_of_seats = Label(frambox, text="NO OF SEATS")
                choices2 = []
                for i in range(2, 51, 1):
                    choices2.append(i)
                entry_no_of_seats = ttk.Combobox(frambox, width=30)
                entry_no_of_seats['values'] = choices2
                entry_no_of_seats.current(3)

                label_vehicle_type = Label(frambox, text="VEHICLE TYPE")
                choices3 = ['Private', 'Hired']
                entry_vehicle_type = ttk.Combobox(frambox, width=30)
                entry_vehicle_type['values'] = choices3
                entry_vehicle_type.current(0)

                label_vehicle_cat = Label(frambox, text="VEHICLE CATEGORY")
                choices4 = ['Car', 'Bus', 'Coaster', 'Truck']
                entry_vehicle_cat = ttk.Combobox(frambox, width=30)
                entry_vehicle_cat['values'] = choices4
                entry_vehicle_cat.current(0)

                label_vehicle_make.grid(row=0, column=0, sticky=W, pady=5)
                entry_vehicle_make.grid(row=0, column=1, pady=5)

                label_year_of_purchase.grid(row=1, column=0, sticky=W, pady=5)
                entry_year_of_purchase.grid(row=1, column=1, pady=5)

                label_vehicle_model.grid(row=2, column=0, sticky=W, pady=5)
                entry_vehicle_model.grid(row=2, column=1, pady=5)

                label_no_of_seats.grid(row=3, column=0, sticky=W, pady=5)
                entry_no_of_seats.grid(row=3, column=1, pady=5)

                label_vehicle_type.grid(row=4, column=0, sticky=W, pady=5)
                entry_vehicle_type.grid(row=4, column=1, pady=5)

                label_vehicle_cat.grid(row=5, column=0, sticky=W, pady=5)
                entry_vehicle_cat.grid(row=5, column=1, pady=5)

                def regvec():
                    if (entry_vehicle_type.get() == 'Hired'):
                        window = Tk()
                        window.geometry("250x610+300+200")
                        win = LabelFrame(window, text="Agency details")
                        label_name = Label(win, text="Agency Name")
                        label_address = Label(win, text="Agency Address")
                        label_name.grid(row=0, column=0)
                        label_address.grid(row=1, column=0)

                        entry_name = Entry(win)
                        entry_address = Entry(win)
                        entry_name.grid(row=0, column=1)
                        entry_address.grid(row=1, column=1)

                        def agencyreg():
                            sql2 = "insert into agency_details (name, address, user_id) values ('%s', '%s','%s')" % \
                                   (entry_name.get(), entry_address.get(), name)
                            db = MySQLdb.connect(HOST, DATABASE_USERNAME, "", DATABASE)

                            cursor = db.cursor()
                            cursor.execute(sql2)
                            db.commit()
                            window.destroy()

                            sql = "INSERT INTO vehicle (make, \
                            year, model, seats, type ,category,user_id) \
                            VALUES ('%s', '%s', '%s', '%s', '%s','%s','%s')" % \
                                  (entry_vehicle_make.get(), entry_year_of_purchase.get(), entry_vehicle_model.get(),
                                   entry_no_of_seats.get(), entry_vehicle_type.get(), entry_vehicle_cat.get(), name)
                            succesfull = True
                            try:
                                db = MySQLdb.connect(HOST, DATABASE_USERNAME, "", DATABASE)
                                cursor = db.cursor()
                                cursor.execute(sql)
                                db.commit()
                            except:
                                db.rollback()
                                succesfull = False
                            finally:
                                db.close()

                            if succesfull == True:
                                MSGBOX.showinfo("SUCCESS", "VEHICLE ADDED")
                                regwindow.destroy()
                            else:
                                MSGBOX.showerror("ERROR", "COULD NOT ADD VEHICLE\nPLEASE TRY AGAIN")

                        send = Button(win, text="Submit", command=agencyreg)

                        send.grid(row=2, columnspan=2)

                        win.pack()
                        window.mainloop()

                    sql = "INSERT INTO vehicle (make, \
                        year, model, seats, type ,category,user_id) \
                        VALUES ('%s', '%s', '%s', '%s', '%s','%s','%s')" % \
                          (entry_vehicle_make.get(), entry_year_of_purchase.get(), entry_vehicle_model.get(),
                           entry_no_of_seats.get(), entry_vehicle_type.get(), entry_vehicle_cat.get(), name)
                    succesfull = True
                    try:
                        db = MySQLdb.connect(HOST, DATABASE_USERNAME, "", DATABASE)
                        cursor = db.cursor()
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                        succesfull = False
                    finally:
                        db.close()

                    if succesfull == True:
                        MSGBOX.showinfo("SUCCESS", "VEHICLE ADDED")
                        regwindow.destroy()
                    else:
                        MSGBOX.showerror("ERROR", "COULD NOT ADD VEHICLE\nPLEASE TRY AGAIN")

                submit = Button(frambox, text="SUBMIT", bg="#2a2a2a", fg="#ffffff", command=regvec)
                submit.grid(row=6, columnspan=2, pady=5)

                frambox.pack(fill="both")
                app = Vehicle(regwindow)
                regwindow.mainloop()

            def viewVehicles():
                view_window = Tk()
                view_window.geometry("450x610+300+50")
                frame_box = LabelFrame(view_window, width=400, height="150", text="Vehicles for " + real_name,
                                       relief=RAISED, padx=20, pady=10)

                sql = "SELECT * FROM vehicle \
                WHERE user_id = '%s'" % (name)
                db = MySQLdb.connect(HOST, DATABASE_USERNAME, "", DATABASE)
                cursor = db.cursor()
                cursor.execute(sql)
                hasCar = False
                allcar = [];
                veh_cars = []
                try:
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    for row in results:
                        i = 0
                        car = []
                        car.append(row[2])
                        car.append(row[1])
                        car.append(row[3])
                        car.append(row[4])
                        car.append(row[5])
                        car.append(row[6])
                        car.append(int(row[0]))
                        veh_cars.append(i)
                        allcar.append(car)
                        i += 1
                        hasCar = True
                except:
                    print "Error: unable to fecth data"
                finally:
                    print allcar

                j = 0
                rowcount = 0
                colcount = 0
                title = Label(frame_box, text="|S/N|  |MAKE|   |YEAR OF PURCHASE|  |MODEL| |NO OF PASSENGERS| |VEHICLE TYPE|    |VEHICLE CAT|",anchor=E)
                title.pack(side=TOP)
                lba = Listbox(frame_box)
                lba.pack(fill=X,side=BOTTOM)
                lba.delete(first=0, last=lba.size())
                dictcar ={}
                for cars in allcar:
                    var=str(j + 1) + ". |" + cars[0] + "|      |" + cars[1] + "|       |" + cars[2] + "|       |" + cars[
                                            3] + "|        |" + cars[4] + "|             |" + cars[5]+"|"
                    lba.insert(0,var)
                    dictcar[var] = cars[6]

                    rowcount += 1
                    j += 1

                frame_box.pack(fill="both")
                bottom_frame = LabelFrame(view_window, width=450, height="410", text="Vehicle Sharing", relief=RAISED,
                                          padx=20)

                label_sharing_cost = Label(bottom_frame, text="Sharing cost(per km)")
                label_starting_point = Label(bottom_frame, text="Sharing point")
                label_destination = Label(bottom_frame, text="Destination")
                label_start = Label(bottom_frame, text="Start time (24hr)")
                label_estimated = Label(bottom_frame, text="Estimated Arrival Time (24hr)")
                label_passengers = Label(bottom_frame, text="No of Allowed Passengers")
                label_date = Label(bottom_frame, text="Trip Date")
                label_gender = Label(bottom_frame, text="Gender Preference")

                entry_sharing_cost = Entry(bottom_frame, width=30)
                entry_starting_point = Entry(bottom_frame, width=30)
                entry_destination = Entry(bottom_frame, width=30)
                entry_start = Entry(bottom_frame, width=30)
                entry_estimated = Entry(bottom_frame, width=30)

                choices2 = []
                for i in range(2, 51, 1):
                    choices2.append(i)
                entry_passengers = ttk.Combobox(bottom_frame, width=27)
                entry_passengers['values'] = choices2

                entry_date = ttkcalender.Calendar(bottom_frame)
                entry_date.pack()

                entry_gender = ttk.Combobox(bottom_frame, width=27)
                entry_gender['values'] = ('Male', 'Female', 'Both')
                entry_gender.current(0)

                label_sharing_cost.grid(row=0, column=0, pady=5, sticky=W)
                entry_sharing_cost.grid(row=0, column=1, pady=5)
                label_starting_point.grid(row=1, column=0, pady=5, sticky=W)
                entry_starting_point.grid(row=1, column=1, pady=5)
                label_destination.grid(row=2, column=0, pady=5, sticky=W)
                entry_destination.grid(row=2, column=1, pady=5)
                label_start.grid(row=3, column=0, pady=5, sticky=W)
                entry_start.grid(row=3, column=1, pady=5)
                label_estimated.grid(row=4, column=0, pady=5, sticky=W)
                entry_estimated.grid(row=4, column=1, pady=5)
                label_passengers.grid(row=5, column=0, pady=5, sticky=W)
                entry_passengers.grid(row=5, column=1, pady=5)
                label_date.grid(row=6, column=0, pady=5, sticky=W)
                entry_date.grid(row=6, column=1, pady=5)
                label_gender.grid(row=7, column=0, pady=5, sticky=W)
                entry_gender.grid(row=7, column=1, pady=5)

                def shareVehicles():
                    car_id = dictcar.get(lba.selection_get())
                    print car_id
                    if(str(car_id).upper()=="None".upper()):
                        MSGBOX.showerror("ERROR", "Please Select a Car to Share")
                        pass

                    else:
                        date = entry_date.selection
                        date = date.date()
                        sql = sql = "INSERT INTO vehicle_sharing (cost, \
                            start_point, dest_point, start_time, arrival_time ,no_pass ,date, gender, user_id,vid) \
                            VALUES ('%s', '%s', '%s', '%s', '%s','%s','%s','%s','%s','%s')" % \
                                    (entry_sharing_cost.get(), entry_starting_point.get(), entry_destination.get(),
                                     entry_start.get(),
                                     entry_estimated.get(), str(entry_passengers.get()), date, entry_gender.get(), name,car_id)
                        succesfull = True
                        try:
                            db = MySQLdb.connect(HOST, DATABASE_USERNAME, "", DATABASE)
                            cursor = db.cursor()
                            cursor.execute(sql)
                            db.commit()
                        except:
                            db.rollback()
                            succesfull = False
                        finally:
                            db.close()

                        if succesfull == True:
                            MSGBOX.showinfo("SUCCESS", "SHARED VEHICLE ADDED")

                            view_window.destroy()
                        else:
                            MSGBOX.showerror("ERROR", "COULD NOT ADD VEHICLE\nPLEASE TRY AGAIN")

                    pass

                button_share = Button(bottom_frame, text="Share Vehicle", pady=0, font=2, relief=GROOVE,
                                      command=shareVehicles)
                button_share.grid(row=8, columnspan=2, pady=5)

                bottom_frame.pack(side=BOTTOM, fill='both')
                app = Vehicle(view_window)
                view_window.mainloop()

            def viewShared():
                toal = ""
                view_window = Tk()
                view_window.geometry("650x610+300+50")
                frame_box = LabelFrame(view_window, width=600, height="400", text="Shared Vehicles for " + real_name,
                                       relief=RAISED, padx=20, pady=0)

                sql = "SELECT * FROM vehicle_sharing \
                WHERE user_id = '%s'" % (name)
                print name
                db = MySQLdb.connect(HOST, DATABASE_USERNAME, "", DATABASE)
                cursor = db.cursor()
                cursor.execute(sql)
                hasCar = False
                allcar = [];
                veh_cars = []
                try:
                    print "jj"
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    for row in results:
                        i = 0
                        car = []
                        car.append(row[2])
                        car.append("cost: " + row[1])
                        car.append(row[3])
                        car.append(row[4])
                        car.append(row[5])
                        car.append(row[6])
                        veh_cars.append(i)
                        allcar.append(car)
                        i += 1
                        hasCar = True
                except:
                    print "Error: unable to fecth data"
                finally:
                    db.close()

                j = 0
                rowcount = 0
                colcount = 0
                for cars in allcar:
                    veh_cars[j] = Label(frame_box,
                                        text=str(j + 1) + ". " + cars[0] + " " + cars[1] + " " + cars[2] + " " + cars[
                                            3] + " " + cars[4] + " " + cars[5])
                    veh_cars[j].grid(row=rowcount, column=colcount, pady=8, sticky=W, columnspan=5)
                    rowcount += 1
                    j += 1

                frame_box.pack(fill="both")
                #
                # Frame for requested vehickes
                #
                bottom_view = LabelFrame(view_window, width=700, height="600", text="Requested Vehicles", relief=RAISED,
                                         padx=20, pady=5)
                lb = Listbox(bottom_view)

                side_frame = Frame(bottom_view, width=80, height=20)
                side_frame.pack(side=RIGHT)

                reqs = {}

                def listset():
                    sql = "SELECT * FROM request \
                    WHERE driver_id = '%s'" % (name) + "ORDER BY `request`.`bearable` ASC"
                    print name
                    db = MySQLdb.connect(HOST, DATABASE_USERNAME, "", DATABASE)
                    cursor = db.cursor()
                    lb.delete(first=0, last=lb.size())
                    i = 0
                    try:
                        cursor.execute(sql)
                        results = cursor.fetchall()
                        for row in results:
                            car = []
                            car.append(row[2])
                            car.append(row[1])
                            car.append(row[3])
                            car.append(row[4])
                            car.append(row[5])
                            car.append(row[6])
                            veh_cars.append(i)
                            allcar.append(car)
                            time = row[3]
                            var = "Request From " + row[4] + ", " + row[5] + ", on " + time[0:19] + " Destination: " + \
                                  row[
                                      2] + ", Pick up point: " + row[1] + "Bearable Cost: " + row[6] + " (" + row[
                                      7].upper() + ") "
                            reqs[var] = int(row[0])
                            lb.insert(i, var)
                            i += 1
                            hasCar = True
                            print row
                            print reqs

                    except:
                        pass
                    finally:
                        db.close()
                        lb.pack(fill=X)

                listset()
                bottom_view.pack(side=BOTTOM, fill=BOTH)

                def approve():
                    try:
                        print lb.selection_get()
                        print reqs[lb.selection_get()]

                        try:
                            db = MySQLdb.connect(HOST, DATABASE_USERNAME, "", DATABASE)
                            cursor = db.cursor()
                            sql = "update request set status = '%s' where id = '%i'" % (
                                'approved', int(reqs[lb.selection_get()]))
                            print sql
                            cursor.execute(sql)
                            db.commit()
                        except:
                            db.rollback()
                        finally:
                            db.close()
                            listset()

                    except:
                        MSGBOX.showerror("Error", "No Request Selected")

                    pass

                def deny():
                    try:
                        print lb.selection_get()
                        print reqs[lb.selection_get()]

                        try:
                            db = MySQLdb.connect(HOST, DATABASE_USERNAME, "", DATABASE)
                            cursor = db.cursor()
                            sql = "update request set status = '%s' where id = '%i'" % (
                                'denied', int(reqs[lb.selection_get()]))
                            print sql
                            cursor.execute(sql)
                            db.commit()
                            lb.update()
                        except:
                            db.rollback()
                        finally:
                            db.close()
                            listset()

                    except:
                        MSGBOX.showerror("Error", "No Request Selected")

                    pass

                def details():
                    try:
                        sql = "select user_id from request where id = '%i'" % (int(reqs[lb.selection_get()]))
                        dbo = MySQLdb.connect(HOST, DATABASE_USERNAME, "", DATABASE)
                        cursor = dbo.cursor()
                        cursor.execute(sql)
                        print sql
                        result = cursor.fetchone()
                        print result[0]
                    except:
                        print "not found"
                        MSGBOX.showerror("Error", "No Request Selected")
                    finally:
                        dbo.close()

                    try:
                        sql2 = "select * from users where username = '%s'" % (result)
                        dbo = MySQLdb.connect(HOST, DATABASE_USERNAME, "", DATABASE)
                        cursor = dbo.cursor()
                        cursor.execute(sql2)

                        result = cursor.fetchone()
                        MSGBOX.showinfo("User Details",
                                        "Name: " + result[1] + "\nEmail: " + result[4] + "\nPhone Number: " + result[
                                            3] + "\nSex: " + result[5])
                        print result
                    except:
                        print "error"

                    finally:
                        dbo.close()

                approve_button = Button(side_frame, text="Approve", pady=0, font=2, relief=GROOVE, command=approve)
                approve_button.pack(side=TOP)
                deny_button = Button(side_frame, text="Deny", pady=0, font=2, relief=GROOVE, command=deny)
                deny_button.pack(side=TOP)
                details_button = Button(side_frame, text="Details", pady=0, font=2, relief=GROOVE, command=details)
                details_button.pack(side=TOP)
                app = Vehicle(view_window)
                view_window.mainloop()
                pass

            def edit():
                valcom = 'Male'
                rot = Tk()
                rot.geometry("400x400+300+200")
                frae = LabelFrame(rot, width=400, height=400, text="EDIT PROFILE INFORMATION", relief=RAISED, padx=20,
                                  pady=30)
                frae.grid(row=0, column=0, sticky='news')
                label_Sname = Label(frae, text="Names")
                label_Saddress = Label(frae, text="Address")
                label_Semail = Label(frae, text="Email")
                label_Smobile = Label(frae, text="Mobile No")
                label_Sender = Label(frae, text="Gender")
                label_Susertype = Label(frae, text="User Type")

                label_Susername = Label(frae, text="Username")
                label_Spassword = Label(frae, text="Password")
                label_Sconfpassword = Label(frae, text="Confirm Password")

                entry_names = Entry(frae, width=30)
                entry_names.insert(1, profile_name_0['text'])
                print profile_name_0['text']
                entry_address = Entry(frae, width=30)
                entry_address.insert(1, profile_address_0['text'])
                entry_email = Entry(frae, width=30)
                entry_email.insert(1, profile_email_0['text'])
                entry_mobile = Entry(frae, width=30)
                entry_mobile.insert(1, profile_mobile_0['text'])
                entry_username = Entry(frae, width=30)
                entry_username.insert(0, profile_username_0['text'])
                entry_password = Entry(frae, width=30, show="*")
                entry_compass = Entry(frae, width=30, show="*")
                cm_gender = ttk.Combobox(frae, width=27, textvariable=valcom, state=DISABLED)
                cm_gender['values'] = (profile_gender_0['text'])

                cm_gender.current(0)
                cm_gender.grid(row=5, column=1)

                cm_usertype = ttk.Combobox(frae, width=27, state=DISABLED)
                cm_usertype['values'] = (profile_type_0['text'])
                cm_usertype.current(0)
                cm_usertype.grid(row=6, column=1)

                label_Sname.grid(column=0, row=1, sticky=W, pady=5)
                label_Saddress.grid(column=0, row=2, sticky=W, pady=5)
                label_Semail.grid(column=0, row=3, sticky=W, pady=5)
                label_Smobile.grid(column=0, row=4, sticky=W, pady=5)
                label_Sender.grid(column=0, row=5, stick=W, pady=5)
                label_Susertype.grid(column=0, row=6, stick=W, pady=5)

                label_Susername.grid(column=0, row=7, sticky=W, pady=5)
                label_Spassword.grid(column=0, row=8, stick=W, pady=5)
                label_Sconfpassword.grid(column=0, row=9, stick=W, pady=5)

                entry_names.grid(row=1, column=1, pady=5)
                entry_address.grid(row=2, column=1, pady=5)
                entry_email.grid(row=3, column=1, pady=5)
                entry_mobile.grid(row=4, column=1, pady=5)

                entry_username.grid(row=7, column=1, pady=5)
                entry_password.grid(row=8, column=1, pady=5)
                entry_compass.grid(row=9, column=1, pady=5)

                errorLabel = Label(frae, text="complete the form ", fg="red")
                errorLabel.grid(row=10, columnspan=3)

                def submit():
                    suc = True
                    sql = "update users set names = '%s', address = '%s', email = '%s', mobile = '%s', username = '%s', password = '%s' where id = '%i'" % (
                        entry_names.get(), entry_address.get(), entry_email.get(), entry_mobile.get(),
                        entry_username.get(),
                        entry_password.get(), int(row[0]))
                    print sql
                    try:
                        dbq = MySQLdb.connect(HOST, DATABASE_USERNAME, "", DATABASE)
                        cursor = dbq.cursor()
                        suc = True
                        cursor.execute(sql)
                        dbq.commit()
                    except:
                        suc = False
                        pass

                    if suc == True:
                        MSGBOX.showinfo("SUCESS!!", "DATA UPDATED SUCESSFULLY")
                    else:
                        MSGBOX.showerror("ERROR", "AN ERROR OCCURED")
                    pass

                but = ttk.Button(frae, text="SUBMIT", command=submit)
                but.grid(row=10, column=0)

                pass

            framboxbtm.pack(side=BOTTOM)
            btn1 = Button(framboxbtm, text="Edit Profile", pady=0, font=2, relief=GROOVE, command=edit)
            btn1.pack(side=LEFT)
            btn2 = Button(framboxbtm, text="Register Vehicle", pady=0, font=2, relief=GROOVE, command=registerVehicle)
            btn2.pack(side=LEFT)
            btn3 = Button(framboxbtm, text="View/Share Registered Vehicles", pady=0, font=2, relief=GROOVE,
                          command=viewVehicles)
            btn3.pack(side=LEFT)
            btn4 = Button(framboxbtm, text="View Your Shared Vehicle", pady=0, font=2, relief=GROOVE,
                          command=viewShared)
            btn4.pack(side=LEFT)

            def home():
                rootd.destroy();
                main()

            btn5 = Button(framboxbtm, text="Log out", pady=0, font=2, relief=GROOVE, command=home)
            btn5.pack(side=LEFT)

            frambox.pack(fill="both")
            appr = Vehicle(rootd)
            rootd.mainloop()

        def doPassenger():
            root.destroy()
            rootd = Tk()
            rootd.geometry("700x400+300+200")
            frambox = LabelFrame(rootd, width=700, height="600", text="User Profile for " + real_name, relief=RAISED,
                                 padx=20, pady=30)
            # name
            profile_name = Label(frambox, text="NAME:")
            profile_name.grid(row=0, column=0, sticky=W, pady=5)
            profile_name_0 = Label(frambox, text=row[1])
            profile_name_0.grid(row=0, column=1, pady=5)
            # address
            profile_address = Label(frambox, text="ADDRESS:")
            profile_address.grid(row=1, column=0, sticky=W, pady=5)
            profile_address_0 = Label(frambox, text=row[2])
            profile_address_0.grid(row=1, column=1, pady=5)
            # email
            profile_email = Label(frambox, text="EMAIL:")
            profile_email.grid(row=2, column=0, sticky=W, pady=5)
            profile_email_0 = Label(frambox, text=row[3])
            profile_email_0.grid(row=2, column=1, pady=5)
            # mobile
            profile_mobile = Label(frambox, text="MOBILE:")
            profile_mobile.grid(row=3, column=0, sticky=W, pady=5)
            profile_mobile_0 = Label(frambox, text=row[4])
            profile_mobile_0.grid(row=3, column=1, pady=5)
            # gender
            profile_gender = Label(frambox, text="GENDER:")
            profile_gender.grid(row=4, column=0, sticky=W, pady=5)
            profile_gender_0 = Label(frambox, text=row[5])
            profile_gender_0.grid(row=4, column=1, pady=5)
            # usertype
            profile_type = Label(frambox, text="PROFILE TYPE:")
            profile_type.grid(row=5, column=0, sticky=W, pady=5)
            profile_type_0 = Label(frambox, text=row[6])
            profile_type_0.grid(row=5, column=1, pady=5)
            # usertype
            profile_username = Label(frambox, text="USERNAME:")
            profile_username.grid(row=6, column=0, sticky=W, pady=5)
            profile_username_0 = Label(frambox, text=row[7])
            profile_username_0.grid(row=6, column=1, pady=5)

            profile_date = Label(frambox, text="DATE REGISTERED:")
            profile_date.grid(row=6, column=0, sticky=W, pady=5)
            profile_date_0 = Label(frambox, text=row[9])
            profile_date_0.grid(row=6, column=1, pady=5)

            framboxbtm = Frame(rootd, relief=GROOVE)

            def requestVehicle():

                sql = "SELECT * FROM vehicle_sharing ORDER BY `vehicle_sharing`.`date` DESC "

                db = MySQLdb.connect(HOST, DATABASE_USERNAME, "", DATABASE)
                cursor = db.cursor()
                cursor.execute(sql)
                hasCar = False
                allcar = [];
                veh_cars = []
                store = {}
                try:
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    for row_vs in results:
                        i = 0
                        car = []

                        # car.append(row[1] +" to "+row[2])
                        store[row_vs[2] + " to " + row_vs[3]] = int(row_vs[0])

                        allcar.append(row_vs[2] + " to " + row_vs[3])
                        i += 1
                        hasCar = True
                except:

                    print "Error: unable to fecth data"
                finally:
                    print allcar
                framboxx = Tk()
                framboxx.geometry("400x300+300+200")
                panel = LabelFrame(framboxx, width=400, height=300, text="Choose Destination")
                label_start = Label(panel, text="Destination")
                combo_start = ttk.Combobox(panel, width=50)
                combo_start.pack(fill=X)
                label_info = Label(panel, text="with selected...")
                # for var in allcar:
                #     for dist in allcar[0]:
                #         veh_cars.append(dist)
                combo_start['values'] = allcar

                def view():
                    print store[combo_start.get()]
                    sql = "SELECT * FROM vehicle_sharing WHERE id = '%i'" % (int(store[combo_start.get()]))

                    db = MySQLdb.connect(HOST, DATABASE_USERNAME, "", DATABASE)
                    cursor = db.cursor()
                    cursor.execute(sql)
                    hasCar = False
                    allcar = [];
                    veh_cars = []


                    try:
                        cursor.execute(sql)
                        results = cursor.fetchall()
                        for row_vees in results:


                            sql_veh = "select * from vehicle where id = '%s'"%row_vees[10]
                            print sql_veh
                            dbw = MySQLdb.connect(HOST, DATABASE_USERNAME, "", DATABASE)
                            cursorw = dbw.cursor()
                            cursorw.execute(sql_veh)
                            resultw = cursorw.fetchone()

                            sql_ve = "select * from licence where driver_id = '%s'"%row_vees[9]
                            print sql_ve
                            dbq = MySQLdb.connect(HOST, DATABASE_USERNAME, "", DATABASE)
                            cursorq = dbq.cursor()
                            cursorq.execute(sql_ve)
                            resultq = cursorq.fetchone()



                            MSGBOX.showinfo("Details For " + combo_start.get(),
                                            "Starting point :" + row_vees[2] + "\nDestination :" + row_vees[3] + "\n" \
                                                                                                                 "Start time: " +
                                            row_vees[4] + "\nEstimated Arrival Time :" + row_vees[
                                                5] + "\nNumber of Passengers :" + row_vees[6] + "" \
                                                                                                "\nDate :" + row_vees[
                                                7] + "\nGender Preference :" + row_vees[8] + "\nCost per Km :" +
                                            row_vees[1]+"\nVehilcle Type: "+resultw[6]+"\nDriving Since: "+resultq[3])

                    except:
                        print "Error: unable to fecth data"
                    finally:
                        print allcar

                def getv():
                    # to get driver id
                    print store[combo_start.get()]
                    sqli = "SELECT * FROM vehicle_sharing WHERE id = '%i'" % (int(store[combo_start.get()]))

                    db = MySQLdb.connect(HOST, DATABASE_USERNAME, "", DATABASE)
                    cursor = db.cursor()

                    hasCar = False
                    allcar = [];
                    veh_cars = []

                    try:
                        cursor.execute(sqli)
                        results = cursor.fetchall()
                        for r_vees in results:
                            driverid = r_vees[9]
                            vid = r_vees[10]
                            setdid(r_vees[9])

                            print " dsfsdfasdfadsfhkdsf", r_vees[9], " hgghhggh ", driverid

                    except:
                        print "Error: unable to fecth data"
                    finally:
                        print allcar

                    # driver id getEnd

                    pick = Input.askstring("Location", "Where would you liked to be picked?\n\n")
                    dest = Input.askstring("Destination", "Where would you liked to be dropped off?\n\n")
                    b_cost = Input.askstring("Bearable Cost", "How much are you willing to pay?\n\n")
                    date = datetime.datetime.now()
                    sql = "INSERT INTO request (pick, \
                        dest, reg_date, user_id,gender, bearable, status,driver_id,vehicle_id) \
                        VALUES ('%s', '%s', '%s','%s','%s','%s','%s','%s','%s')" % \
                          (pick, dest, date, profile_username_0['text'], profile_gender_0['text'], b_cost, "pending",
                           r_vees[9], r_vees[10])
                    print sql
                    succesfull = True
                    try:
                        db = MySQLdb.connect(HOST, DATABASE_USERNAME, "", DATABASE)
                        cursor = db.cursor()
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                        succesfull = False
                    finally:
                        db.close()

                    if succesfull == True:
                        MSGBOX.showinfo("SUCCESS", "REQUEST SENT ")

                    else:
                        MSGBOX.showerror("ERROR", "COULD NOT SEND REQUEST\nPLEASE TRY AGAIN")

                    pass

                def filtdes():
                    sql = "SELECT * FROM vehicle_sharing ORDER BY `vehicle_sharing`.`start_point` ASC "

                    db = MySQLdb.connect(HOST, DATABASE_USERNAME, "", DATABASE)
                    cursor = db.cursor()
                    cursor.execute(sql)
                    hasCar = False
                    allcar = [];
                    veh_cars = []
                    store = {}
                    try:
                        cursor.execute(sql)
                        results = cursor.fetchall()
                        for row_vs in results:
                            i = 0
                            car = []

                            # car.append(row[1] +" to "+row[2])
                            store[row_vs[2] + " to " + row_vs[3]] = int(row_vs[0])

                            allcar.append(row_vs[2] + " to " + row_vs[3])
                            i += 1
                            hasCar = True
                    except:

                        print "Error: unable to fecth data"
                    finally:
                        print allcar
                    # for var in allcar:
                    #     for dist in allcar[0]:
                    #         veh_cars.append(dist)
                    combo_start['values'] = allcar

                def filtdate():
                    sql = "SELECT * FROM vehicle_sharing ORDER BY `vehicle_sharing`.`date` ASC "

                    db = MySQLdb.connect(HOST, DATABASE_USERNAME, "", DATABASE)
                    cursor = db.cursor()
                    cursor.execute(sql)
                    hasCar = False
                    allcar = [];
                    veh_cars = []
                    store = {}
                    try:
                        cursor.execute(sql)
                        results = cursor.fetchall()
                        for row_vs in results:
                            i = 0
                            car = []

                            # car.append(row[1] +" to "+row[2])
                            store[row_vs[2] + " to " + row_vs[3]] = int(row_vs[0])

                            allcar.append(row_vs[2] + " to " + row_vs[3])
                            i += 1
                            hasCar = True
                    except:

                        print "Error: unable to fecth data"
                    finally:
                        print allcar
                    # for var in allcar:
                    #     for dist in allcar[0]:
                    #         veh_cars.append(dist)
                    combo_start['values'] = allcar

                botn1 = Button(panel, text="View \nDetails", pady=10, font=2, relief=GROOVE, command=view)
                botn2 = Button(panel, text="Request \nVehicle", pady=10, font=2, relief=GROOVE, command=getv)
                botn3 = Button(panel, text="Filter \nby Destination", pady=10, font=2, relief=GROOVE, command=filtdes)
                botn4 = Button(panel, text="Filter \nby Date", pady=10, font=2, relief=GROOVE, command=filtdate)

                label_start.grid(row=0, columnspan=3)
                combo_start.grid(row=1, columnspan=3)
                label_info.grid(row=2, columnspan=3)
                botn1.grid(row=3, column=0)
                botn2.grid(row=3, column=1)
                botn3.grid(row=3, column=2)
                botn4.grid(row=3, column=3)
                combo_start.current(0)
                panel.pack()
                app = Vehicle(framboxx)
                framboxx.mainloop()

                pass

            def viewreqs():
                window = Tk()

                window.geometry("450x350+500+300")
                frame = LabelFrame(window, relief=RAISED, borderwidth=1, text="Vehicle Requests", padx=20, pady=30)
                sql_req = """select * from request where user_id = '%s' """ % (profile_username_0['text'])
                print sql_req + "sqlreq"
                lb = Listbox(frame)
                lb.pack(fill=X)

                def view():
                    try:
                        detail = details[lb.selection_get()]
                        print lb.selection_get()
                        sql2 = """select * from users where username = '%s' """ % detail
                        print sql2
                        db2 = MySQLdb.connect(HOST, DATABASE_USERNAME, "", DATABASE)
                        cursor2 = db2.cursor()
                        cursor2.execute(sql2)
                        result = cursor2.fetchone()
                        MSGBOX.showinfo("Driver Info",
                                        "Name: " + result[1] + "\nEmail: " + result[3] + "\nPhone Number: " + result[4])
                    except:
                        MSGBOX.showerror("ERROR", "No Request selected")
                    finally:
                        db2.close()

                    pass

                details = {}
                try:
                    db = MySQLdb.connect(HOST, DATABASE_USERNAME, "", DATABASE)
                    cursor = db.cursor()
                    cursor.execute(sql_req)
                    results = cursor.fetchall()
                    i = 0
                    for rowec in results:
                        lb.insert(i, rowec[1] + " to " + rowec[2] + " (" + rowec[7] + ")")
                        details[rowec[1] + " to " + rowec[2] + " (" + rowec[7] + ")"] = rowec[8]
                        i += 1
                        print rowec[8]
                        pass
                except:
                    print "Error: unable to fecth data"
                finally:
                    db.close()

                view_button = Button(window, text="View ", pady=0, font=2, relief=GROOVE, command=view)
                view_button.pack(side=BOTTOM)
                frame.pack(fill=BOTH)
                app = Vehicle(window)
                window.mainloop()
                # print(sql)
                pass

            def edit():
                valcom = 'Male'
                rot = Tk()
                rot.geometry("400x400+300+200")
                frae = LabelFrame(rot, width=400, height=400, text="EDIT PROFILE INFORMATION", relief=RAISED, padx=20,
                                  pady=30)
                frae.grid(row=0, column=0, sticky='news')
                label_Sname = Label(frae, text="Names")
                label_Saddress = Label(frae, text="Address")
                label_Semail = Label(frae, text="Email")
                label_Smobile = Label(frae, text="Mobile No")
                label_Sender = Label(frae, text="Gender")
                label_Susertype = Label(frae, text="User Type")

                label_Susername = Label(frae, text="Username")
                label_Spassword = Label(frae, text="Password")
                label_Sconfpassword = Label(frae, text="Confirm Password")

                entry_names = Entry(frae, width=30)
                entry_names.insert(1, profile_name_0['text'])
                print profile_name_0['text']
                entry_address = Entry(frae, width=30)
                entry_address.insert(1, profile_address_0['text'])
                entry_email = Entry(frae, width=30)
                entry_email.insert(1, profile_email_0['text'])
                entry_mobile = Entry(frae, width=30)
                entry_mobile.insert(1, profile_mobile_0['text'])
                entry_username = Entry(frae, width=30)
                entry_username.insert(0, profile_username_0['text'])
                entry_password = Entry(frae, width=30, show="*")
                entry_compass = Entry(frae, width=30, show="*")
                cm_gender = ttk.Combobox(frae, width=27, textvariable=valcom, state=DISABLED)
                cm_gender['values'] = (profile_gender_0['text'])

                cm_gender.current(0)
                cm_gender.grid(row=5, column=1)

                cm_usertype = ttk.Combobox(frae, width=27, state=DISABLED)
                cm_usertype['values'] = (profile_type_0['text'])
                cm_usertype.current(0)
                cm_usertype.grid(row=6, column=1)

                label_Sname.grid(column=0, row=1, sticky=W, pady=5)
                label_Saddress.grid(column=0, row=2, sticky=W, pady=5)
                label_Semail.grid(column=0, row=3, sticky=W, pady=5)
                label_Smobile.grid(column=0, row=4, sticky=W, pady=5)
                label_Sender.grid(column=0, row=5, stick=W, pady=5)
                label_Susertype.grid(column=0, row=6, stick=W, pady=5)

                label_Susername.grid(column=0, row=7, sticky=W, pady=5)
                label_Spassword.grid(column=0, row=8, stick=W, pady=5)
                label_Sconfpassword.grid(column=0, row=9, stick=W, pady=5)

                entry_names.grid(row=1, column=1, pady=5)
                entry_address.grid(row=2, column=1, pady=5)
                entry_email.grid(row=3, column=1, pady=5)
                entry_mobile.grid(row=4, column=1, pady=5)

                entry_username.grid(row=7, column=1, pady=5)
                entry_password.grid(row=8, column=1, pady=5)
                entry_compass.grid(row=9, column=1, pady=5)

                errorLabel = Label(frae, text="complete the form ", fg="red")
                errorLabel.grid(row=10, columnspan=3)

                def submit():
                    suc = True
                    sql = "update users set names = '%s', address = '%s', email = '%s', mobile = '%s', username = '%s', password = '%s' where id = '%i'" % (
                        entry_names.get(), entry_address.get(), entry_email.get(), entry_mobile.get(),
                        entry_username.get(),
                        entry_password.get(), int(row[0]))
                    print sql
                    try:
                        db = MySQLdb.connect(HOST, DATABASE_USERNAME, "", DATABASE)
                        cursor = db.cursor()
                        suc = True
                        cursor.execute(sql)
                        db.commit()
                    except:
                        suc = False
                        pass

                    if suc == True:
                        MSGBOX.showinfo("SUCESS!!", "DATA UPDATED SUCESSFULLY")
                    else:
                        MSGBOX.showerror("ERROR", "AN ERROR OCCURED")
                    pass

                but = ttk.Button(frae, text="SUBMIT", command=submit)
                but.grid(row=10, column=0)

                pass

            framboxbtm.pack(side=BOTTOM)
            btn1 = Button(framboxbtm, text="Edit Profile", pady=0, font=2, relief=GROOVE, command=edit)
            btn1.pack(side=LEFT)
            btn2 = Button(framboxbtm, text="Search Vehicle", pady=0, font=2, relief=GROOVE, command=requestVehicle)
            btn2.pack(side=LEFT)
            btn3 = Button(framboxbtm, text="View Requested Vehicle", pady=0, font=2, relief=GROOVE, command=viewreqs)
            btn3.pack(side=LEFT)

            def home():
                rootd.destroy();
                main()

            btn5 = Button(framboxbtm, text="Log out", pady=0, font=2, relief=GROOVE, command=home)
            btn5.pack(side=LEFT)

            frambox.pack(fill="both")
            appr = Vehicle(rootd)
            rootd.attributes('-fullscreen',True)
            rootd.mainloop()

        if (isUser == True):
            MSGBOX.showinfo(title="WELCOME", message="WELCOME " + name + " ")
            if usertype == "Driver":
                doDriverPage()

            elif usertype == "Passenger":
                doPassenger()
        else:
            MSGBOX.showerror("ERROR", "Invalid Username or Password")

    bclivk = Button(frame, text="LOG IN", fg="blue", command=login)
    # bclivk.pack(side=LEFT)

    bclivk.grid(column=1, row=17, columnspan=2)

    # bclivk.bind("<Button-1>",myPrint())
    frame.pack(expand="yes")

    app = Vehicle(root)
    root.attributes('-fullscreen',True)
    root.mainloop()

# calling main method that starts the program
main()

# request time
