#!/usr/bin/env python
from Tkinter import *
import tkMessageBox
import threshold_scheme
import sys

class Display(Frame):
  
  def start_over(self):
    self.destroy()
    Display().mainloop()
    
  def quit(self):
    sys.exit()
  
  def __init__(self,parent=0):
    Frame.__init__(self,parent)
    self.recover_button = Button(self, text = "Recover Secret", command = self.recover)
    self.generate_button = Button(self, text = "Generate Shares", command = self.generate)
    self.recover_button.grid(row = 0)
    self.generate_button.grid(row = 1)
    self.output = Text(self)
    self.output.grid(row = 5, column = 2)
    self.restart_button = Button(self, text = "Start Over", command = self.start_over)
    self.restart_button.grid(row = 7, column = 0)
    self.quit_button = Button(self, text = 'Quit', command = self.quit)
    self.quit_button.grid(row = 7, column = 1)
    self.pack()
    sys.stdout = self
    
  def write(self, txt):
    self.output.insert(END,str(txt))
        
  def generate(self): 
    self.recover_button.destroy()
    self.generate_button.destroy()
      
    def distribute():
      k = int(self.required.get()) # required number of shares
      n = int(self.total.get()) # total number of shares to generate
      s = self.secret.get() # the secret value
      if k >=2 and k <= n:
        shares = threshold_scheme.dist_shares(k,n,s)
        for share in shares:
          print "%d-%s" % (share,shares[share])
      else:
        tkMessageBox.showerror(message = 'Invalid entry for share numbers!', title = 'Invalid Entry')
      
    self.distribute_button = Button(self, text = "Generate", width = 10, command = distribute)
    self.distribute_button.grid(row = 3)
    self.required = Entry(self)
    self.required.grid(row = 0, column = 1)
    self.total = Entry(self)
    self.total.grid(row = 1, column = 1)
    self.secret = Entry(self)
    self.secret.grid(row = 2, column = 1)
    self.required_label = Label(self, text = 'Required').grid(row = 0, column = 0)
    self.total_label = Label(self, text = 'Total').grid(row = 1, column = 0)
    self.secret_label = Label(self, text = 'Secret').grid(row = 2, column = 0)
  
  def recover(self):  
    self.recover_button.destroy()
    self.generate_button.destroy()
    self.share_entry = Entry(self)
    self.share_entry.grid(row = 2, column = 1)
    self.share_label = Label(self, text = 'Share').grid(row = 2, column = 0)
    self.shares = []
        
    def add_share():
      each  = self.share_entry.get()
      if each.strip() != '':
        print each
        self.share_entry.delete(0, END)
        self.shares.append(each)
      else: 
        tkMessageBox.showerror(message = 'Share cannot be empty!', title = 'Invalid Entry')
              
    def compute():
      if len(self.shares) > 1:
        print threshold_scheme.recover_secret(self.shares)
      else:
        tkMessageBox.showerror(message = 'Need more shares!', title = 'Invalid Entry')
                    
    self.add_share_button = Button(self, text = "Add Share", width = 10, command = add_share)
    self.add_share_button.grid(row =  3, column = 1)
    self.compute_secret_button = Button(self, text = "Recover!", width = 10, command = compute)
    self.compute_secret_button.grid(row =  4, column = 1)
    
if __name__ == '__main__':
  Display().mainloop()