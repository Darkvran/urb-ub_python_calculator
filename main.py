from tkinter import *

if __name__ == '__main__':
  #выполнение кода до загрузки
  window = Tk()
  window.title('Python calculator')
  window.geometry('400x500')
  window.resizable(height=False, width=False)

  app_frame = Frame(window)
  app_frame.pack()

  app_title = Label(app_frame, text='Simple python calculator', font=50)
  app_title.grid(row=0, columnspan=2, pady=(5,0))

  first_input_title = Label(app_frame, text='Введите первое число:')
  first_input_title.grid(row=1, columnspan=2, pady=(10,0))
  first_input = Entry(app_frame)
  first_input.grid(row=2, columnspan=2,)


  second_input_title = Label(app_frame, text='Введите второе число:')
  second_input_title.grid(row=3, columnspan=2, pady=(10,0))
  second_input = Entry(app_frame)
  second_input.grid(row=4, columnspan=2)

  plus_button = Button(app_frame, text='+')
  plus_button.grid(row=5, column=0, ipadx=10, ipady=6, pady=(20,0))

  minus_button = Button(app_frame, text='-')
  minus_button.grid(row=5, column=1, ipadx=10, ipady=6, pady=(20,0))

  multiply_button = Button(app_frame, text='*')
  multiply_button.grid(row=6, column=0, ipadx=10, ipady=6, pady=(10,0))

  divide_button = Button(app_frame, text='/')
  divide_button.grid(row=6, column=1, ipadx=10, ipady=6, pady=(10,0))

  #to-do: answer label
  answer_label = Label(app_frame, bg='grey')
  answer_label.grid(row=7, columnspan=2, pady=(30,0), ipady=30, ipadx=100)


  window.mainloop()