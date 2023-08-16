import pandas as pd
from tkinter import *
from tkinter import filedialog, ttk, messagebox

# Первоначальные настройки главного окна
Window = Tk()
Window.geometry('500x450')
Window.title('SoldierApp')

my_font1=('times', 12, 'bold')

# Объявление переменных и элементов
input1 = StringVar(Window)
input2 = StringVar(Window)
input3 = StringVar(Window)

label1 = Label(Window, text='Выбрать набор данных', width=30, font=my_font1)
label1.grid(row=1, column=1)
button1 = Button(Window, text='Выбрать файл', width=20, command=lambda:upload_file(), background='lightgreen')
button1.grid(row=2,column=1,pady=5) 
label2 = Label(Window, width=40, text='', bg='lightgreen')
label2.grid(row=3,column=1,padx=5)
label1 = []
entry1 = Entry(textvariable=input1)
entry1.grid(row=5, column=1, padx=5, pady=5)
entry2 = Entry(textvariable=input2)
entry2.grid(row=6, column=1, padx=5, pady=5)
entry3 = Entry(textvariable=input3)
entry3.grid(row=7, column=1, padx=5, pady=5)
button2 = Button(Window, text='Добавить элемент', width=20, command=lambda:add_row(), background='lightgreen')
button2.grid(row=5, column=2, padx=5)

# Объявление необходимых функций
def upload_file(): # Загрузка файла с устройства
    global df ,label1
    f_types = [('CSV files',"*.csv"),('All',"*.*")]
    file = filedialog.askopenfilename(filetypes=f_types)
    df=pd.read_csv(file)
    label1=list(df)
    str1="Rows:" + str(df.shape[0])+ " , Columns:"+str(df.shape[1])
    #print(str1)
    label2.config(text=str1)
    trv_refresh()

def trv_refresh(): # Обновление данных
    global df,trv,l1 
    r_set=df.to_numpy().tolist()
    trv=ttk.Treeview(Window,selectmode='browse',height=10,
        show='headings',columns=label1)
    trv.grid(row=4,column=1,columnspan=3,padx=10,pady=20)
    
    for i in label1:
        trv.column(i,width=90,anchor='c')
        trv.heading(i,text=str(i))
    for dt in r_set:
        v=[r for r in dt]
        trv.insert("",'end',iid=v[0],values=v)
    vs = ttk.Scrollbar(Window,orient="vertical", command=trv.yview)
    trv.configure(yscrollcommand=vs.set)  
    vs.grid(row=4,column=4,sticky='ns')
    
def add_row(): # Добавляет ряд значений в выбранный набор данных
    if 'df' in globals():
        global df
        new_list = []
        new_list.append(len(df.index))
        if input1.get() == '':
            new_list.append('undefined')
        else:
            new_list.append(input1.get())
        if input2.get() == '':
            new_list.append('undefined')
        else:
            new_list.append(input2.get())
        if input3.get() == '':
            new_list.append('undefined')
        else:
            new_list.append(input3.get())
        df.loc[len(df.index)] = new_list
        df.to_csv('parsed_data.csv', index=False)
        messagebox.showinfo(title="Уведомление", message="Элемент добавлен! Выберите набор данных снова, чтобы обновить содержание.")
    else:
        messagebox.showwarning(title="Предупреждение", message="Вы не выбрали набор данных!")

# Запуск
Window.mainloop()