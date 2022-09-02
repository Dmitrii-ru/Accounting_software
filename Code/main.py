import tkinter


from Nalog import nal, result
# sudo apt install python3-tk
win_main = tkinter.Tk()
win_main.geometry(f'200x70+10+20')
win_main.config(bg='#20FC9D')
win_main.title("Бух")
btn1 = tkinter.Button(win_main, text="Налоги 1.Грузим налоги 2. Грузим больничный ", command=nal, bg="#20FCED", pady=0.5, padx=0.5).grid(row=6, column=1)

btn2 = tkinter.Button(win_main, text="Результат оплачено", command=result, bg="#20FCED", pady=0.5, padx=0.5).grid(row=7,
                                                                                                             column=1)

win_main.mainloop()


