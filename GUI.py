from tkinter import*

fenetre = Tk()
fenetre.geometry("500x500")

label = Label(fenetre, text="Recheche d'aliments de substitution")
label.pack()

Category = Label(fenetre,text="Selectionner une catégorie").pack(side=LEFT)

liste = Listbox(fenetre)
liste.insert(1, "saucisson")
liste.insert(2, "pizza")
liste.insert(3, "sfds")
liste.insert(4, "sdfsf")
liste.insert(5, "sfdsf")

liste.pack(side=LEFT)

bouton=Button(fenetre, text="Fermer",bg="red", command=fenetre.quit).pack(side=BOTTOM)




fenetre.mainloop()