from tkinter import *
from tkinter import messagebox
import backend
from tkinter.scrolledtext import ScrolledText

window  = Tk()

window.title("My Data Software")

def login_command():
    global u
    u = str(u_name.get())
    # logged_in(u)
    p = str(password.get())
    if u == "admin" and p == "a":
        logged_in(u)
    else:
        messagebox.showwarning("Failed", "Check Username and Password")

def close_command():
    window.destroy()

window.geometry("300x200")
l1 = Label(window, text = 'Username : ', fg ="blue",
height = 3, width = 10  ,font=("Helvetica", 15), justify = LEFT)
l1.grid(row = 0, column = 0)
u_name = StringVar()
e1 = Entry(window, textvariable = u_name)
e1.grid(row=0,column=3)
l2 = Label(window, text = 'Password : ', fg ="blue" ,font=("Helvetica", 15), justify = LEFT)
l2.grid(row = 1, column = 0)
password = StringVar()
e1 = Entry(window, textvariable = password, show="*")
e1.grid(row=1,column=3)

b = Button(window, text = "Login", bg = "green", width = 12, command = login_command)
b.grid(row=3,column=3)

b1 = Button(window, text = "close",  bg = "Red" , width = 12, command = close_command)
b1.grid(row=5,column=3)

# second screen start from here
def start_logged_in():
    window.destroy()

def logged_in(uname):
    start_logged_in()
    global window_login
    window_login  = Tk()
    window_login.title("Welcome: "+uname)
    window_login.geometry("920x560")
    b2 = Button(window_login, height = 3, width = 12, text = "View Data", fg = "green",command= view_command, justify = LEFT)
    b2.grid(row=0,column=0)
    b3 = Button(window_login, height = 3, width = 12, text = "Start Chat",  command= start_chat, justify = LEFT)
    b3.grid(row=0,column=1)
    b4 = Button(window_login, height = 3, width = 12, text = "Timing",   command = timming, justify = LEFT )
    b4.grid(row=0,column=2)

    gettext = ScrolledText(window_login, height=10,width=100)
    global textPad
    background_image=PhotoImage('wallpaper.jpg')
    textPad = ScrolledText(window_login, image=background_image)
    # textPad.configure(background='#99ff99', )
    # textPad.insert(END, "Welcome "+u )
    textPad.grid(row=1,column=1)

    b6 = Button(window_login, height = 3, width = 12, text = "Logout", fg ="red", command = close_logged_in_command, justify = LEFT)
    b6.grid(row=2,column=0)

    b6 = Button(window_login, height = 3, width = 12, text = "Clear Data", fg ="red", command = clear_data_command, justify = LEFT)
    b6.grid(row=2,column=2)

def clear_data_command():
    textPad.delete('1.0', END)

def view_command():
    for row in backend.view_data():
        textPad.insert(END, row[0] +": "+ str(row[1])+"\n" )

def get_selected_row(event):
    print(list1.curselection()[0])

def start_chat():
    window_login.destroy()
    global start_chat_window
    global gettext
    global sendtext
    global textPad
    start_chat_window = Tk()
    start_chat_window.title( "Welcome "+u + " Created By Pardeep"  )
    start_chat_window.geometry("500x500")
    gettext = ScrolledText(start_chat_window, height=10,width=100)
    textPad = ScrolledText(start_chat_window)
    # textPad.insert(END, "Welcome "+u )
    textPad.pack()
    sframe = Frame(start_chat_window)
    sframe.pack(anchor='w')
    pro = Label(sframe, text= "< " + u + " >");
    sendtext = Entry(sframe,width=80)
    sendtext.focus_set()
    sendtext.bind(sequence="<Return>", func=Send)
    pro.pack(side=LEFT)
    sendtext.pack(side=LEFT)
    b4 = Button(start_chat_window, text = "Logout !", bg ="Red",  command = Logout_command_for_chat, justify = LEFT )
    b4.pack(side=LEFT)

def Send(args):
    gettext.configure(state='normal')
    text = sendtext.get()
    textPad.insert(END, u +": "+ text+"\n" )
    sendtext.delete(0, 'end')

def Logout_command_for_chat():
    start_chat_window.destroy()

def timming():
    print("timming")

def status():
    print("status")

def close_logged_in_command():
    window_login.destroy()

window.mainloop()
