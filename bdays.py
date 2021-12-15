from tkinter import *
from bs4 import BeautifulSoup as bs
from bokeh.plotting import figure, show, output_file
import bdays_backend, datetime, requests, calendar, tkinter.messagebox

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        for i in range(4):
            eval("e" + str(i+1)).delete(0,END)
            eval("e" + str(i+1)).insert(END,selected_tuple[i])
    except IndexError:
        pass

def view_cmd():
    list1.delete(0,END)
    for row in bdays_backend.view():
        list1.insert(END,row)

def search_cmd():
    list1.delete(0,END)
    for row in bdays_backend.search(name_text.get().title(),day_text.get(),month_text.get(),year_text.get()):
        list1.insert(END,row)

def addlist_cmd():
    box_text=t1.get("1.0",'end-1c')
    names_list = [y.title() for y in (x.strip() for x in box_text.splitlines()) if y]
    list1.delete(0,END)
    for name in names_list:
        url = 'https://en.wikipedia.org/wiki/' + name
        r = requests.get(url)
        soup = bs(r.content,'lxml')
        birthday = soup.find('span',{'class':'bday'})
        try:
            date = birthday.get_text()
        except AttributeError:
            list1.insert(END,(name + '...not found!'))
            continue
        bday = datetime.datetime.strptime(date,'%Y-%m-%d')
        bdays_backend.add(name,bday.day,bday.month,bday.year)
        list1.insert(END,(name,bday.day,bday.month,bday.year))

def add_cmd():
    entries = [name_text.get().title(),day_text.get(),month_text.get(),year_text.get()]
    if '' in entries:
        return tkinter.messagebox.showerror( "Error message", "You have empty fields!")
    elif '%' in entries[0]:
        return tkinter.messagebox.showerror( "Error message", "You can't add '%' symbol!")
    try:
        date = datetime.datetime(int(entries[3]),int(entries[2]),int(entries[1])).date()
    except ValueError:
        return tkinter.messagebox.showerror( "Error message", "Wrong Date!")
    if date > datetime.date.today():
        return tkinter.messagebox.showerror( "Error message", "Date in Future!")
    bdays_backend.add(entries[0],entries[1],entries[2],entries[3])
    list1.delete(0,END)
    list1.insert(END,entries)

def delete_cmd():
    bdays_backend.delete(selected_tuple[0])
    view_cmd()

def graph_cmd():
    month_count = bdays_backend.count_months()
    x = [calendar.month_name[element[0]] for element in month_count]
    y = [element[1] for element in month_count]
    # Creating Graph
    output_file("bdays.html")
    p = figure(x_range=calendar.month_name[1:], plot_width=600, plot_height=350)
    p.xaxis.major_label_orientation = 0.785
    p.xaxis.axis_label = "Months"
    p.xgrid.grid_line_color = None
    p.yaxis.minor_tick_line_color = None
    p.yaxis.axis_label = "Birthdays per month"
    p.vbar(x=x, top=y, width=0.5, color="#69ded8")
    show(p)

window = Tk()

window.wm_title("Birthdays List v1.0")

# Fields Labels
l1 = Label(window,text="Name")
l1.grid(row=0,column=0)

l2 = Label(window,text="Day")
l2.grid(row=0,column=2)

l3 = Label(window,text="Month")
l3.grid(row=0,column=4)

l4 = Label(window,text="Year")
l4.grid(row=0,column=6)

l5 = Label(window,text="Enter list of names to add:")
l5.grid(row=1,column=0,columnspan=2)

l6 = Label(window,text="Results:")
l6.grid(row=1,column=8)

# Entry Fields
name_text=StringVar()
e1=Entry(window,textvariable=name_text,width=25)
e1.grid(row=0,column=1)

day_text=StringVar()
e2=Entry(window,textvariable=day_text,width=3)
e2.grid(row=0,column=3)

month_text=StringVar()
e3=Entry(window,textvariable=month_text,width=3)
e3.grid(row=0,column=5)

year_text=StringVar()
e4=Entry(window,textvariable=year_text,width=6)
e4.grid(row=0,column=7)

t1=Text(window,height=15,width=30)
t1.grid(row=2,column=0,columnspan=2,rowspan=7)

# List & Skrollbar
list1=Listbox(window,height=15,width=40)
list1.grid(row=2,column=8,rowspan=7)

sb1=Scrollbar(window)
sb1.grid(row=2,column=9,rowspan=7)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

# Buttons
b1=Button(window,text="View All",width=14,command=view_cmd)
b1.grid(row=2,column=4,columnspan=3)

b2=Button(window,text="Add from List",width=14,command=addlist_cmd)
b2.grid(row=3,column=4,columnspan=3)

b3=Button(window,text="Add Manually",width=14,command=add_cmd)
b3.grid(row=4,column=4,columnspan=3)

b4=Button(window,text="Search Database",width=14,command=search_cmd)
b4.grid(row=5,column=4,columnspan=3)

b5=Button(window,text="Delete Entry",width=14,command=delete_cmd)
b5.grid(row=6,column=4,columnspan=3)

b6=Button(window,text="Births by Month",width=14,command=graph_cmd)
b6.grid(row=7,column=4,columnspan=3)

b7=Button(window,text="Exit",width=14,command=window.destroy)
b7.grid(row=8,column=4,columnspan=3)


window.mainloop()