from tkinter import *
import time
root=Tk()
root.title('DIGITAL CLOCK')
root.geometry('1350x700+0+0')
root.config(bg='black')

def clock():
    h = str(time.strftime("%H"))
    m = str(time.strftime("%M"))
    s = str(time.strftime("%S"))
    

    if int(h)>12 and int(m)>0:
        lbl_noon.config(text='PM')

    if int(h) >12:
        h = str((int(h)-12))
    


    lbl_hr.config(text=h)
    lbl_min.config(text=m)
    lbl_sec.config(text=s)

    lbl_hr.after(200,clock)


lbl_hr=Label(root,text='12',font=('times new roman',50,'bold'),bg = 'blue',fg='white')
lbl_hr.place(x=350,y=200,width=150,height=150)

lbl_hr2=Label(root,text='HOUR',font=('times new roman',20,'bold'),bg = 'blue',fg='white')
lbl_hr2.place(x=350,y=360,width=150,height=50)

lbl_min=Label(root,text='12',font=('times new roman',50,'bold'),bg = 'grey',fg='white')
lbl_min.place(x=520,y=200,width=150,height=150)

lbl_min2=Label(root,text='MINUTE',font=('times new roman',20,'bold'),bg = 'grey',fg='white')
lbl_min2.place(x=520,y=360,width=150,height=50)

lbl_sec=Label(root,text='12',font=('times new roman',50,'bold'),bg = 'red',fg='white')
lbl_sec.place(x=690,y=200,width=150,height=150)

lbl_sec2=Label(root,text='SECOND',font=('times new roman',20,'bold'),bg = 'red',fg='white')
lbl_sec2.place(x=690,y=360,width=150,height=50)

lbl_noon=Label(root,text='PM',font=('times new roman',50,'bold'),bg = 'red',fg='white')
lbl_noon.place(x=860,y=200,width=150,height=150)

lbl_noon2=Label(root,text='NOON',font=('times new roman',20,'bold'),bg = 'red',fg='white')
lbl_noon2.place(x=860,y=360,width=150,height=50)

clock()
root.mainloop()
