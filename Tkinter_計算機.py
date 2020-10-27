
import tkinter as tk

win=tk.Tk()

win.title('計算機')
frame1=tk.Frame(win)
frame1.pack(fill='x')
frame2=tk.Frame(win)
frame2.pack()

#建立上方的frame
entry=tk.Entry(frame1,bg='lightpink',fg='black',font=('Arial',20),borderwidth=3)
entry.pack(fill='x')
label=tk.Label(frame1,text='計算結果',bg='black',fg='yellow',font=('Arial',16)
,anchor='e')
label.pack(fill='x')


button_text='1,2,3,+,4,5,6,-,7,8,9,*,0,cls,=,/'

button_text=button_text.split(',')


def click(x):
    entry.insert('end',x)  

def clear():
    entry.delete(0,'end')
    
def answer():
    try:
        input_value=entry.get()
        output_value=eval(input_value)
        label.config(text=output_value)
    except ZeroDivisionError:
        label.config(text='ZeroDivisionError')
    except:
        label.config(text='算式有誤')
    clear()
    

for i in range(len(button_text)):    
    x=button_text[i]    
    #clear
    if i==13:
        button=tk.Button(frame2,text=button_text[i],width=10,command=clear)
    elif i==14:
         button=tk.Button(frame2,text=button_text[i],width=10,command=answer)
    else:
        button=tk.Button(frame2,text=button_text[i],width=10,
                         command=lambda x=x:click(x))
    button.grid(padx=5,pady=5,row=int(i/4),column=i%4)
    
    
    
win.mainloop()
