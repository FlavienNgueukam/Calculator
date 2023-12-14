import tkinter as tk
import math
from math import sqrt, factorial,exp,log,log10,pi,e


class calculator:
    def __init__ (self,root):
        self.root = root
        root.title("Calculator")
        self.entry = tk.Entry(root, font =('Arial', 20 ) , justify = 'right', bd = 10)
        self.entry.grid(row=0, column=0, columnspan = 5)

        #Buttton Layout
        buttons = ['2sqrt','pi','e','CE','<--',
                   'x^2','1/x','|x|','exp','%',
                   'sqrt','(',')','n!','/',
                   'x^y','7','8','9','*',
                   '10^y','4','5','6','-',
                   'log','1','2','3','+',
                   'ln','+/-','0',',','=',
                   ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(root, text = button, padx = 20, pady = 20 , font = ('Arial',14), command = lambda b = button: self.button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 4:
               col_val = 0
               row_val += 1

    def button_click(self,button):
        current_entry = self.entry.get()

        if button == 'pi':
           
            self.entry.insert(tk.END, str(math.pi))
        elif button == 'e':
            
            self.entry.insert(tk.END,str(math.e))
        elif button == 'CE':
           
            self.entry.delete(0,tk.END)
        elif button == 'sqrt':
            
            self.entry.insert(tk.END,'sqrt(')
        elif button == '^':
            self.entry.insert(tk.END, '**')
        elif button == 'x^2':
            
            self.entry.insert(tk.END,'** 2')
        elif button == '1/x':
            
            self.entry.insert(tk.END,'1/')
        elif button == '|x|':
            
            self.entry.insert(tk.END,'abs(')
        elif button == 'exp':
            
            self.entry.insert(tk.END,'exp(')
        elif button == '2sqrt':
           
            self.entry.insert(tk.END,'sqrt(')
        elif button == 'n!':
            
            self.entry.insert(tk.END,'factorial(')
        elif button == 'x^y':
            self.entry.insert(tk.END,'**')

        elif button == 'log':
            
            self.entry.insert(tk.END,'log10(')
        elif button == '+/-':
            self.entry.insert(tk.END,'-')
        elif  button == '<--':
            self.entry.delete(len(current_entry) -1,tk.END)
  
        elif button == 'ln':
           
            self.entry.insert(tk.END,'math.log(')
        elif button == '10^y':
            
            self.entry.insert(tk.END,'10**')
        elif button == '%':
            
            self.entry.insert(tk.END,'/100')
        elif button == '=':
             try:
                 result = eval(current_entry)
                 self.entry.delete(0,tk.END)
                 self.entry.insert(tk.END,str(result))

             except Exception as e:
                 self.entry.delete(0,tk.END)
                 self.entry.insert(tk.END, "Error")

        else:
             self.entry.insert(tk.END,button)

#Create and run  the calculator
root=tk.Tk()
calc= calculator(root)
root.mainloop()
         
