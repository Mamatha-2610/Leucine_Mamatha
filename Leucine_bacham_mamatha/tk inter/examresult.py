import tkinter as tk
top = tk.Tk()
top.title("Mid marks")
top.geometry("700x250")
# display lables
tk.Label(top, text="Name").grid(row=0, column=0)
tk.Label(top, text="roll no").grid(row=1, column=0)
tk.Label(top, text="class").grid(row=0, column=3)
tk.Label(top, text="section").grid(row=1, column=3)
tk.Label(top, text="S.No").grid(row=2, column=0)
tk.Label(top, text="1").grid(row=3, column=0)
tk.Label(top, text="2").grid(row=4, column=0)
tk.Label(top, text="3").grid(row=5, column=0)
tk.Label(top, text="Subject").grid(row=2, column=1)
tk.Label(top, text="OS").grid(row=3, column=1)
tk.Label(top, text="DBMS").grid(row=4, column=1)
tk.Label(top, text="PP").grid(row=5, column=1)
tk.Label(top, text="Marks").grid(row=2, column=2)
tk.Label(top, text="Total").grid(row=7, column=3)
tk.Label(top, text="Average").grid(row=8, column=3)
# Display entry fields
e1 = tk.Entry(top)
e2 = tk.Entry(top)
e3 = tk.Entry(top)
e4 = tk.Entry(top)
e5 = tk.Entry(top)
e6 = tk.Entry(top)
e7 = tk.Entry(top)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=0, column=4)
e4.grid(row=1, column=4)
e5.grid(row=3, column=2)
e6.grid(row=4, column=2)
e7.grid(row=5, column=2)
def display():
            OS=int(e5.get())
            DBMS=int(e6.get())
            PP=int(e7.get())
            tot=OS+DBMS+PP
            avg=tot/3
            # to display total
            tk.Label(top, text=str(tot)).grid(row=7, column=4)
            # to display AVG
            tk.Label(top, text=str(avg)).grid(row=8, column=4)       
# end of display function
# button to display all the calculated total scores and avg
button1=tk.Button(top, text="Submit", bg="green", command=display)
button1.grid(row=8, column=1)
top.mainloop()