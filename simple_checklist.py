import tkinter
from tkinter import ttk
import os
#Defining Window
root=tkinter.Tk()
root.geometry("400x400")
root.title("Simple Check-List")
root.iconbitmap("check.ico")
root.resizable(0,0)
root.config(bg="#6d1cbc")

#Defining Font and style
root_clr="#6d1cbc"
f=("Comic Sans MS",10,"bold")
button_color ="#b189f5"

#Define Functions
def add_item(*events):                       #*events is a wild card to link both enter key and add_item button to this function
    '''Add an item to the list box'''
    if entry_box.get()!='':
        item=entry_box.get()
        entry_box.delete(0,tkinter.END)
        my_list.insert(tkinter.END,item)   #tkinter.END gives the last index so that the item can be added at the end of the list 
    else:
        pass

def remove_item():
    '''Remove the selected (ANCHOR) item from the listbox'''
    my_list.delete(tkinter.ANCHOR)  #Anchor passes in the index of item that is selected


def clear_list():
    '''To clear the list'''
    my_list.delete(0,tkinter.END)    #Deleting from first to last element
    #To remove the previously saved text file
    if os.path.exists("checkList.txt"):
        os.remove("checkList.txt")
    else:
        pass

def save_list():
    '''Saving the list to a text file'''
    with open("checkList.txt",'w') as f:
        #listbox.get() it returns a tuple
        list_tuple=my_list.get(0,tkinter.END)
        for items in list_tuple:
            #take precaution to include only one \n for each item
            if items.endswith("\n"):
                f.write(items)
            else:
                f.write(items + '\n')

def open_list():
    '''Open the previously saved list if that exists'''
    try:
        with open("checkList.txt","r") as f:
            for lines in f.readlines():
                my_list.insert(tkinter.END,lines)
    except:
        return

#Define Layout
input_frame=tkinter.Frame(root,bg=root_clr)
output_frame=tkinter.Frame(root,bg=root_clr)
button_frame=tkinter.Frame(root,bg=root_clr)
input_frame.pack()
output_frame.pack()
button_frame.pack()

#Defining Input Frame
entry_box=tkinter.Entry(input_frame,width=45,border=2)
add_button=tkinter.Button(input_frame,text="Add Item",width=10,bg=button_color,font=f,relief="raised",borderwidth=2,command=add_item)
entry_box.bind("<Return>", add_item)  #Binding the enter keyword, pressing enter after typing will automatically add the item without  cliclick on add item button
entry_box.grid(row=0,column=0,padx=(10,0),pady=10)
add_button.grid(row=0,column=1,padx=(10,0),pady=10,ipadx=5)

#Output Frame layout
#We will create a list box widget
my_scrollbar=tkinter.Scrollbar(output_frame)
my_list=tkinter.Listbox(output_frame,height=15,width=45,borderwidth=2,font=f,yscrollcommand=my_scrollbar.set)
my_list.grid(row=0,column=0)
my_scrollbar.grid(row=0,column=1,sticky='NS')
#link scrollbar to list box
my_scrollbar.config(command=my_list.yview) #y.view to scroll vertically (up&down), x.view to scroll horizontally(left&right)

#Button Frame layout
remove_button=tkinter.Button(button_frame,text="Remove Item",font=f,command=remove_item)
clear_button=tkinter.Button(button_frame,text="Clear List",font=f,command=clear_list)
save_button=tkinter.Button(button_frame,text="Save List",font=f,command=save_list)
exit_button=tkinter.Button(button_frame,text="Exit",font=f,command=root.destroy)
remove_button.grid(row=0,column=0,pady=5,padx=2)
clear_button.grid(row=0,column=1,pady=5,padx=2,ipadx=10)
save_button.grid(row=0,column=2,pady=5,padx=2,ipadx=10)
exit_button.grid(row=0,column=3,pady=5,padx=2,ipadx=20)

open_list()

root.mainloop()