import customtkinter
from tkinter import END
from tkinter import messagebox

#Functionality Section
def answer():
    expression=entryField.get()
    try:
       result=eval(expression)
       ans=round(result,1)
       entryField.delete(0, END)
       entryField.insert(0, ans)
    except SyntaxError:
        messagebox.showerror('SyntaxError','Invalid Expression!')
    except ZeroDivisionError:
        messagebox.showerror('ZeroDivisionError', 'A number cannot be divided by zero!')
def click(number):
    entryField.insert(END,number)
def clear():
    entryField.delete(0,END)

#GUI section
root = customtkinter.CTk()
root.title("Calculator")
root.geometry('340x444')
root.config(bg='#242424')

entryField =customtkinter.CTkEntry(root, font=('Roboto',20,'bold'),text_color='#ffffff',fg_color='#121212',
                                   border_color='#000000',width=332, height=136, bg_color='#242424')
entryField.grid(row=0,column=0,padx=5,pady=5, columnspan=4, sticky="nsew")
entryField.configure(justify="right")

entryField.insert("end", "")


b1=customtkinter.CTkButton(root,font=('Roboto',20,'bold'), corner_radius=84,fg_color='#272727',bg_color='#242424', text_color='#feb0b0', text='1', width=66,height=44, cursor='hand2', hover_color='#181818', border_width=2, border_color='#000000', command=lambda :click('1'))
b1.grid(row=1,column=0,pady=6, padx=2)
b2=customtkinter.CTkButton(root,font=('Roboto',20,'bold'), corner_radius=84,fg_color='#272727',bg_color='#242424', text_color='#feb0b0', text='2', width=66,height=44, cursor='hand2', hover_color='#181818', border_width=2, border_color='#000000', command=lambda :click('2'))
b2.grid(row=1,column=1)
b3=customtkinter.CTkButton(root,font=('Roboto',20,'bold'), corner_radius=84,fg_color='#272727',bg_color='#242424', text_color='#feb0b0', text='3', width=66,height=44, cursor='hand2', hover_color='#181818', border_width=2, border_color='#000000', command=lambda :click('3'))
b3.grid(row=1,column=2)
bdiv=customtkinter.CTkButton(root,font=('Roboto',20,'bold'), corner_radius=84,fg_color='#272727',bg_color='#242424', text_color='#feb0b0', text='/', width=66,height=44, cursor='hand2', hover_color='#181818', border_width=2, border_color='#000000', command=lambda :click('/'))
bdiv.grid(row=1,column=3)

b4=customtkinter.CTkButton(root,font=('Roboto',20,'bold'), corner_radius=84,fg_color='#272727',bg_color='#242424', text_color='#feb0b0', text='4', width=66,height=44, cursor='hand2', hover_color='#181818', border_width=2, border_color='#000000', command=lambda :click('4'))
b4.grid(row=2,column=0,pady=6)
b5=customtkinter.CTkButton(root,font=('Roboto',20,'bold'), corner_radius=84,fg_color='#272727',bg_color='#242424', text_color='#feb0b0', text='5', width=66,height=44, cursor='hand2', hover_color='#181818', border_width=2, border_color='#000000', command=lambda :click('5'))
b5.grid(row=2,column=1)
b6=customtkinter.CTkButton(root,font=('Roboto',20,'bold'), corner_radius=84,fg_color='#272727',bg_color='#242424', text_color='#feb0b0', text='6', width=66,height=44, cursor='hand2', hover_color='#181818', border_width=2, border_color='#000000', command=lambda :click('6'))
b6.grid(row=2,column=2)
bmul=customtkinter.CTkButton(root,font=('Roboto',20,'bold'), corner_radius=84,fg_color='#272727',bg_color='#242424', text_color='#feb0b0', text='x', width=66,height=44, cursor='hand2', hover_color='#181818', border_width=2, border_color='#000000', command=lambda :click('*'))
bmul.grid(row=2,column=3)

b7=customtkinter.CTkButton(root,font=('Roboto',20,'bold'), corner_radius=84,fg_color='#272727',bg_color='#242424', text_color='#feb0b0', text='7', width=66,height=44, cursor='hand2', hover_color='#181818', border_width=2, border_color='#000000', command=lambda :click('7'))
b7.grid(row=3,column=0,pady=6)
b8=customtkinter.CTkButton(root,font=('Roboto',20,'bold'), corner_radius=84,fg_color='#272727',bg_color='#242424', text_color='#feb0b0', text='8', width=66,height=44, cursor='hand2', hover_color='#181818', border_width=2, border_color='#000000', command=lambda :click('8'))
b8.grid(row=3,column=1)
b9=customtkinter.CTkButton(root,font=('Roboto',20,'bold'), corner_radius=84,fg_color='#272727',bg_color='#242424', text_color='#feb0b0', text='9', width=66,height=44, cursor='hand2', hover_color='#181818', border_width=2, border_color='#000000', command=lambda :click('9'))
b9.grid(row=3,column=2)
bmin=customtkinter.CTkButton(root,font=('Roboto',20,'bold'), corner_radius=84,fg_color='#272727',bg_color='#242424', text_color='#feb0b0', text='-', width=66,height=44, cursor='hand2', hover_color='#181818', border_width=2, border_color='#000000', command=lambda :click('-'))
bmin.grid(row=3,column=3)

b0=customtkinter.CTkButton(root,font=('Roboto',20,'bold'), corner_radius=84,fg_color='#272727',bg_color='#242424', text_color='#feb0b0', text='0', width=66,height=44, cursor='hand2', hover_color='#181818', border_width=2, border_color='#000000', command=lambda :click('0'))
b0.grid(row=4,column=0,pady=6)
bdot=customtkinter.CTkButton(root,font=('Roboto',20,'bold'), corner_radius=84,fg_color='#272727',bg_color='#242424', text_color='#feb0b0', text='.', width=66,height=44, cursor='hand2', hover_color='#181818', border_width=2, border_color='#000000', command=lambda :click('.'))
bdot.grid(row=4,column=1)
bclr=customtkinter.CTkButton(root,font=('Roboto',20,'bold'), corner_radius=84,fg_color='#272727',bg_color='#242424', text_color='#feb0b0', text='C', width=66,height=44, cursor='hand2', hover_color='#181818', border_width=2, border_color='#000000', command=clear)
bclr.grid(row=4,column=2)
bplus=customtkinter.CTkButton(root,font=('Roboto',20,'bold'), corner_radius=84,fg_color='#272727',bg_color='#242424', text_color='#feb0b0', text='+', width=66,height=44, cursor='hand2', hover_color='#181818', border_width=2, border_color='#000000', command=lambda :click('+'))
bplus.grid(row=4,column=3)
beq=customtkinter.CTkButton(root,font=('Arial',20,'bold'), corner_radius=16,fg_color='#E39696',bg_color='#242424', text_color='#121212', text='=', width=320,height=44, cursor='hand2', hover_color='#C38080', border_width=2, border_color='#000000', command=answer)
beq.grid(row=5,column=0, columnspan=4, pady=10, padx=2)
root.mainloop()