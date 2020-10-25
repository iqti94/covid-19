from tkinter import *
from PIL import ImageTk,Image
from  tkinter import ttk
import tkinter as  tk
from tkinter import messagebox
import random
from threading import *
from time import *
import pyttsx3
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame
import cProfile
####### VOICE ########
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
engine.say("WELCOME TO COVID-19 DATA ANALYSIS")
############ OVERVIEW #########
url="https://www.worldometers.info/coronavirus/"
r=requests.get(url)
data=r.content
soup=BeautifulSoup(data,"html.parser")
cases=soup.find_all('div',class_="maincounter-number")
########## ACTIVE CASES #########
url2="https://www.worldometers.info/coronavirus/"
r2=requests.get(url2)
data2=r2.content
soup2=BeautifulSoup(data2,"html.parser")
cases2=soup2.find_all('div',class_="number-table-main")

url3="https://www.worldometers.info/coronavirus/"
r3=requests.get(url3)
data3=r3.content
soup3=BeautifulSoup(data3,"html.parser")
cases3=soup3.find_all('span',class_="number-table")
######### CLOSED CASES ########
url4="https://www.worldometers.info/coronavirus/"
r4=requests.get(url4)
data4=r4.content
soup4=BeautifulSoup(data4,"html.parser")
cases4=soup4.find_all('div',class_="number-table-main")
b=[items.get_text() for items in cases4]

url5="https://www.worldometers.info/coronavirus/"
r5=requests.get(url5)
data5=r5.content
soup5=BeautifulSoup(data5,"html.parser")
cases5=soup5.find_all('span',class_="number-table")
b1=[items.get_text() for items in cases5]
########## WORLD & GRAPH ###########
source=requests.get("https://www.worldometers.info/coronavirus/").text
soup=BeautifulSoup(source,'lxml')
match=soup.find('tbody')
match=match.find_all('tr')

##### OVERVIEW WINDOW #######
global bckimg
global btnimg
def overview():
    global bckimg
    global btnimg
    over=tk.Toplevel()
    over.geometry("1250x200")
    over.title("OVERVIEW")
    over.resizable(FALSE,FALSE)
    over.wm_iconbitmap("./icon/icn.ico")
    bckimg=ImageTk.PhotoImage(Image.open("./images/bck1.jpg"))
    bcklbl=tk.Label(over,image=bckimg,width=1250,height=200)
    bcklbl.pack(expand=TRUE)
    def ovrlbl(e):
        overview_lbl['bg']="light green"
        overview_lbl.config(bg="light green",fg="black")
        overview_lbl['fg']="black"
    def ovrlbl2(f):
        overview_lbl['bg']="light green"
        overview_lbl.config(bg="black",fg="white")
    def ovrlbl3(e):
        overview_lbl2['bg']="light green"
        overview_lbl2.config(bg="light green",fg="black")
        overview_lbl2['fg']="black"
    def ovrlbl4(f):
        overview_lbl2['bg']="light green"
        overview_lbl2.config(bg="black",fg="white")
    def ovrlbl5(e):
        overview_lbl3['bg']="light green"
        overview_lbl3.config(bg="light green",fg="black")
        overview_lbl3['fg']="black"
    def ovrlbl6(f):
        overview_lbl3['bg']="light green"
        overview_lbl3.config(bg="black",fg="white")

    lbl=tk.Label(over,text="OVERVIEW",font="Georgia 35 bold",relief=GROOVE,fg="white",bg="black"
              ,bd=0)
    lbl.place(x=500,y=0)
    frame4=tk.Frame(over,width=30,relief=GROOVE)
    frame4.config(highlightcolor="light green",bg="light green",bd=2,highlightbackground="light green")
    frame4.place(x=0,y=80)
    overview_lbl=tk.Label(frame4,highlightcolor="light green",font="Helvetica 20 bold italic",width=22,relief=GROOVE
                         ,bg="black" ,fg="white",bd=0,highlightbackground="light green")
    overview_lbl['text']=f"Corona Cases: {cases[0].get_text().strip()}"
    overview_lbl.grid(row=1,column=1)
    overview_lbl.bind("<Enter>",ovrlbl)
    overview_lbl.bind("<Leave>",ovrlbl2)
    frame5=tk.Frame(over,width=30,relief=GROOVE)
    frame5.config(highlightcolor="light green",bg="light green",bd=2,highlightbackground="light green")
    frame5.place(x=400,y=80)
    overview_lbl2=tk.Label(frame5,font="Helvetica 20 bold italic",highlightcolor="light green",width=22
                           ,relief=GROOVE,fg="white"
             ,bg="black" ,bd=0,highlightbackground="light green")
    overview_lbl2['text']=f"Death Cases: {cases[1].get_text().strip()}"
    overview_lbl2.grid(row=1,column=2,padx=(0,10))
    overview_lbl2.bind("<Enter>",ovrlbl3)
    overview_lbl2.bind("<Leave>",ovrlbl4)

    frame6=tk.Frame(over,width=35,relief=GROOVE)
    frame6.config(highlightcolor="light green",bg="light green",bd=2)
    frame6.place(x=800,y=80)
    overview_lbl3=tk.Label(frame6,highlightcolor="light green",highlightbackground="light green"
                           ,font="Helvetica 20 bold italic",width=25,relief=GROOVE,fg="white"
              ,bd=0,bg="black")
    overview_lbl3['text']=f"Recovered Cases: {cases[2].get_text().strip()}"
    overview_lbl3.grid(row=1,column=3,padx=(0,10))
    overview_lbl3.bind("<Enter>",ovrlbl5)
    overview_lbl3.bind("<Leave>",ovrlbl6)
    def talk():
        engine.say(f"Corona Cases: {cases[0].get_text().strip()}")
        engine.say(f"Death Cases: {cases[1].get_text().strip()}")
        engine.say(f"Recovered Cases: {cases[2].get_text().strip()}")
        engine.runAndWait()
        engine.stop()
    btnimg=ImageTk.PhotoImage(Image.open("./images/img12.png"))
    btn=tk.Button(over,text="SPEAK",font="Helvetica 20 bold italic",relief=GROOVE,image=btnimg
              ,bd=0,command=talk)
    btn.place(x=1050,y=150)
######## ACTIVE CASES WINDOW #######
global bckimg1
global btnimg
def Cases():
    global bckimg1
    global cases2
    global cases3
    global btnimg
    case=tk.Toplevel()
    case.geometry("1250x200")
    case.config(bg="black")
    case.title("ACTIVE CASES")
    case.resizable(FALSE,FALSE)
    case.wm_iconbitmap("./icon/icn.ico")
    bckimg1=ImageTk.PhotoImage(Image.open("./images/bck2.jpg"))
    bcklbl1=tk.Label(case,image=bckimg1,width=1250,height=200)
    bcklbl1.pack(expand=TRUE)
    lbl2=tk.Label(case,text="ACTIVE CASES",font="Georgia 40 bold",relief=GROOVE,bg="black",fg="#ffffff"
              ,highlightthickness=2,bd=0,highlightcolor="light green",highlightbackground="light green")
    lbl2.place(x=430,y=0)
    def case_lbl1(e):
        case_lbl['bg']="light green"
        case_lbl.config(bg="light green",fg="black")
        case_lbl['fg']="black"
    def case_lbl2(f):
        case_lbl['bg']="light green"
        case_lbl.config(bg="black",fg="white")
    def mild_lbl1(e):
        mild_lbl['bg']="light green"
        mild_lbl.config(bg="light green",fg="black")
        mild_lbl['fg']="black"
    def mild_lbl2(f):
        mild_lbl['bg']="light green"
        mild_lbl.config(bg="black",fg="white")
    def serious_lbl1(e):
        serious_lbl['bg']="light green"
        serious_lbl.config(bg="light green",fg="black")
        serious_lbl['fg']="black"
    def serious_lbl2(f):
        serious_lbl['bg']="light green"
        serious_lbl.config(bg="black",fg="white")
    case_frame=tk.Frame(case,width=30,relief=GROOVE)
    case_frame.config(highlightcolor="light green",bg="light green",bd=2,highlightbackground="light green")
    case_frame.place(x=0,y=80)
    case_lbl=tk.Label(case_frame,highlightcolor="light green",font="Helvetica 20 bold italic",width=22,relief=GROOVE,bg="black",fg="white"
              ,bd=0,highlightbackground="light green")
    case_lbl['text']=f"Cases: {cases2[0].get_text().strip()}"
    case_lbl.grid(row=1,column=1)
    case_lbl.bind("<Enter>",case_lbl1)
    case_lbl.bind("<Leave>",case_lbl2)

    mild_frame=tk.Frame(case,width=30,relief=GROOVE)
    mild_frame.config(highlightcolor="light green",bg="light green",bd=2,highlightbackground="light green")
    mild_frame.place(x=400,y=80)
    mild_lbl=tk.Label(mild_frame,highlightcolor="light green",font="Helvetica 20 bold italic",width=22,relief=GROOVE,bg="black",fg="white"
              ,bd=0,highlightbackground="light green")
    mild_lbl['text']=f"In Mild Condition: {cases3[0].get_text().strip()}"
    mild_lbl.grid(row=1,column=2)
    mild_lbl.bind("<Enter>",mild_lbl1)
    mild_lbl.bind("<Leave>",mild_lbl2)

    serious_frame=tk.Frame(case,width=45,relief=GROOVE)
    serious_frame.config(highlightcolor="light green",bg="light green",bd=2,highlightbackground="light green")
    serious_frame.place(x=800,y=80)
    serious_lbl=tk.Label(serious_frame,highlightcolor="light green",font="Helvetica 20 bold italic",width=22,relief=GROOVE,bg="black",fg="white"
              ,bd=0,highlightbackground="light green")
    serious_lbl['text']=f"In Serious or Critical: {cases3[1].get_text().strip()}"
    serious_lbl.grid(row=1,column=3)
    serious_lbl.bind("<Enter>",serious_lbl1)
    serious_lbl.bind("<Leave>",serious_lbl2)
    def talk():
        engine.say(f"Cases: {cases2[0].get_text().strip()}")
        engine.say(f"In Mild Condition: {cases3[0].get_text().strip()}")
        engine.say(f"In Serious or Critical: {cases3[1].get_text().strip()}")
        engine.runAndWait()
        engine.stop()
    btnimg=ImageTk.PhotoImage(Image.open("./images/img12.png"))
    btn=tk.Button(case,text="SPEAK",font="Helvetica 20 bold italic",relief=GROOVE,image=btnimg
              ,bd=0,command=talk)
    btn.place(x=1050,y=147)
######## CLOSED CASES WINDOW ##########
global btnimg
global bckimg2
def deaths():
    global bckimg2
    global b
    global b1
    global btnimg
    close=tk.Toplevel()
    close.geometry("1200x230")
    close.config(bg="black")
    close.title("CLOSED CASES")
    close.resizable(FALSE,FALSE)
    close.wm_iconbitmap("./icon/icn.ico")
    bckimg2=ImageTk.PhotoImage(Image.open("./images/bck3.jpg"))
    bcklbl2=tk.Label(close,image=bckimg2,width=1200,height=230)
    bcklbl2.pack(expand=TRUE)
    close_lbl=tk.Label(close,text="CLOSED CASES",font="Georgia 40 bold",relief=GROOVE,bg="black",fg="#ffffff"
              ,highlightthickness=2,bd=0,highlightcolor="light green",highlightbackground="light green")
    close_lbl.place(x=380,y=0)
    def lbl_click(e):
        close_lbl1['bg']="light green"
        close_lbl1.config(bg="light green",fg="black")
        close_lbl1['fg']="black"
    def lbl_leave(f):
        close_lbl1['bg']="light green"
        close_lbl1.config(bg="black",fg="white")
    def lbl_click1(e):
        recover_lbl['bg']="light green"
        recover_lbl.config(bg="light green",fg="black")
        recover_lbl['fg']="black"
    def lbl_leave1(f):
        recover_lbl['bg']="light green"
        recover_lbl.config(bg="black",fg="white")
    def lbl_click2(e):
        death_lbl['bg']="light green"
        death_lbl.config(bg="light green",fg="black")
        death_lbl['fg']="black"
    def lbl_leave2(f):
        death_lbl['bg']="light green"
        death_lbl.config(bg="black",fg="white")

    close_frame=tk.Frame(close,width=40,relief=GROOVE)
    close_frame.config(highlightcolor="light green",bg="light green",bd=2,highlightbackground="light green")
    close_frame.place(x=0,y=80)
    close_lbl1=tk.Label(close_frame,highlightcolor="light green",font="Helvetica 20 bold italic",width=30,relief=GROOVE,bg="black",fg="white"
              ,bd=0,highlightbackground="light green")
    close_lbl1['text']=f"Cases which had outcome: {b[1]}"
    close_lbl1.grid(row=1,column=0)
    close_lbl1.bind("<Enter>",lbl_click)
    close_lbl1.bind("<Leave>",lbl_leave)

    recoverd_frame=tk.Frame(close,width=40,relief=GROOVE)
    recoverd_frame.config(highlightcolor="light green",bg="light green",bd=2,highlightbackground="light green")
    recoverd_frame.place(x=560,y=80)
    recover_lbl=tk.Label(recoverd_frame,highlightcolor="light green",font="Helvetica 20 bold italic",width=30,relief=GROOVE,bg="black",fg="white"
              ,bd=0,highlightbackground="light green")
    recover_lbl['text']=f"Recovered/Discharged: {b1[2]}"
    recover_lbl.grid(row=1,column=1)
    recover_lbl.bind("<Enter>",lbl_click1)
    recover_lbl.bind("<Leave>",lbl_leave1)

    deaths_frame=tk.Frame(close,width=40,relief=GROOVE)
    deaths_frame.config(highlightcolor="light green",bg="light green",bd=2,highlightbackground="light green")
    deaths_frame.place(x=240,y=160)
    death_lbl=tk.Label(deaths_frame,highlightcolor="light green",font="Helvetica 20 bold italic",width=30,relief=GROOVE,bg="black",fg="white"
              ,bd=0,highlightbackground="light green")
    death_lbl['text']=f"Deaths: {b1[3]}"
    death_lbl.grid(row=1,column=1)
    death_lbl.bind("<Enter>",lbl_click2)
    death_lbl.bind("<Leave>",lbl_leave2)
    def talk():
        engine.say(f"Cases which had outcome: {b[1]}")
        engine.say(f"Recovered/Discharged: {b1[2]}")
        engine.say(f"Deaths: {b1[3]}")
        engine.runAndWait()
        engine.stop()
    btnimg=ImageTk.PhotoImage(Image.open("./images/img12.png"))
    btn=tk.Button(close,text="SPEAK",font="Georgia 25 bold italic",image=btnimg,relief=GROOVE,bg="white",fg="pink"
              ,bd=0,command=talk)
    btn.place(x=1050,y=165)
########### COUNTRY WINDOW ###########
global ctnimg
global talk
global country
global btnimg
def countries_affected():
    global ctnimg
    global country
    global btnimg
    country=""
    def submit():
        global ctnimg
        global country
        global b
        global talk
        global btnimg
        country=lblentry.get()
        url1="https://www.worldometers.info/coronavirus/country/" + country
        response=requests.get(url1)
        data1=response.content
        soup1=BeautifulSoup(data1,"html.parser")
        cases1=soup1.find_all('div',class_="maincounter-number")
        b=[items.get_text() for items in cases1]

        showframe=tk.Frame(ctn,relief=GROOVE)
        showframe.config(highlightthickness=2,highlightbackground="light green",bg="#252525",width=20)
        showframe.place(x=0,y=450)
        showlbl=tk.Label(showframe,text=f"Total cases in {country}: ".replace("-",' '),font="Helvetica 17 bold italic",relief=GROOVE,width=22,bd=0,bg="#252525"
                     ,fg="white")
        showlbl.grid(row=5,column=0)
        showlbl=tk.Label(showframe,text=b[0],font="Helvetica 17 bold italic",relief=GROOVE,width=16,bd=0,bg="#252525"
                     ,fg="white")
        showlbl.grid(row=5,column=1,padx=(0,10))

        deathframe=tk.Frame(ctn,relief=GROOVE)
        deathframe.config(highlightthickness=2,highlightbackground="light green",bg="#252525",width=23)
        deathframe.place(x=660,y=450)
        deathlbl=tk.Label(deathframe,text=f"Death Cases in {country}: ".replace('-',' '),font="Helvetica 17 bold italic",relief=GROOVE,width=23,bd=0,bg="#252525"
                       ,fg="white")
        deathlbl.grid(row=5,column=1)
        deathlbl=tk.Label(deathframe,text=b[1],font="Helvetica 17 bold italic",relief=GROOVE,width=13,bd=0,bg="#252525",fg="white")
        deathlbl.grid(row=5,column=2,padx=(0,10))

        recoverframe=tk.Frame(ctn,relief=GROOVE)
        recoverframe.config(highlightthickness=2,highlightbackground="light green",bg="#252525",width=30)
        recoverframe.place(x=300,y=600)
        recvrlbl=tk.Label(recoverframe,text=f"Recovered Cases in {country}: ".replace('-',' '),font="Helvetica 17 bold italic",relief=GROOVE,width=28,bd=0,bg="#252525",
                       fg="white" )
        recvrlbl.grid(row=6,column=0)
        recvrlbl=tk.Label(recoverframe,text=b[2],font="Helvetica 17 bold italic",relief=GROOVE,width=17,bd=0,bg="#252525",
                       fg="white")
        recvrlbl.grid(row=6,column=1,padx=(0,10))

    def refresh():
        newdata=submit()
        refresh_ctn['text']=newdata

    ctn=tk.Toplevel()
    ctn.geometry("1280x853")
    ctn.title("COUNTRIES")
    ctn.resizable(FALSE,FALSE)
    ctn.wm_iconbitmap("./icon/icn.ico")
    ctnimg=ImageTk.PhotoImage(Image.open("./images/cntry1.jpg"))
    ctnlbl=tk.Label(ctn,image=ctnimg,width=1280,height=853)
    ctnlbl.place(x=0,y=0)
    ctnry_lbl=tk.Label(ctn,text="COUNTRIES",font="Georgia 40 bold",relief=GROOVE,bg="light green",fg="#252525",bd=0)
    ctnry_lbl.pack(fill=Y)
    lblctn=tk.Label(ctn,text="Enter Country Name: ",font="Georgia 22 bold italic",relief=GROOVE,bd=0,bg="sky blue"
                 ,fg="#252525")
    lblctn.place(x=40,y=210)
    lblentry=tk.Entry(ctn,font="Georgia 22 bold italic",relief=GROOVE,width=30,bd=6)
    lblentry.place(x=400,y=200)
    def ctnclick(e):
        btn_ctn['bg']="orange"
        btn_ctn.config(bg="orange",fg="#252525")
        btn_ctn['fg']="black"
    def ctnleave(f):
        btn_ctn['bg']="light green"
        btn_ctn.config(bg="light green",fg="#252525")
    def ctnclick1(e):
        refresh_ctn['bg']="orange"
        refresh_ctn.config(bg="orange",fg="#252525")
        refresh_ctn['fg']="black"
    def ctnleave1(f):
        refresh_ctn['bg']="light green"
        refresh_ctn.config(bg="light green",fg="#252525")

    btn_ctn=tk.Button(ctn,text="FIND INFO",font="Georgia 20 bold italic",relief=GROOVE,width=18,bd=1,command=submit,bg="light green",
                   fg="#252525",activebackground="light green",activeforeground="#252525")
    btn_ctn.place(x=230,y=300)
    btn_ctn.bind("<Enter>",ctnclick)
    btn_ctn.bind("<Leave>",ctnleave)
    refresh_ctn=tk.Button(ctn,text="REFRESH",font="Georgia 20 bold italic",relief=GROOVE,width=18,bd=1,bg="light green",
                   fg="#252525",command=refresh,activebackground="light green",activeforeground="#252525")
    refresh_ctn.place(x=600,y=300)
    refresh_ctn.bind("<Enter>",ctnclick1)
    refresh_ctn.bind("<Leave>",ctnleave1)
    def talk():
        engine.say(f"Total cases in {country}: {b[0]} ".replace("-",' '))
        engine.say(f"Death Cases in {country}: {b[1]} ".replace('-',' '))
        engine.say(f"Recovered Cases in {country}: {b[2]} ".replace('-',' '))
        engine.runAndWait()
        engine.stop()
    btnimg=ImageTk.PhotoImage(Image.open("./images/img12.png"))
    btn=tk.Button(ctn,text="SPEAK",font="Helvetica 20 bold italic",relief=GROOVE,image=btnimg
              ,bd=0,command=talk)
    btn.place(x=1020,y=300)
######## WORLD & GRAPH WINDOW ########
def world():
    root=tk.Toplevel()
    root.geometry('820x500')
    root.config(bg='#252525')
    root.title('WORLD & GRAPH')
    root.resizable(FALSE,FALSE)
    root.wm_iconbitmap("./icon/icn.ico")
    lbl=tk.Label(root,text="WORLD AND GRAPH ",font="Georgia 35  bold italic",width=25,fg="sky blue",bg="#252525",bd=0)
    lbl.pack(fill=Y)
   
    s = ttk.Style()
    s.configure('TNotebook.Tab', font=('Comic Sans MS','15'))
    tab=ttk.Notebook(root)
    
    style = ttk.Style()
    style.map("C.TButton",
        foreground=[('pressed', 'red'), ('active', 'blue')],
        background=[('pressed', '!disabled', 'black'), ('active', 'white')]
        )
    style.configure('TButton', font =
                   ('calibri',18, 'bold'),
                        borderwidth = '1')
   
    world=[]
    continents=[]
    no=0
    for i in match:
       data=i.text.split('\n')
       fun=lambda a:False if a=='' else True
       data=list(filter(fun,data))
       if no<8:
          continents.append(data)
          no+=1
          continue
       world.append(data)
    
    all_=tk.Frame(tab, bg='white',width="800",height="500")
    tab.add(all_,text="  world  ")

    for i in ['Cases','Recovered','Death']:
       mm=i
       globals()[mm]=Frame(tab, bg='black',width="800",height="600")
       tab.add(eval(mm),text='  '+i+'  ')
    tab.place(x=10,y=100,width=800,height=400)
    tree=ttk.Treeview(all_)
    
    name=[]
    cases=[]
    a=0
    no=[]
    for i in match:
       data=i.text.split('\n')
       fun=lambda a:False if a=='' else True
       data=list(filter(fun,data))
       name.append(data[0])
       value=int(data[1].replace(',',''))
       cases.append(value)
       a+=1
       no.append(a)
       if a==6:
          break
    data1 = {'Country':name,
             'Cases':cases
            }
    df1 = DataFrame(data1,columns=['Country','Cases'])

    figure1 = plt.Figure(figsize=(5,6), dpi=100)
    ax1 = figure1.add_subplot(111)
    line1 = FigureCanvasTkAgg(figure1, Cases)
    line1.get_tk_widget().pack(fill=BOTH)
    df1 = df1[['Country','Cases']].groupby('Country').sum()
    df1.plot(kind='line', legend=True, ax=ax1, color='orange',marker='o', fontsize=10)
    ax1.set_title('Cases')
    ax1.tick_params(axis='x', labelrotation=10)
   
    name=[]
    cases=[]
    a=0
    no=[]
    for i in match:
       data=i.text.split('\n')
       fun=lambda a:False if a=='' else True
       data=list(filter(fun,data))
       name.append(data[0])
       value=int(data[4].replace(',',''))
       cases.append(value)
       a+=1
       no.append(a)
       if a==6:
          break
    data2 = {'Country':name,
             'Recovered':cases
            }
    df2 = DataFrame(data2,columns=['Country','Recovered'])

    figure2 = plt.Figure(figsize=(5,4), dpi=100)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, Recovered)
    line2.get_tk_widget().pack(fill=BOTH)
    df2 = df2[['Country','Recovered']].groupby('Country').sum()
    df2.plot(kind='line', legend=True, ax=ax2, color='green',marker='o', fontsize=10)
    ax2.set_title('Recovered')
    ax2.tick_params(axis='x', labelrotation=10)
   
    name=[]
    cases=[]
    a=0
    no=[]
    for i in match:
       data=i.text.split('\n')
       fun=lambda a:False if a=='' else True
       data=list(filter(fun,data))
       name.append(data[0])
       value=int(data[3].replace(',',''))
       cases.append(value)
       a+=1
       no.append(a)
       if a==6:
          break
    data3 = {'Country':name,
             'Death':cases
            }
    df3 = DataFrame(data3,columns=['Country','Death'])

    figure3 = plt.Figure(figsize=(5,4), dpi=100)
    ax3 = figure3.add_subplot(111)
    line3 = FigureCanvasTkAgg(figure3,Death)
    line3.get_tk_widget().pack(fill=BOTH)
    df3 = df3[['Country','Death']].groupby('Country').sum()
    df3.plot(kind='line', legend=True, ax=ax3, color='r',marker='o', fontsize=10)
    ax3.set_title('Death')
    ax3.tick_params(axis='x', labelrotation=10)


    cnty=('sno','country','Total Cases','New Cases','Total Death',
                     'Total Recovered','Active Cases','Serious Critical')
    tree['columns']=cnty
    tree.column('#0',width=50)
    tree.column('#1',width=120)
    for i in range(2,8):
       if i==1:
          tree.column('#'+str(i),width=150)
          continue
       tree.column('#'+str(i),width=105)
    for i in range(8):
       tree.heading('#'+str(i),text=cnty[i])
    a=1
    for country in world:
       try:
          tree.insert('',str(a),'item '+str(a),text=a,values=(country[0],country[1],country[2],
                                                              country[3],country[4],country[5],country[6]), tags = ('oddrow',))
          a+=1
       except:
          pass

    tree.tag_configure('oddrow', background='white')
    for i in continents:
       if i[0].lower()=='world':
          break

    tree.pack()
###### DEATH RATE WINDOW ########
def death_rate():
    root=tk.Toplevel()
    root.geometry("1300x1000")
    root.title("DEATH RATE")
    root.config(bg="#252525")
    root.wm_iconbitmap("./icon/icn.ico")
    lbl1=tk.Label(root,text="DEATH RATE",font="Georgia 40 bold italic",bg="#252525",fg="sky blue",width=25,bd=0)
    lbl1.pack(fill=Y)
    frame=tk.Frame(root,width=800,relief=GROOVE,bg="#252525")
    frame.config(highlightthickness=2,highlightbackground="light green",highlightcolor="light green")
    frame.pack(expand=TRUE,pady=(10,0),fill=BOTH)
    scrollbar = tk.Scrollbar(frame,relief=GROOVE,bg="#252525")
    scrollbar.config(bg="#252525")
    scrollbar.pack(side=RIGHT, fill=Y)
    lbl3 =tk.Text(frame, yscrollcommand=scrollbar.set,width=100,bg="white",fg="#252525",bd=0,font="Helvetica 16 bold italic")
    lbl3.place(x=0,y=20)
    lbl3.insert(END,
    ''' INTRODUCTION:
         When calculating the mortality rate, we need:
    
1.The number of actual cases. We need to know the number of actual cases(not merely the reported ones, which are typically only a small portion of the actual ones)
that have already had an outcome (positive or negative: recovery or death)
not the current cases that still have to resolve(the case sample shall contain zero active cases and include only "closed" cases).
    
2.The number of actual deaths related to the closed cases examined above.
    
Considering that a large number of cases are asymptomatic(or present with very mild symptoms) and that
testing has
not been performed on the entire population,
only a fraction of the SARS-CoV-2 infected population is detected, confirmed through a laboratory test, and officially reported as a COVID-19 case. The number of actual cases is therefore estimated to be at
several multiples above the number of reported cases. The number of deaths also tends to be underestimated,
as some patients are not hospitalized and not tested.
If we base our calculation (deaths / cases) on the number of reported cases(rather than on the actual ones),we will greatly overestimate the fatality rate.
    
   
2. Fatality Rate based on New York City Actual Cases and Deaths:
    
       Worldometer has analyzed the data provided by New York City, the New York State antibody study, 
and the excess deaths analysis by the CDC. Combining these 3 sources together we can derive 
the most accurate estimate to date on the mortality rate for COVID-19, as well as the 
mortality rate by age group and underlying condition. These findings can be valid 
for New York City and not necessarily for other places (suburban or rural areas, 
other countries, etc.), 
but they represent the best estimates to date given the co-occurrence of these 3 studies.
    
    
3.Actual Cases (1.7 million: 10 times the number of confirmed cases):
    
          New York State conducted an antibody testing study [source], showing that 12.3% of the population in the 
state had COVID-19 antibodies as of May 1, 2020. The survey developed a baseline infection rate by 
testing 15,103 people at grocery stores and community centers across the state over the 
preceding two weeks. The study provides a breakdown by county, 
race (White 7%, Asian 11.1%, multi/none/other 14.4%, Black 17.4%, Latino/Hispanic 25.4%), and age, 
among other variables. 19.9% of the population of New York City had COVID-19 antibodies. 
With a population of 8,398,748 people in NYC [source], this percentage would indicate that 
1,671,351 people had been infected with SARS-CoV-2 and had recovered as of May 1 in New York City. 
The number of confirmed cases reported as of May 1 by New York City was 166,883 [source], 
more than 10 times less.
    
    
4.ACTUAL DEATHS (23,000: almost twice the number of confirmed deaths):
    
       As of May 1, New York City reported 13,156 confirmed deaths and 5,126 probable deaths (deaths with COVID-19 on the death certificate but no laboratory test performed), for a total of 18,282 deaths [source]. The CDC on May 11 released its "Preliminary Estimate of Excess Mortality During the COVID-19 Outbreak — New York City, March 11–May 2, 2020" [source] in which it calculated an estimate of actual COVID-19 deaths in NYC by analyzing the "excess deaths" (defined as "the number of deaths above expected seasonal baseline levels, regardless of the reported cause of death") and found that, in addition to the confirmed and probable deaths reported by the city, there were an estimated 5,293 more deaths to be attributed. After adjusting for the previous day (May 1), we get 5,148 additional deaths, for a total of actual deaths of 13,156 confirmed + 5,126 probable + 5,148 additional excess deaths calculated by CDC = 23,430 actual COVID-19 deaths as of May 1, 2020 in New York City.
    
    
5.INFECTION Fatality Rate (23k / 1.7M = 1.4% IFR):
    
        Actual Cases with an outcome as of May 1 = estimated actual recovered (1,671,351) + estimated actual deaths (23,430) = 1,694,781.
Infection Fatality Rate (IFR) = Deaths / Cases = 23,430 / 1,694,781 = 1.4% (1.4% of people infected with SARS-CoV-2 have a fatal outcome, while 98.6% recover).   
    
    
6. MORTALITY Rate (23k / 8.4M = 0.28% CMR to date) and Probability of Dying:
    
     As of May 1, 23,430 people are estimated to have died out of a total population of 8,398,748 in New York City. This corresponds to a 0.28% crude mortality rate to date, or 279 deaths per 100,000 population, or 1 death every 358 people. Note that the Crude Mortality Rate will continue to increase as more infections and deaths occur
    
    
7. MORTALITY Rate by Age:
    
       When analyzing the breakdown of deaths by age and condition [source], we can observe how, out of 15,230 confirmed deaths in New York City up to May 12, only 690 (4.5% of all deaths) occurred in patients under the age of 65 who did not have an underlying medical condition (or for which it is unknown whether they had or did not have an underlying condition).

Underlying illnesses include Diabetes, Lung Disease, Cancer, Immunodeficiency, Heart Disease, Hypertension, Asthma, Kidney Disease, GI/Liver Disease, and Obesity
    
    
    
8. UNDER 65-year-old (0.09% CMR to date):
    
    
        85.9% of the population (7,214,525 people out of 8,398,748) in New York City is under 65 years old according to the US Census Bureau, which indicates the percent of persons 65 years old and over in New York City as being 14.1% [source].

We don't know what percentage of the population in this age group has an underlying condition, so at this time we are not able to accurately estimate the fatality rate for the under 65 years old and healthy.

But we can calculate it for the entire population under 65 years old (both healthy and unhealthy): with 6,188 deaths (26% of the total deaths in all age groups) occurring in this age group, of which 5,498 deaths (89%) in patients with a known underlying condition, the crude mortality rate to date will correspond to 6,188 / 7,214,525 = 0.09% CMR, or 86 deaths per 100,000 population (compared to 0.28% and 279 deaths per 100,000 for the general population).

So far there has been 1 death every 1,166 people under 65 years old (compared to 1 death every 358 people in the general population). And 89% of the times, the person who died had one or more underlying medical conditions.


    
9. Herd Immunity and final Crude Mortality Rate:
    
       Crude mortality rate is not really applicable during an ongoing epidemic.

And to reach herd immunity for COVID-19 and effectively end the epidemic, approximately two thirds (67%) of the population would need to be infected. As of May 1, New York City is at 20%, based on the antibody study findings.

Therefore, the crude mortality rate has the potential to more than triple from our current estimate, reaching close to 1,000 deaths per 100,000 population (1% CMR), and close to 300 per 100,000 (0.3% CMR) in the population under 65 years old, with 89% of these deaths (267 out of 300) occurring in people with a known underlying medical condition (including obesity).
    
 
    
10. How to calculate the mortality rate during an outbreak:
    
      
        At present, it is tempting to estimate the case fatality rate by dividing the number of known deaths by the number of confirmed cases. The resulting number, however, does not represent the true case fatality rate and might be off by orders of magnitude [...]

A precise estimate of the case fatality rate is therefore impossible at present.
2019-Novel Coronavirus (2019-nCoV): estimating the case fatality rate – a word of caution - Battegay Manue et al., Swiss Med Wkly, February 7, 2020
    
    
The case fatality rate (CFR) represents the proportion of cases who eventually die from a disease.
    
    Once an epidemic has ended, it is calculated with the formula: deaths / cases.
    
But while an epidemic is still ongoing, as it is the case with the current novel coronavirus outbreak, this formula is, at the very least, "naïve" and can be "misleading if, at the time of analysis, the outcome is unknown for a non negligible proportion of patients." [8]
    
(Methods for Estimating the Case Fatality Ratio for a Novel, Emerging Infectious Disease - Ghani et al, American Journal of Epidemiology).
    
In other words, current deaths belong to a total case figure of the past, not to the current case figure in which the outcome (recovery or death) of a proportion (the most recent cases) hasn't yet been determined.
    

The correct formula, therefore, would appear to be:
    
    CFR = deaths at day.x / cases at day.x-{T}
    (where T = average time period from case confirmation to death)
    
This would constitute a fair attempt to use values for cases and deaths belonging to the same group of patients.
    
One issue can be that of determining whether there is enough data to estimate T with any precision, but it is certainly not T = 0 (what is implicitly used when applying the formula current deaths / current cases to determine CFR during an ongoing outbreak).
    
Let's take, for example, the data at the end of February 8, 2020: 813 deaths (cumulative total) and 37,552 cases (cumulative total) worldwide.
    
If we use the formula (deaths / cases) we get:
    
    813 / 37,552 = 2.2% CFR (flawed formula).
    

With a conservative estimate of T = 7 days as the average period from case confirmation to death, we would correct the above formula by using February 1 cumulative cases, which were 14,381, in the denominator:
    
Feb. 8 deaths / Feb. 1 cases = 813 / 14,381 = 5.7% CFR (correct formula, and estimating T=7).
    
T could be estimated by simply looking at the value of (current total deaths + current total recovered) and pair it with a case total in the past that has the same value. For the above formula, the matching dates would be January 26/27, providing an estimate for T of 12 to 13 days. This method of estimating T uses the same logic of the following method, and therefore will yield the same result.
    
An alternative method, which has the advantage of not having to estimate a variable, and that is mentioned in the American Journal of Epidemiology study cited previously as a simple method that nevertheless could work reasonably well if the hazards of death and recovery at any time t measured from admission to the hospital, conditional on an event occurring at time t, are proportional, would be to use the formula:
    
    CFR = deaths / (deaths + recovered)
    
which, with the latest data available, would be equal to:
    
    652,437 / (652,437 + 10,056,340) = 6% CFR (worldwide)
    
If we now exclude cases in mainland China, using current data on deaths and recovered cases, we get:
    
647,803 / (647,803 + 9,977,422) = 6.1% CFR (outside of mainland China)
    
The sample size above is limited, and the data could be inaccurate (for example, the number of recoveries in countries outside of China could be lagging in our collection of data from numerous sources, whereas the number of cases and deaths is more readily available and therefore generally more up to par).
    
There was a discrepancy in mortality rates (with a much higher mortality rate in China) which however is not being confirmed as the sample of cases outside of China is growing in size. On the contrary, it is now higher outside of China than within.
    
That initial discrepancy was generally explained with a higher case detection rate outside of China especially with respect to Wuhan, where priority had to be initially placed on severe and critical cases, given the ongoing emergency.
    
Unreported cases would have the effect of decreasing the denominator and inflating the CFR above its real value. For example, assuming 10,000 total unreported cases in Wuhan and adding them back to the formula, we would get a CFR of 6.1% (quite different from the CFR of 6% based strictly on confirmed cases).
    
Neil Ferguson, a public health expert at Imperial College in the UK, said his “best guess” was that there were 100,000 affected by the virus even though there were only 2,000 confirmed cases at the time. [11]
    
Without going that far, the possibility of a non negligible number of unreported cases in the initial stages of the crisis should be taken into account when trying to calculate the case fatally rate.
    
As the days go by and the city organized its efforts and built the infrastructure, the ability to detect and confirm cases improved. As of February 3, for example, the novel coronavirus nucleic acid testing capability of Wuhan had increased to 4,196 samples per day from an initial 200 samples.[10]
    
A significant discrepancy in case mortality rate can also be observed when comparing mortality rates as calculated and reported by China NHC: a CFR of 3.1% in the Hubei province (where Wuhan, with the vast majority of deaths is situated), and a CFR of 0.16% in other provinces (19 times less).
    
Finally, we shall remember that while the 2003 SARS epidemic was still ongoing, the World Health Organization (WHO) reported a fatality rate of 4% (or as low as 3%), whereas the final case fatality rate ended up being 9.6%.
    '''.replace(',',"\n"))
    scrollbar.config(command=lbl3.yview)
######## SYMPTOMS WINDOW #########
def symptoms():
    root=tk.Toplevel()
    root.geometry("1300x1000")
    root.title("SYMPTOMS")
    root.config(bg="#252525")
    root.wm_iconbitmap("./icon/icn.ico")
    lbl1=tk.Label(root,text="SYPMTOMS",font="Georgia 40 bold italic",bg="#252525",fg="sky blue",width=25,bd=0)
    lbl1.pack(fill=Y)
    frame=tk.Frame(root,width=800,relief=GROOVE,bg="#252525")
    frame.config(highlightthickness=2,highlightbackground="light green",highlightcolor="light green")
    frame.pack(expand=TRUE,pady=(10,0),fill=BOTH)
    scrollbar = tk.Scrollbar(frame,relief=GROOVE,bg="#252525")
    scrollbar.config(bg="#252525")
    scrollbar.pack(side=RIGHT, fill=Y)
    lbl3 =tk.Text(frame, yscrollcommand=scrollbar.set,width=100,bg="white",fg="#252525",bd=0,font="Helvetica 16 bold italic")
    lbl3.place(x=0,y=20)
    lbl3.insert(END,'''People with COVID-19 have had a wide range of symptoms reported – ranging from mild symptoms to severe illness. These symptoms may appear 2-14 days after exposure to the virus:

   1. Fever
   2. Cough
   3. Shortness of breath or difficulty breathing
   4. Chills
   5. Repeated shaking with chills
   6. Muscle pain
   7. Headache
   8. Sore throat
   9. New loss of taste or smell
  
  
  TYPICAL SYMPTOMS:
   
     COVID-19 typically causes flu-like symptoms including a fever and cough.

In some patients - particularly the elderly and others with other chronic health conditions - these symptoms can develop into pneumonia, with chest tightness, chest pain, and shortness of breath.

It seems to start with a fever, followed by a dry cough.

After a week, it can lead to shortness of breath, with about 20% of patients requiring hospital treatment.

Notably, the COVID-19 infection rarely seems to cause a runny nose, sneezing, or sore throat (these symptoms have been observed in only about 5% of patients). Sore throat, sneezing, and stuffy nose are most often signs of a cold.  
   
   
   80% of CASES ARE MILD:
   
      Based on all 72,314 cases of COVID-19 confirmed, suspected, and asymptomatic cases in China as of February 11, a paper by the Chinese CCDC released on February 17 and published in the Chinese Journal of Epidemiology has found that:

80.9% of infections are mild (with flu-like symptoms) and can recover at home.
13.8% are severe, developing severe diseases including pneumonia and shortness of breath.
4.7% as critical and can include: respiratory failure, septic shock, and multi-organ failure.
in about 2% of reported cases the virus is fatal.
Risk of death increases the older you are.
Relatively few cases are seen among children.
   
   
   Pre-Existing Conditions:
   
      Pre-existing illnesses that put patients at higher risk:

1.cardiovascular disease
2.diabetes
3.chronic respiratory disease
4.hypertension
 
 That said, some otherwise healthy people do seem to develop a severe form of pneumonia after being infected by the virus. The reason for this is being investigated as we try to learn more about this new virus.
   
   
  Examples of possible development of symptoms (from actual cases):   
   
    A man in his 40s in Japan:

Day #1: malaise and muscle pain
later diagnosed with pneumonia
A man in his 60s in Japan:

Day #1: initial symptoms of low-grade fever and sore throat.
A man in his 40s in Japan:

Day #1: chills, sweating and malaise
Day #4: fever, muscle pain and cough
A woman in her 70s, in Japan:

Day #1: 38° fever for a few minutes
Day #2-3: went on a bus tour
Day #5: visited a medical institution
Day #6: showed symptoms of pneumonia.
A woman in her 40s, in Japan:

Day #1: low-grade fever
Day #2: 38° fever
Day #6: being treated at home.
A man in his 60s, in Japan:

Day #1: Cold
Day #6: Fever of 39° C. (102.2 F)
Day #8: Pneumonia
Another patient, in China with a history of type 2 diabetes and hypertension:

Jan. 22: Fever and cough
Feb. 5: Died
First death in the Philippines (a 44-year-old Chinese thought to have had other pre-existing health conditions):

Jan. 25: Fever, cough, and sore throat (hospitalized)
Developed severe pneumonia
Feb. 2: Died

   
  How long do symptoms last? 
   
     Using available preliminary data, the Report of the WHO-China Joint Mission published on Feb. 28 by WHO, [5] which is based on 55,924 laboratory confirmed cases, observed the following median time from symptoms onset to clinical recovery:

mild cases: approximately 2 weeks
severe or critical disease: 3 - 6 weeks
time from onset to the development of severe disease (including hypoxia): 1 week
Among patients who have died, the time from symptom onset to outcome ranges from 2 - 8 weeks.
   
   
   
  Information on Coronavirus Symptoms from Government Health Officials:
  
  
  
  Canada Public Health Agency:
  
    The Canadian PHAC section dedicated to the 2019 novel coronavirus states that:

1.You may have little to no symptoms.
2.You may not know you have symptoms of COVID-19 because they are similar to a cold or flu.
3.Symptoms may take up to 14 days to appear after exposure to the virus. This is the longest known infectious period for this virus.
  
   
  Symptoms have included:

1.fever
2.cough
3.difficulty breathing
4.pneumonia in both lungs
In severe cases, infection can lead to death.
  
  
  UK Government and NHS:

     The UK National Health Service (NHS) section dedicated to Coronavirus (2019-nCoV) lists the following as the main symptoms of coronavirus:

1.a cough
2.a high temperature
3.shortness of breath

The GOV.UK novel coronavirus guidance for the public page says:

  ...Typical symptoms of coronavirus include fever and a cough that may progress to a severe pneumonia causing shortness of breath and breathing difficulties.
   

The GOV.UK clinical guidance on Novel coronavirus (2019-nCoV): epidemiology, virology and clinical features notes that:

  1.Fever, cough or chest tightness, and dyspnoea are the main symptoms reported. While most cases report a mild illness, severe are also being reported, some of whom require intensive care.
  
  
  
  Australian Government: 
   
    The Australian Government Department of Health informs that symptoms can range from mild illness to pneumonia, adding that some people will recover easily, while others may get very sick very quickly. According to their list of novel coronavirus symptoms, people may experience:

1.fever
2.flu-like symptoms such as coughing, sore throat and fatigue
3.shortness of breath
   
   
  
  World Health Organization :
   
      The WHO has issued an interim guidance on the clinical management of suspected cases in which it says that

1. "nCoV may present with mild, moderate, or severe illness; the latter includes severe pneumonia, ARDS, sepsis and septic shock."
   '''.replace(',',"\n"))
    scrollbar.config(command=lbl3.yview)
######### PREVENTION WINDOW ##########
def prevention():
    root=tk.Toplevel()
    root.geometry("1300x1000")
    root.title("PREVENTION")
    root.config(bg="#252525")
    root.wm_iconbitmap("./icon/icn.ico")
    lbl1=tk.Label(root,text="PREVENTION",font="Georgia 40 bold italic",bg="#252525",fg="sky blue",width=25,bd=0)
    lbl1.pack(fill=Y)
    frame=tk.Frame(root,width=800,relief=GROOVE,bg="#252525")
    frame.config(highlightthickness=2,highlightbackground="light green",highlightcolor="light green")
    frame.pack(expand=TRUE,pady=(10,0),fill=BOTH)
    scrollbar = tk.Scrollbar(frame,relief=GROOVE,bg="#252525")
    scrollbar.config(bg="#252525")
    scrollbar.pack(side=RIGHT, fill=Y)
    lbl3 =tk.Text(frame, yscrollcommand=scrollbar.set,width=100,bg="white",fg="#252525",bd=0,font="Helvetica 16 bold italic")
    lbl3.place(x=0,y=20)
    lbl3.insert(END,'''
    Know how it spreads:

1.There is currently no vaccine to prevent coronavirus disease 2019 (COVID-19).
2.The best way to prevent illness is to avoid being exposed to this virus.
3.The virus is thought to spread mainly from person-to-person.
   i. Between people who are in close contact with one another (within about 6 feet).
   ii. Through respiratory droplets produced when an infected person coughs, sneezes or talks.
   iii. These droplets can land in the mouths or noses of people who are nearby or possibly be inhaled into the lungs.
   iv. Some recent studies have suggested that COVID-19 may be spread by people who are not showing symptoms.
   
   
   Everyone Should:
    
     Wash your hands often
       
       1. Wash your hands often with soap and water for at least 20 seconds especially after you have been in a public place, or after blowing your nose, coughing, or sneezing.
       2. It’s especially important to wash:
             i.  Before eating or preparing food
             ii. Before touching your face
             iii. After using the restroom
             iv.  After leaving a public place
             v.   After blowing your nose, coughing, or sneezing
             vi.   After handling your cloth face covering
             vii.   After changing a diaper
             viii.   After caring for someone sick
             ix.   After touching animals or pets
       3.  If soap and water are not readily available, use a hand sanitizer that contains at least 60% alcohol. Cover all surfaces of your hands and rub them together until they feel dry.
       4.  Avoid touching your eyes, nose, and mouth with unwashed hands  
   
   Avoid close contact:
   
     1. Inside your home: Avoid close contact with people who are sick.
        i. If possible, maintain 6 feet between the person who is sick and other household members.
  
     2.Outside your home: Put 6 feet of distance between yourself and people who don’t live in your household.
        i.Remember that some people without symptoms may be able to spread virus.
        ii.  Stay at least 6 feet (about 2 arms’ length) from other people.
        iii.   Keeping distance from others is especially important for people who are at higher risk of getting very sick.
   
   
 
Cover your mouth and nose with a cloth face cover when around others:  
   
  1. You could spread COVID-19 to others even if you do not feel sick.
  2. The cloth face cover is meant to protect other people in case you are infected.
  3. Everyone should wear a cloth face cover in public settings and when around people who don’t live in your household, especially when other social distancing measures are difficult to maintain.
       i. Cloth face coverings should not be placed on young children under age 2, anyone who has trouble breathing, or is unconscious, incapacitated or otherwise unable to remove the mask without assistance.
  
  4. Do NOT use a facemask meant for a healthcare worker. Currently, surgical masks and N95 respirators are critical supplies that should be reserved for healthcare workers and other first responders.
  5. Continue to keep about 6 feet between yourself and others. The cloth face cover is not a substitute for social distancing.
   
   
   
Cover coughs and sneezes:   
   
   1. Always cover your mouth and nose with a tissue when you cough or sneeze or use the inside of your elbow and do not spit.
   2. Throw used tissues in the trash.
   3. Immediately wash your hands with soap and water for at least 20 seconds. If soap and water are not readily available, clean your hands with a hand sanitizer that contains at least 60% alcohol.
   
   
 
 
Clean and disinfect:
   
   1.Clean AND disinfect frequently touched surfaces daily. This includes tables, doorknobs, light switches, countertops, handles, desks, phones, keyboards, toilets, faucets, and sinks.
   2.If surfaces are dirty, clean them. Use detergent or soap and water prior to disinfection.
   3.Then, use a household disinfectant. Most common EPA-registered household disinfectantsexternal icon will work.  
   
   
 
Monitor Your Health Daily:   
   
  1. Be alert for symptoms. Watch for fever, cough, shortness of breath, or other symptoms of COVID-19.
      i. Especially important if you are running essential errands, going into the office or workplace, and in settings where it may be difficult to keep a physical distance of 6 feet.
  2. Take your temperature if symptoms develop.
      i. Don’t take your temperature within 30 minutes of exercising or after taking medications that could lower your temperature, like acetaminophen.
  3. Follow CDC guidance if symptoms develop.   
      '''.replace(',',"\n"))
    scrollbar.config(command=lbl3.yview)
######### TEST PROCESS WINDOW ################
global loginimage
def testprocess():
    global loginimage
    root=tk.Toplevel()
    root.geometry("480x640")
    root.resizable(FALSE,FALSE)
    root.title("Login")
    root.wm_iconbitmap("./icon/icn.ico")
    loginimage=ImageTk.PhotoImage(Image.open("./chatbot_login/login.jpg"))
    loginlabl=tk.Label(root,image=loginimage,width=480,height=640)
    loginlabl.place(x=0,y=0)
    pl=tk.Label(root, text="PLEASE LOGIN TO CONTINUE", justify=CENTER, font="Georgia 20 bold italic",bg="RosyBrown",
             fg="Lime",bd=0)
    pl.pack(fill=Y,pady=(20,0))
    name_labl=tk.Label(root, text="NAME: ", font="times 18 bold italic",bg="RosyBrown",fg="#252525",bd=0)
    name_labl.place(x=40,y=160)
    entryName=tk.Entry(root, font="times 15 bold italic",width=24)
    entryName.place(x=180,y=160)
    entryName.focus()
    labelAge=tk.Label(root, text="AGE: ", font="times 18 bold italic",bg="RosyBrown",fg="#252525",bd=0)
    labelAge.place(x=40,y=240)
    entryAge=tk.Entry(root, font="times 15 bold italic",width=24)
    entryAge.bind("<Return>", lambda a:goAhead(entryName.get(), entryAge.get()))
    entryName.focus()
    entryAge.place(x=180,y=240)
    def goenter(e):
        go['bg']="light green"
        go.config(bg="light green",fg="#252525")
        go['fg']="#252525"
    def goleave(f):
        go['bg']="orange"
        go.config(bg="orange",fg="#252525")
    go=tk.Button(root, text="CONTINUE", font="Georgia 15 bold italic", command=lambda: goAhead(entryName.get(), entryAge.get()),
              bg="orange",fg="#252525",activeforeground="#252525",activebackground="light green")
    go.place(x=180,y=350)
    go.bind("<Enter>",goenter)
    go.bind("<Leave>",goleave)
    def goAhead(name,age):
        if age.isdecimal()==False:
            messagebox.showerror("Error","Enter valid age")
        else:
            cons=Consult(name,age)
            root.destroy()
def Consult(name,age):
    name=name
    age=int(age)
    consultWindow=Tk()
    consultWindow.title("Your Digital Helper")
    consultWindow.resizable(width=False, height=False)
    consultWindow.configure(width=900, height=750, bg="#17202A")
    labelHead=Label(consultWindow, bg="#17202A", fg="#EAECEE", text="DR FLOYD", font="Georgia 18 bold", pady=5)
    labelHead.place(relwidth=1)
    line=Label(consultWindow,width=450, bg="#ABB2B9")
    line.place(relwidth=1, rely=0.07, relheight=0.012)
    textCons=Text(consultWindow, width=60, height=2,bg="#17202A", fg="#EAECEE", font="Georgia 14", padx=5, pady=5)
    textCons.place(relheight=0.745, relwidth=1, rely=0.08)
    labelBottom=Label(consultWindow, bg="#ABB2B9", height=80)
    labelBottom.place(relwidth=1, rely=0.825)
    entryMsg=Entry(labelBottom,bg="#2C3E50", fg="#EAECEE", font="Georgia 13")
    entryMsg.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
    entryMsg.bind("<Return>", lambda a:send(entryMsg.get()))
    entryMsg.focus()
    buttonMsg=Button(labelBottom, text="Send", font="Georgia 12 bold", width=20, bg="#ABB2B9", command= lambda:send(entryMsg.get()))
    buttonMsg.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
    greet=["Hi, "+name+" I am your digital helper, Floyd.", "Hello! I'm here to help you, "+name+"! I'm Floyd.", "Hey, "+name+"! This is Floyd, your digital helper!" ]
    greet2=random.choice(greet)
    textCons.insert(END, random.choice(greet)+"\n", 'bot')
    textCons.tag_configure('bot', relief='raised', wrap=WORD, lmargin1=30, rmargin=150, foreground='#C7DCF0')
    textCons.config(cursor="arrow")
    scrollbar = Scrollbar(textCons)
    scrollbar.place(relheight=1, relx=0.968)
    scrollbar.config(command = textCons.yview)
    speak(greet2)
    def send(message):
        textCons.config(state=NORMAL)
        textCons.tag_configure('user', relief='raised', wrap=WORD, lmargin1=100, rmargin=50, justify=RIGHT, foreground="#ECDCC7")
        message=message.lower()
        entryMsg.delete(0, END)
        if message=="hello" or message=="hi" or message =="hey":
                    textCons.insert(END, message+"\n", 'user')
                    textCons.insert(END, "How are you?\n", 'bot')
                    speak("How are you?")
        elif message =="not well" or message == "ill" or message == "not fine" or message == "bad" or message == "sick" or message =="tired":
                    textCons.insert(END, message+"\n", 'user')
                    textCons.insert(END, "Uh oh! Let's see!\n", 'bot')
                    textCons.insert(END, "Where would you like to begin?\n", 'bot')
                    speak("Uh oh! Let's see! Where would you like to begin?")
                    options()
        elif message =="well" or message == "fine" or message == "i'm fine" or message == "good" or message == "awesome" or message =="great":
                    textCons.insert(END, message+"\n", 'user')
                    textCons.insert(END, "Wonderful!\n", 'bot')
                    textCons.insert(END, "Where would you like to begin?\n", 'bot')
                    speak("Wonderful! Where would you like to begin?")
                    options()
        else:
            textCons.insert(END, "\n"+message+"\n", 'user')
            sorry=["Sorry, what?", "Please try again!", "I'm sorry, I couldn't catch"]
            sorry2=random.choice(sorry)
            textCons.insert(END, "\n"+sorry2+"\n", 'bot')
            speak(random.choice(sorry))
            textCons.config(state=DISABLED)
            textCons.yview(END)
    def options():
        textCons.config(state=NORMAL)
        buttonKnow=Button(textCons, text="Learn about Coronavirus", font="Georgia 8 bold", command=whatscorona)
        buttonKnow.bind("<Button-1>", lambda a:textCons.insert(INSERT, "\nLearn about Coronavirus\n", 'user'))
        buttonKnow.place(relx=0.3, rely=0.55, width=180, height=40)
        buttonTest=Button(textCons, text="Test for symptoms", font="Georgia 8 bold", command=confirm)
        buttonTest.bind("<Button-1>", lambda a:textCons.insert(INSERT, "\nTest me for symptoms\n", 'user'))
        buttonTest.place(relx=0.3, rely=0.7, width=180, height=40)
        textCons.config(state=DISABLED)
        textCons.yview(END)
    def whatscorona():
            textCons.config(state=NORMAL)
            coronaDef="\nCoronaviruses are a large family of viruses which may cause illness in animals or humans.  In humans, several coronaviruses are known to cause respiratory infections ranging from the common cold to more severe diseases such as Middle East Respiratory Syndrome (MERS) and Severe Acute Respiratory Syndrome (SARS). The most recently discovered coronavirus causes coronavirus disease COVID-19.\n"
            textCons.insert(END, "\n"+coronaDef+"\n", 'bot')
            sleep(0.2)
            t1=Thread(target=speak, args=(coronaDef, ))
            t1.start()
            sleep(0.2)
            buttonTest2 = Button(textCons, text="Test for symptoms", font="Georgia 8 bold", width=20, height=2, command=confirm)
            buttonTest2.bind("<Button-1>", lambda a: textCons.insert(INSERT, "\nTest me for symptoms\n", 'user'))
            textCons.window_create(INSERT, window=buttonTest2, padx=170)
            textCons.see(END)
            textCons.config(state=DISABLED)
    def confirm():
            textCons.config(state=NORMAL)
            textCons.insert(INSERT, "\n\nI will ask you certain questions to evaluate your medical needs\n\n", 'bot')
            textCons.insert(INSERT, "\nShall we begin?\n\n")
            speak("I will ask you certain questions to evaluate your medical needs. Shall we begin?")
            buttonYes = Button(textCons, text="YES", font="Georgia 8 bold", width=20, height=2, command=questions)
            buttonYes.bind("<Button-1>", lambda a: textCons.insert(INSERT, "\nYes\n", 'user'))
            textCons.window_create(INSERT, window=buttonYes, padx=170)
            buttonNo = Button(textCons, text="EXIT", font="Georgia 8 bold", width=20, height=2, command=textCons.quit)
            buttonNo.bind("<Button-1>", lambda a: textCons.insert(INSERT, "\nNo\n", 'user'))
            textCons.window_create(INSERT, window=buttonNo, padx=170)
            textCons.see(END)
            textCons.config(state=DISABLED)
            textCons.config(state=NORMAL)
    def questions():
              c=0
              cough=messagebox.askquestion("", "Do you have cough?")
              if cough=="yes":
                c+=1
                sleep(0.2)
                cold=messagebox.askquestion("", "Do you have cold?")
                if cold=="yes":
                    c+=1
                sleep(0.2)
                diarrhea=messagebox.askquestion("", "Are you having Diarrhea?")
                if diarrhea=="yes":
                    c+=1
                sleep(0.2)
                sorethroat=messagebox.askquestion("", "Are you having a sore throat?")
                if sorethroat=="yes":
                    c+=1
                sleep(0.2)
                myalgia=messagebox.askquestion("", "Are you experiencing MYALGIA or body ache?")
                if myalgia=="yes":
                    c+=1
                sleep(0.2)
                headache=messagebox.askquestion("", "Do you have a headache?")
                if headache=="yes":
                    c+=1
                sleep(0.2)
                fever=messagebox.askquestion("", "Do you have fever? (Temperature 37.8 C and above)")
                if fever=="yes":
                    c+=1
                sleep(0.2)
                diffBreathe=messagebox.askquestion("", "Are you having difficulty in breathing?")
                if diffBreathe=="yes":
                    c+=2
                sleep(0.2)
                fatigue=messagebox.askquestion("", "Are you experiencing fatigue?")
                if fatigue=="yes":
                    c+=2
                sleep(0.2)
                travelled=messagebox.askquestion("", "Have you travelled in the last 14 days?")
                if travelled=="yes":
                    c+=3
                sleep(0.2)
                infectedArea=messagebox.askquestion("", "Do you have travel history to a COVID-19 infected area?")
                if infectedArea=="yes":
                    c+=3
                sleep(0.2)
                contact=messagebox.askquestion("", "Are you taking care of a COVID-19 patient or are in direct contact with them?")
                if contact=="yes":
                    c+=3
                textCons.config(state=NORMAL)
                if 0<=c<=2:
                    if 0<=age<=7 or age>41:
                        evalualtion11="\nWell "+name+", nothing too serious as of now, but considering your age group, you need to take extra care and precautions\n"
                        textCons.insert(INSERT, evalualtion11, 'bot')
                        t11=Thread(target=speak, args=(evalualtion11, ))
                        t11.start()
                    elif 8<=age<=41:
                        evalualtion12="\n"+name+", nothing too serious as of now also considering the age group you fall in. However, you should still observe and take precautions\n"
                        textCons.insert(INSERT, evalualtion12, 'bot')
                        t12=Thread(target=speak, args=(evalualtion12, ))
                        t12.start()

                elif 3<=c<=5:
                    if 0<=age<=7 or age>41:
                        evalualtion21="\n"+name+", you need to keep yourself hydrated and maintain personal hygiene. Take extra precautions because the immune system of the age group you fall in is a bit weaker. Observe yourself and re-evaluate in 2 days.\n"
                        textCons.insert(INSERT, evalualtion21, 'bot')
                        t21=Thread(target=speak, args=(evalualtion21, ))
                        t21.start()
                    elif 8<=age<=41:
                        evalualtion22="\nOkay "+name+", you need to keep yourself hydrated and maintain personal hygiene. Observe yourself and re-evaluate in 2 days.\n"
                        textCons.insert(INSERT, evalualtion22, 'bot')
                        t22=Thread(target=speak, args=(evalualtion22, ))
                        t22.start()

                elif 6<=c<=12:
                    if 0<=age<=7 or age>41:
                        evalualtion31="\nHmm! "+name+", considering your age group and hence the immunity, this is not ignorable, you need to consult a doctor as soon as possible\n"
                        textCons.insert(INSERT,evalualtion31 , 'bot')
                        t31=Thread(target=speak, args=(evalualtion31, ))
                        t31.start()
                    elif 8<=age<=41:
                        evalualtion32="\nHmm! "+name+", this is not ignorable! You should seek a consultation with a doctor.\n"
                        textCons.insert(INSERT, evalualtion32, 'bot')
                        t32=Thread(target=speak, args=(evalualtion32, ))
                        t32.start()

                elif 12<=c<=24:
                    evalualtion4="\nIt's serious. Seek medical help immediately, "+name+"!\n"
                    textCons.insert(INSERT, evalualtion4 , 'bot')
                    t32=Thread(target=speak, args=(evalualtion4, ))
                    t32.start()
                textCons.see(END)
                textCons.config(state=DISABLED)
def speak(reply):
    engine.say(reply)
    engine.runAndWait()
###### QUIT ########
def Quit():
    root.destroy()
########## FOR FULL SCREEN ########
def large(event):
    root.attributes("-fullscreen",True)
def small(event):
    root.attributes("-fullscreen",False)

########## MAIN WINDOW #########

root=Tk()
root.geometry("1500x1000")
root.config(bg="#252525")
root.title("COVID-19")
root.wm_iconbitmap("./icon/icn.ico")
root.bind("<F1>",large)
root.bind("<Escape>",small)

y=1
global lbl
global lblimg
def color():
    global y
    if y==10:
        y=1
    if y==1:
      lbl.config(fg="#667eea")
    elif y==2:
      lbl.config(fg="#66a6ff")
    elif y==3:
      lbl.config(fg="#ff758c")
    elif y==4:
       lbl.config(fg="#fcb045")
    elif y==5:
       lbl.config(fg="#8e0e00")
    elif y==6:
       lbl.config(fg="#ff00cc")
    elif y==7:
       lbl.config(fg="#ff6a00")
    elif y==8:
       lbl.config(fg="#dce35b")
    elif y==9:
       lbl.config(fg="#f80759")
    y+=1
    lbl.after(2000, color)
lbl=Label(root,text="COVID-19 DATA ANALYSIS",font="Georgia 25 bold",bg="#252525",fg="white",width=25)
lbl.pack(fill=Y,pady=(10,0))
lblimg=ImageTk.PhotoImage(Image.open("./logo/logo2.png"))
covidlbl=Label(root,image=lblimg,width=60,height=50)
covidlbl.place(x=930,y=0)
color()
######## FRAME 1 ###########
frame=Frame(root,relief=SOLID,highlightthickness=2,bd=0)
frame.config(highlightbackground="light green",highlightcolor="light green",bg="#252525")
frame.pack(fill=BOTH,expand=TRUE)

x=1
def move():
    global x
    if x==10:
        x=1
    if x==1:
      labl.config(image=image1)
    elif x==2:
      labl.config(image=image2)
    elif x==3:
      labl.config(image=image3)
    elif x==4:
       labl.config(image=image4)
    elif x==5:
       labl.config(image=image5)
    elif x==6:
       labl.config(image=image6)
    elif x==7:
       labl.config(image=image7)
    elif x==8:
       labl.config(image=image8)
    elif x==9:
       labl.config(image=image9)
    x+=1
    labl.after(2000,move)
########## FRAME 3 ############3
frame3=Frame(frame,relief=SOLID)
frame3.pack(side=RIGHT)
image1=ImageTk.PhotoImage(Image.open("./images/img2.jpg"))
image2=ImageTk.PhotoImage(Image.open("./images/img3.jpg"))
image3=ImageTk.PhotoImage(Image.open("./images/img4.jpg"))
image4=ImageTk.PhotoImage(Image.open("./images/img5.jpg"))
image5=ImageTk.PhotoImage(Image.open("./images/img6.jpg"))
image6=ImageTk.PhotoImage(Image.open("./images/img7.png"))
image7=ImageTk.PhotoImage(Image.open("./images/img8.jpg"))
image8=ImageTk.PhotoImage(Image.open("./images/img9.png"))
image9=ImageTk.PhotoImage(Image.open("./images/img10.jpg"))

labl=Label(frame3,width=1100,height=650)
labl.pack(side=RIGHT,fill=Y)
move()
############# HOVER EFFECTS AND BUTTON DASHBOARD ##################
def button1(e):
        btn1['bg']="light green"
        btn1.config(bg="light green",fg="#252525",text=" overview")
        frame4.pack(side=TOP,padx=(8,8),pady=(13,0))

def leavebtn(f):
        btn1['bg']="#252525"
        btn1['fg']="white"
        btn1.config(bg="#252525",fg="white",text="OVERVIEW")
        frame4.pack(side=TOP,padx=(2,0),pady=(17,0))
def button2(e):
            btn2['bg']="light green"
            btn2.config(bg="light green",fg="#252525",text=" active cases")
            frame5.pack(side=TOP,padx=(8,8),pady=(13,0))
def leavebtn2(f):
            btn2['bg']="#252525"
            btn2['fg']="white"
            btn2.config(bg="#252525",fg="white",text="ACTIVE CASES")
            frame5.pack(side=TOP,padx=(2,0),pady=(17,0))
def button3(e):
            btn3['bg']="light green"
            btn3.config(bg="light green",fg="#252525",text=" closed cases")
            frame6.pack(side=TOP,padx=(8,8),pady=(13,0))
def leavebtn3(f):
            btn3['bg']="#252525"
            btn3['fg']="white"
            btn3.config(bg="#252525",fg="white",text="CLOSED CASES")
            frame6.pack(side=TOP,padx=(2,0),pady=(17,0))
def button4(e):
            btn9['bg']="light green"
            btn9.config(bg="light green",fg="#252525",text=" countries")
            frame7.pack(side=TOP,padx=(8,8),pady=(13,0))
def leavebtn4(f):
            btn9['bg']="#252525"
            btn9['fg']="white"
            btn9.config(bg="#252525",fg="white",text="COUNTRIES")
            frame7.pack(side=TOP,padx=(2,0),pady=(17,0))
def button5(e):
            btn10['bg']="light green"
            btn10.config(bg="light green",fg="#252525",text=" quit")
            frame13.pack(side=TOP,padx=(8,8),pady=(13,0))
def leavebtn5(f):
            btn10['bg']="#252525"
            btn10['fg']="white"
            btn10.config(bg="#252525",fg="white",text="QUIT")
            frame13.pack(side=TOP,padx=(2,0),pady=(17,0))
def button6(e):
            wrldbtn8['bg']="light green"
            wrldbtn8.config(bg="light green",fg="#252525",text=" world & graph")
            frame8.pack(side=TOP,padx=(8,8),pady=(13,0))
def leavebtn6(f):
            wrldbtn8['bg']="#252525"
            wrldbtn8['fg']="white"
            wrldbtn8.config(bg="#252525",fg="white",text="WORLD & GRAPH")
            frame8.pack(side=TOP,padx=(2,0),pady=(17,0))
def button7(e):
            btn11['bg']="light green"
            btn11.config(bg="light green",fg="#252525",text=" death rate")
            frame9.pack(side=TOP,padx=(8,8),pady=(13,0))
def leavebtn7(f):
            btn11['bg']="#252525"
            btn11['fg']="white"
            btn11.config(bg="#252525",fg="white",text="DEATH RATE")
            frame9.pack(side=TOP,padx=(2,0),pady=(17,0))
def button8(e):
            btn12['bg']="light green"
            btn12.config(bg="light green",fg="#252525",text=" symptoms")
            frame10.pack(side=TOP,padx=(8,8),pady=(13,0))
def leavebtn8(f):
            btn12['bg']="#252525"
            btn12['fg']="white"
            btn12.config(bg="#252525",fg="white",text="SYMPTOMS")
            frame10.pack(side=TOP,padx=(2,0),pady=(17,0))
def button9(e):
            btn13['bg']="light green"
            btn13.config(bg="light green",fg="#252525",text=" prevention")
            frame11.pack(side=TOP,padx=(8,8),pady=(13,0))
def leavebtn9(f):
            btn13['bg']="#252525"
            btn13['fg']="white"
            btn13.config(bg="#252525",fg="white",text="PREVENTION")
            frame11.pack(side=TOP,padx=(2,0),pady=(17,0))
def button10(e):
            btn14['bg']="light green"
            btn14.config(bg="light green",fg="#252525",text=" test process")
            frame12.pack(side=TOP,padx=(8,8),pady=(13,0))
def leavebtn10(f):
            btn14['bg']="#252525"
            btn14['fg']="white"
            btn14.config(bg="#252525",fg="white",text="TEST PROCESS")
            frame12.pack(side=TOP,padx=(2,0),pady=(17,0))

frame2=Frame(frame,highlightthickness=2,bd=1,width=442,height=640,relief=GROOVE)
frame2.config(highlightbackground="light green",highlightcolor="light green",bg="#252525")
frame2.pack(side=LEFT,fill=Y,expand=True)
frameimg=ImageTk.PhotoImage(Image.open("./dashboard img/dashboard.jpg"))
lblimg1=Label(frame2,image=frameimg,width=442,height=640)
lblimg1.place(x=0,y=1)
frame4=Frame(frame2,highlightthickness=2,bd=0,width=20,relief=SOLID)
frame4.config(highlightbackground="light green",highlightcolor="light green",bg="light green")
frame4.pack(side=TOP,padx=(2,0),pady=(17,0))
btn1=Button(frame4,text="OVERVIEW",highlightthickness=2,width=20)
btn1.config(activebackground="light green",activeforeground="white",font="Consolas 18 bold italic",bg="#252525",fg="white",bd=1,command=overview)
btn1.pack()
btn1.bind("<Enter>",button1)
btn1.bind("<Leave>",leavebtn)
icnlblimg=ImageTk.PhotoImage(Image.open("./icon/world-icon (1).png"))
icnlbl=Label(btn1,image=icnlblimg,bd=0)
icnlbl.place(x=33,y=5)
frame5=Frame(frame2,highlightthickness=2,bd=0,width=20,relief=SOLID)
frame5.config(highlightbackground="light green",highlightcolor="light green",bg="#252525")
frame5.pack(side=TOP,padx=(2,0),pady=(17,0))
btn2=Button(frame5,text="ACTIVE CASES",highlightthickness=2,width=20)
btn2.config(activebackground="light green",activeforeground="white",font="Consolas 18 bold italic",bg="#252525",fg="white",bd=1,command=Cases)
btn2.pack()
btn2.bind("<Enter>",button2)
btn2.bind("<Leave>",leavebtn2)
icnlblimg1=ImageTk.PhotoImage(Image.open("./icon/case-icon.png"))
icnlbl1=Label(btn2,image=icnlblimg1,bd=0)
icnlbl1.place(x=8,y=5)
frame6=Frame(frame2,highlightthickness=2,bd=0,width=20,relief=SOLID)
frame6.config(highlightbackground="light green",highlightcolor="light green",bg="#252525")
frame6.pack(side=TOP,padx=(2,0),pady=(17,0))
btn3=Button(frame6,text="CLOSED CASES",highlightthickness=2,width=20,command=deaths)
btn3.config(activebackground="light green",activeforeground="white",font="Consolas 18 bold italic",bg="#252525",fg="white",bd=1)
btn3.pack()
btn3.bind("<Enter>",button3)
btn3.bind("<Leave>",leavebtn3)
icnlblimg2=ImageTk.PhotoImage(Image.open("./icon/Close-2-icon.png"))
icnlbl2=Label(btn3,image=icnlblimg2,bd=0)
icnlbl2.place(x=8,y=5)
frame7=Frame(frame2,highlightthickness=2,bd=0,width=20,relief=SOLID)
frame7.config(highlightbackground="light green",highlightcolor="light green",bg="#252525")
frame7.pack(side=TOP,padx=(2,0),pady=(17,0))
btn9=Button(frame7,text="COUNTRIES",highlightthickness=2,width=20,command=countries_affected)
btn9.config(activebackground="light green",activeforeground="white",font="Consolas 18 bold italic",bg="#252525",fg="white",bd=1)
btn9.pack()
btn9.bind("<Enter>",button4)
btn9.bind("<Leave>",leavebtn4)
icnlblimg3=ImageTk.PhotoImage(Image.open("./icon/Country-icon.png"))
icnlbl3=Label(btn9,image=icnlblimg3,bd=0)
icnlbl3.place(x=19,y=5)

frame8=Frame(frame2,highlightthickness=2,bd=0,width=20,relief=SOLID)
frame8.config(highlightbackground="light green",highlightcolor="light green",bg="#252525")
frame8.pack(side=TOP,padx=(2,0),pady=(17,0))
wrldbtn8=Button(frame8,text="WORLD & GRAPH",highlightthickness=2,width=20,command=world)
wrldbtn8.config(activebackground="light green",activeforeground="white",font="Consolas 18 bold italic",bg="#252525",fg="white",bd=1)
wrldbtn8.pack()
wrldbtn8.bind("<Enter>",button6)
wrldbtn8.bind("<Leave>",leavebtn6)
icnlblimg4=ImageTk.PhotoImage(Image.open("./icon/Color-MS-Excel-icon.png"))
icnlbl4=Label(wrldbtn8,image=icnlblimg4,bd=0)
icnlbl4.place(x=0,y=5)

frame9=Frame(frame2,highlightthickness=2,bd=0,width=20,relief=SOLID)
frame9.config(highlightbackground="light green",highlightcolor="light green",bg="#252525")
frame9.pack(side=TOP,padx=(2,0),pady=(17,0))
btn11=Button(frame9,text="DEATH RATE",highlightthickness=2,width=20,command=death_rate)
btn11.config(activebackground="light green",activeforeground="white",font="Consolas 18 bold italic",bg="#252525",fg="white",bd=1)
btn11.pack()
btn11.bind("<Enter>",button7)
btn11.bind("<Leave>",leavebtn7)
icnlblimg5=ImageTk.PhotoImage(Image.open("./icon/Skull-and-bones-icon.png"))
icnlbl5=Label(btn11,image=icnlblimg5,bd=0)
icnlbl5.place(x=20,y=5)
frame10=Frame(frame2,highlightthickness=2,bd=0,width=20,relief=SOLID)
frame10.config(highlightbackground="light green",highlightcolor="light green",bg="#252525")
frame10.pack(side=TOP,padx=(2,0),pady=(17,0))
btn12=Button(frame10,text="SYMPTOMS",highlightthickness=2,width=20,command=symptoms)
btn12.config(activebackground="light green",activeforeground="white",font="Consolas 18 bold italic",bg="#252525",fg="white",bd=1)
btn12.pack()
btn12.bind("<Enter>",button8)
btn12.bind("<Leave>",leavebtn8)
icnlblimg6=ImageTk.PhotoImage(Image.open("./icon/uxwing-svg-icon-editor (1).png"))
icnlbl6=Label(btn12,image=icnlblimg6,bd=0)
icnlbl6.place(x=25,y=5)
frame11=Frame(frame2,highlightthickness=2,bd=0,width=20,relief=SOLID)
frame11.config(highlightbackground="light green",highlightcolor="light green",bg="#252525")
frame11.pack(side=TOP,padx=(2,0),pady=(17,0))
btn13=Button(frame11,text="PREVENTION",highlightthickness=2,width=20,command=prevention)
btn13.config(activebackground="light green",activeforeground="white",font="Consolas 18 bold italic",bg="#252525",fg="white",bd=1)
btn13.pack()
btn13.bind("<Enter>",button9)
btn13.bind("<Leave>",leavebtn9)
icnlblimg7=ImageTk.PhotoImage(Image.open("./icon/uxwing-svg-icon-editor (3).png"))
icnlbl7=Label(btn13,image=icnlblimg7,bd=0)
icnlbl7.place(x=18,y=5)
frame12=Frame(frame2,highlightthickness=2,bd=0,width=20,relief=SOLID)
frame12.config(highlightbackground="light green",highlightcolor="light green",bg="#252525")
frame12.pack(side=TOP,padx=(2,0),pady=(17,0))
btn14=Button(frame12,text="TEST PROCESS",highlightthickness=2,width=20,command=testprocess)
btn14.config(activebackground="light green",activeforeground="white",font="Consolas 18 bold italic",bg="#252525",fg="white",bd=1)
btn14.pack()
btn14.bind("<Enter>",button10)
btn14.bind("<Leave>",leavebtn10)
icnlblimg8=ImageTk.PhotoImage(Image.open("./icon/test process.png"))
icnlbl8=Label(btn14,image=icnlblimg8,bd=0)
icnlbl8.place(x=5,y=5)
frame13=Frame(frame2,highlightthickness=2,bd=0,width=20,relief=SOLID)
frame13.config(highlightbackground="light green",highlightcolor="light green",bg="#252525")
frame13.pack(side=TOP,padx=(2,0),pady=(17,0))
btn10=Button(frame13,text="QUIT",highlightthickness=2,width=20,command=Quit)
btn10.config(activebackground="light green",activeforeground="white",font="Consolas 18 bold italic",bg="#252525",fg="white",bd=1)
btn10.pack()
btn10.bind("<Enter>",button5)
btn10.bind("<Leave>",leavebtn5)
icnlblimg9=ImageTk.PhotoImage(Image.open("./icon/quit.png"))
icnlbl9=Label(btn10,image=icnlblimg9,bd=0)
icnlbl9.place(x=50,y=5)

####################### DARK MODE AND LIGHT MODE #######################
def button():
        root.config(bg="#ffffff")
        frame.config(bg="#ffffff")
        frame.config(highlightbackground="red",highlightcolor="red",bg="#ffffff")
        frame2.config(bg="#ffffff")
        frame2.config(highlightbackground="red",highlightcolor="red",bg="#ffffff")
        frame3.config(bg="#ffffff")
        frame4.config(highlightbackground="red",highlightcolor="red",bg="red")
        frame5.config(highlightbackground="red",highlightcolor="red",bg="red")
        frame6.config(highlightbackground="red",highlightcolor="red",bg="red")
        frame7.config(highlightbackground="red",highlightcolor="red",bg="red")
        frame8.config(highlightbackground="red",highlightcolor="red",bg="red")
        frame9.config(highlightbackground="red",highlightcolor="red",bg="red")
        frame10.config(highlightbackground="red",highlightcolor="red",bg="red")
        frame11.config(highlightbackground="red",highlightcolor="red",bg="red")
        frame12.config(highlightbackground="red",highlightcolor="red",bg="red")
        frame13.config(highlightbackground="red",highlightcolor="red",bg="red")
        lbl.config(bg="#ffffff")
        btn1.config(bg="#ffffff",fg="#252525",bd=1)
        btn2.config(bg="#ffffff",fg="#252525",bd=1)
        btn3.config(bg="#ffffff",fg="#252525",bd=1)
        btn9.config(bg="#ffffff",fg="#252525",bd=1)
        wrldbtn8.config(bg="#ffffff",fg="#252525",bd=1)
        btn11.config(bg="#ffffff",fg="#252525",bd=1)
        btn12.config(bg="#ffffff",fg="#252525",bd=1)
        btn13.config(bg="#ffffff",fg="#252525",bd=1)
        btn14.config(bg="#ffffff",fg="#252525",bd=1)
        btn10.config(bg="#ffffff",fg="#252525",bd=1)
def btnmve(e):
    button1.place(x=20,y=1)
def btnleve(f):
    button1.place(x=30,y=0)
daymde=ImageTk.PhotoImage(Image.open("./images/dark.jpg"))
button1=Button(root,text="LIGHT MODE",image=daymde,font="times 15 bold italic",command=button)
button1.place(x=30,y=0)
button1.bind("<Enter>",btnmve)
button1.bind("<Leave>",btnleve)
def button3():
        root.config(bg="#252525")
        frame.config(bg="#252525",)
        frame.config(highlightbackground="light green",highlightcolor="light green",bg="#252525")
        frame2.config(bg="#252525")
        frame2.config(highlightbackground="light green",highlightcolor="light green",bg="#252525")
        frame3.config(bg="#252525")
        frame4.config(highlightbackground="light green",highlightcolor="light green",bg="light green")
        frame5.config(highlightbackground="light green",highlightcolor="light green",bg="light green")
        frame6.config(highlightbackground="light green",highlightcolor="light green",bg="light green")
        frame7.config(highlightbackground="light green",highlightcolor="light green",bg="light green")
        frame8.config(highlightbackground="light green",highlightcolor="light green",bg="light green")
        frame9.config(highlightbackground="light green",highlightcolor="light green",bg="light green")
        frame10.config(highlightbackground="light green",highlightcolor="light green",bg="light green")
        frame11.config(highlightbackground="light green",highlightcolor="light green",bg="light green")
        frame12.config(highlightbackground="light green",highlightcolor="light green",bg="light green")
        frame13.config(highlightbackground="light green",highlightcolor="light green",bg="light green")
        lbl.config(bg="#252525")
        btn1.config(bg="#252525",fg="white",bd=1)
        btn2.config(bg="#252525",fg="white",bd=1)
        btn3.config(bg="#252525",fg="white",bd=1)
        btn9.config(bg="#252525",fg="white",bd=1)
        wrldbtn8.config(bg="#252525",fg="white",bd=1)
        btn11.config(bg="#252525",fg="white",bd=1)
        btn12.config(bg="#252525",fg="white",bd=1)
        btn13.config(bg="#252525",fg="white",bd=1)
        btn14.config(bg="#252525",fg="white",bd=1)
        btn10.config(bg="#252525",fg="white",bd=1)
def btnmve1(f):
    button2.place(x=1020,y=10)
def btnleve1(e):
    button2.place(x=1050,y=8)
nghtmde=ImageTk.PhotoImage(Image.open("./images/nightmode.jpg"))
button2=Button(root,text="DARK MODE",font="times 15 bold italic",image=nghtmde,command=button3)
button2.place(x=1050,y=8)
button2.bind("<Enter>",btnmve1)
button2.bind("<Leave>",btnleve1)
########## VOICE RUN ############
engine.runAndWait()
engine.stop()
######## CHECK TIME OF APP ############
cProfile.run('re.compile("foo|bar")')
####### THREAD TO INCREASE THE PERFORMANCE #################
control_thread = Thread(target=root.mainloop(),daemon=TRUE)
control_thread.start()

