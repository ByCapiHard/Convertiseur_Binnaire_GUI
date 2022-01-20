from tkinter import *
from tkinter import messagebox

root =Tk()



root.title("Convertiseur de chiffre binaire")
root.geometry("720x480")
root.config(bg="#ffffff")
root.iconbitmap("assets/binaire.ico")
root.maxsize(720,480)
root.minsize(720,480)

image=PhotoImage(file='assets/tkinter.png')
Label(root,image=image,bg="#ffffff").pack(side=LEFT)

frame=Frame(root,bg="#ffffff")
contenu_text= Label(frame,text="Convertir en binnaire",bg="#ffffff").pack()
entry = Entry(frame,width=40)

entry.pack()

def bianire():
        
    try:
        res=int(entry.get())
        nb=8
        if res == 0:
            return "0".zfill(nb)
        if res<0:
            res += 1<<nb
        b=""
        while res != 0:
            res, r = divmod(res, 2)
            b = "01"[r] + b
        messagebox.showinfo(title="Resultat", message="La convertion de {} est de {}".format(entry.get(),b.zfill(nb)))
        
    except (RuntimeError, TypeError, NameError, ValueError):
        messagebox.showerror(title="Erreur",message="Veuillez mettre un decimal non un chiffre à virgule (application en beta), ni une chaine de caractére")
boutton=Button(frame, bg="#87eda2",text="Convertir", command=bianire).pack()
frame.pack(side=RIGHT,expand=YES)

root.mainloop()



    
