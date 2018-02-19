# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 01:54:28 2018

@author: ARKADIP GHOSH & AISHWARJYAMOY MUKHERJEE
"""
import Breast_cancer_Prediction as bcp
from tkinter import *
root=Tk()
a=DoubleVar()
b=DoubleVar()
c=DoubleVar()
d=DoubleVar()
e=DoubleVar()
f=DoubleVar()
g=DoubleVar()
h=DoubleVar()
i=DoubleVar()
j=DoubleVar()
k=DoubleVar()
l=DoubleVar()
m=DoubleVar()
n=DoubleVar()
o=DoubleVar()
p=DoubleVar()
q=DoubleVar()
r=DoubleVar()
s=DoubleVar()
t=DoubleVar()
u=DoubleVar()
v=DoubleVar()
w=DoubleVar()
x=DoubleVar()
y=DoubleVar()
z=DoubleVar()
a1=DoubleVar()
b1=DoubleVar()
c1=DoubleVar()
d1=DoubleVar()
label_1=Label(root,text="Mean Radius",bg="red",fg="white")
entry_1=Entry(root,textvariable=a)
label_2=Label(root,text="Mean Texture",bg="red",fg="white")
entry_2=Entry(root,textvariable=b)
label_3=Label(root,text="Mean Perimeter",bg="red",fg="white")
entry_3=Entry(root,textvariable=c)
label_4=Label(root,text="Mean Area",bg="red",fg="white")
entry_4=Entry(root,textvariable=d)
label_5=Label(root,text="Mean Smoothness",bg="red",fg="white")
entry_5=Entry(root,textvariable=e)
label_6=Label(root,text="Mean Compactness",bg="red",fg="white")
entry_6=Entry(root,textvariable=f)
label_7=Label(root,text="Mean Concavity",bg="red",fg="white")
entry_7=Entry(root,textvariable=g)
label_8=Label(root,text="Mean Concave Points",bg="red",fg="white")
entry_8=Entry(root,textvariable=h)
label_9=Label(root,text="Mean Symmetry",bg="red",fg="white")
entry_9=Entry(root,textvariable=i)
label_10=Label(root,text="Mean Fractal Dimension",bg="red",fg="white")
entry_10=Entry(root,textvariable=j)
label_11=Label(root,text="Standard Error Radius",bg="red",fg="white")
entry_11=Entry(root,textvariable=k)
label_12=Label(root,text="Standard Error Texture",bg="red",fg="white")
entry_12=Entry(root,textvariable=l)
label_13=Label(root,text="Standard Error Perimeter",bg="red",fg="white")
entry_13=Entry(root,textvariable=m)
label_14=Label(root,text="Standard Error Area",bg="red",fg="white")
entry_14=Entry(root,textvariable=n)
label_15=Label(root,text="Standard Error Smoothness",bg="red",fg="white")
entry_15=Entry(root,textvariable=o)
label_16=Label(root,text="Standard Error Compactness",bg="red",fg="white")
entry_16=Entry(root,textvariable=p)
label_17=Label(root,text="Standard Error Concavity",bg="red",fg="white")
entry_17=Entry(root,textvariable=q)
label_18=Label(root,text="Standard Error Concave Points",bg="red",fg="white")
entry_18=Entry(root,textvariable=r)
label_19=Label(root,text="Standard Error Symmetry",bg="red",fg="white")
entry_19=Entry(root,textvariable=s)
label_20=Label(root,text="Standard Error Fractal Dimension",bg="red",fg="white")
entry_20=Entry(root,textvariable=t)
label_21=Label(root,text="Worst Radius",bg="red",fg="white")
entry_21=Entry(root,textvariable=u)
label_22=Label(root,text="Worst Texture",bg="red",fg="white")
entry_22=Entry(root,textvariable=v)
label_23=Label(root,text="Worst Perimeter",bg="red",fg="white")
entry_23=Entry(root,textvariable=w)
label_24=Label(root,text="Worst Area",bg="red",fg="white")
entry_24=Entry(root,textvariable=x)
label_25=Label(root,text="Worst Smoothness",bg="red",fg="white")
entry_25=Entry(root,textvariable=y)
label_26=Label(root,text="Worst Compactness",bg="red",fg="white")
entry_26=Entry(root,textvariable=z)
label_27=Label(root,text="Worst Concavity",bg="red",fg="white")
entry_27=Entry(root,textvariable=a1)
label_28=Label(root,text="Worst Concave Points",bg="red",fg="white")
entry_28=Entry(root,textvariable=b1)
label_29=Label(root,text="Worst Symmetry",bg="red",fg="white")
entry_29=Entry(root,textvariable=c1)
label_30=Label(root,text="Worst Fractal Dimension",bg="red",fg="white")
entry_30=Entry(root,textvariable=d1)








label_1.grid(row=0)
label_2.grid(row=1)
label_3.grid(row=2)
label_4.grid(row=3)
label_5.grid(row=4)
label_6.grid(row=5)
label_7.grid(row=6)
label_8.grid(row=7)
label_9.grid(row=8)
label_10.grid(row=9)
label_11.grid(row=10)
label_12.grid(row=11)
label_13.grid(row=12)
label_14.grid(row=13)
label_15.grid(row=14)
label_16.grid(row=15)
label_17.grid(row=16)
label_18.grid(row=17)
label_19.grid(row=18)
label_20.grid(row=19)
label_21.grid(row=20)
label_22.grid(row=21)
label_23.grid(row=22)
label_24.grid(row=23)
label_25.grid(row=24)
label_26.grid(row=25)
label_27.grid(row=26)
label_28.grid(row=27)
label_29.grid(row=28)
label_30.grid(row=29)





entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)
entry_3.grid(row=2,column=1)
entry_4.grid(row=3,column=1)
entry_5.grid(row=4,column=1)
entry_6.grid(row=5,column=1)
entry_7.grid(row=6,column=1)
entry_8.grid(row=7,column=1)
entry_9.grid(row=8,column=1)
entry_10.grid(row=9,column=1)
entry_11.grid(row=10,column=1)
entry_12.grid(row=11,column=1)
entry_13.grid(row=12,column=1)
entry_14.grid(row=13,column=1)
entry_15.grid(row=14,column=1)
entry_16.grid(row=15,column=1)
entry_17.grid(row=16,column=1)
entry_18.grid(row=17,column=1)
entry_19.grid(row=18,column=1)
entry_20.grid(row=19,column=1)
entry_21.grid(row=20,column=1)
entry_22.grid(row=21,column=1)
entry_23.grid(row=22,column=1)
entry_24.grid(row=23,column=1)
entry_25.grid(row=24,column=1)
entry_26.grid(row=25,column=1)
entry_27.grid(row=26,column=1)
entry_28.grid(row=27,column=1)
entry_29.grid(row=28,column=1)
entry_30.grid(row=29,column=1)
label_34=Label(root,text="Prediction by logistic regression and SVM classifier",bg="red",fg="white")
label_34.grid(row=30)
e1=Button(root,text="Submit",command=lambda :bcp.give_value(a.get(),b.get(),c.get(),d.get(),e.get(),f.get(),g.get(),h.get(),i.get(),j.get(),k.get(),l.get(),m.get(),n.get(),o.get(),p.get(),q.get(),r.get(),s.get(),t.get(),u.get(),v.get(),w.get(),x.get(),y.get(),z.get(),a1.get(),b1.get(),c1.get(),d1.get()))
e1.grid(row=30,column=1)
'''label_35=Label(root,text="Prediction by Support Vector Machine classifier",bg="red",fg="white")
label_35.grid(row=31)
e2=Button(root,text="Submit",command=lambda :bcp.gives_value(a.get(),b.get(),c.get(),d.get(),e.get(),f.get(),g.get(),h.get(),i.get(),j.get(),k.get(),l.get(),m.get(),n.get(),o.get(),p.get(),q.get(),r.get(),s.get(),t.get(),u.get(),v.get(),w.get(),x.get(),y.get(),z.get(),a1.get(),b1.get(),c1.get(),d1.get()))
e2.grid(row=31,column=1)'''



root.mainloop()






























