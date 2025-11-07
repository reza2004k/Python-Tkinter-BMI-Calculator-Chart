import matplotlib.pyplot as plt
import numpy as np
from tkinter import*

window=Tk()
def calculate():
  weight=float(w.get())
  height=float(h.get())
  bmi_tk=round(weight/(height**2),2)
  Label(window,text=f'Your BMI is : {bmi_tk}',bg='black',fg='white',font=12).pack()
  fr=Frame(window)
  fr.pack(pady=10)
  bt1=Button(fr,text='Chart',command=bmi_calculation,bg='blue',fg='white',font=('bold',14))
  bt1.pack(side='right')
  bt2=Button(fr,text='Quit',command=window.quit,bg='red',fg='white',font=('bold',14))
  bt2.pack(side='left')
  

def bmi_calculation():
  global w,h
  
  w=float(w.get())
  h=float(h.get())
  fig, ax = plt.subplots(figsize=(8, 6))
  ax.set_xlim(40, 200)
  ax.set_ylim(1.4,2.5)

  x_ticks = np.linspace(40, 200, 17)
  y_ticks=np.linspace(1.4,2.5,12)
  ax.set_xticks(x_ticks)
  ax.set_yticks(y_ticks)
  ax.set_title('BMI Chart',color='#00e50f',fontweight='bold',fontsize=20)
  ax.set_xlabel('weight(kg)',color='red')
  ax.set_ylabel('height(m)',color='red')

  bmi=round(w/(h**2),2)
  if bmi<18.5:
    ax.annotate(f'{round((18.5-bmi)*(h**2),2)}kg Underweight', (w, h), textcoords="offset points", xytext=(0,10), ha='left',color='blue')
    ax.scatter(w,h,color='blue')
  elif 18.5<=bmi<25:
    ax.annotate('Normal weight', (w, h), textcoords="offset points", xytext=(0,10), ha='left',color='#1fa300')
    ax.scatter(w,h,color='#1fa300')
  else:
    ax.annotate(f'{round((bmi-24.99)*(h**2),2)}kg Overweight', (w, h), textcoords="offset points", xytext=(0,10), ha='left',color='red')
    ax.scatter(w,h,color='red')
  
  
  plt.show()
  window.quit()  
  

window.geometry('280x300')
window.title('BMI')
window.resizable(False,False)
window.config(bg='black')
Label(window,text='Weight(kg):',font=('B Titr',18),bg='black',fg='white',bd=5).pack()
w=Entry(window,font='bold')
w.pack()
Label(window,text='Height(m):',font=('B Titr',19),bg='black',fg='white',bd=5).pack()
h=Entry(window,font='bold')
h.pack()
bt3=Button(window,text='Calculate BMI',command=calculate,bg='green',fg='white',font=('bold',12))
bt3.pack(pady=10)
window.mainloop()
