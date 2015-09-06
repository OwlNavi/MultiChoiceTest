from Tkinter import *
import ScrolledText

class Test:
    def __init__(self):

        self.saveButton = Button(text='Save',width=7,command=self.save_answer_command)
        self.saveButton.grid(row=0,column=3)
        
        self.newButton = Button(text='New',width=7,command=self.new_command)
        self.newButton.grid(row=0,column=0)

        self.quitButton = Button(text='Quit',width=7,command=self.quit_command)
        self.quitButton.grid(row=0,column=4)

        self.deselectButton = Button(text='Deselect',width=7,command=self.deselect)
        self.deselectButton.grid(row=0,column=1)

        self.selectButton = Button(text='Select',width=7,command=self.select)
        self.selectButton.grid(row=0,column=2)
        
        self.output = Label(text='This is a blank space')
        self.output.grid(row=3,column=0,columnspan=5)

        self.doneButton = Button(text='Done',width=4,command=self.save_answer_command)
        self.doneButton.grid(row=2,column=5)

        self.test_num = 0
        self.question_num = 1
        self.filename = 'test{}.txt'.format(str(self.test_num))
        self.v = IntVar()

        self.selected_answer = ''
        
        self.button1 = Radiobutton(text='A', variable=self.v, value=1, width=4)
        self.button2 = Radiobutton(text='B', variable=self.v, value=2, width=4)
        self.button3 = Radiobutton(text='C', variable=self.v, value=3, width=4)
        self.button4 = Radiobutton(text='D', variable=self.v, value=4, width=4)
        self.button5 = Radiobutton(text='E', variable=self.v, value=5, width=4)

        
        self.button1.grid(row=2,column=0)
        self.button2.grid(row=2,column=1)
        self.button3.grid(row=2,column=2)
        self.button4.grid(row=2,column=3)
        self.button5.grid(row=2,column=4)

        #the magic button
        self.buttonx = Radiobutton(variable=self.v, value=0)
        #the magic text box
        self.outputx = ScrolledText.ScrolledText(height=10,width=42)
        self.outputx.grid(row=4,column=0,columnspan=5)

        #root.bind('<Return>',self.save_answer_command2)
        root.bind('<Return>',self.save_answer_command2)
        root.bind('1', self.select1)
        root.bind('2', self.select2)
        root.bind('3', self.select3)
        root.bind('4', self.select4)
        root.bind('5', self.select5)
        root.bind('`', self.select_magic_button)
        root.bind('q', self.quit_command2)

    def select1(self, value):
        self.button1.select()
    def select2(self, value):
        self.button2.select()
    def select3(self, value):
        self.button3.select()
    def select4(self, value):
        self.button4.select()
    def select5(self, value):
        self.button5.select()
    def select_magic_button(self, value):
        self.buttonx.select()
        
        
    def press(self, event):
        print 'You pressed the button!'

    def value(self, parent):
        value = self.v.get()
        possible_answers = {
                0: 'None',
                1: 'A',
                2: 'B',
                3: 'C',
                4: 'D',
                5: 'E'
                }
        
        if value != None:
            print possible_answers[value]
            return possible_answers[value]
        else:
            print 'None'
    def save_answer_command2(self,parent):
        answer = self.v.get()
        answer = self.value(answer)
        if self.v.get() != None:
            print self.v.get()
        oldtext = ''
        num = str(self.question_num)
        self.question_num += 1
        myfile = open(self.filename,'r')
        oldtext = myfile.read()
        myfile.close()
        self.outputx.delete("1.0",END)
        newtext = oldtext + '\n' + '{}: {}'.format(num, answer)
        self.outputx.insert(END,newtext)
        myfile = open(self.filename, 'w')
        myfile.write(newtext)
        myfile.close()
        
    def save_answer_command(self):
        answer = self.v.get()
        answer = self.value(answer)
        if self.v.get() != None:
            print self.v.get()
        oldtext = ''
        num = str(self.question_num)
        self.question_num += 1
        myfile = open(self.filename,'r')
        oldtext = myfile.read()
        myfile.close()
        self.outputx.delete("1.0",END)
        newtext = oldtext + '\n' + '{}: {}'.format(num, answer)
        self.outputx.insert(END,newtext)
        myfile = open(self.filename, 'w')
        myfile.write(newtext)
        myfile.close()
           
#        myfile = open(self.filename, 'w')
#        myfile.close()
#        myfile = open(self.filename, 'r')
#        oldtext = myfile.read()
#        myfile.close()
#        myfile = open(self.filename, 'w')
#        newtext = oldtext + '/n' + answer
#        myfile.write(self.value)
#        myfile.close()
    def save_answer_command2(self,parent):
        answer = 0
        if self.v.get() != None:
            print self.v.get()
        else:
            return None
               
    def deselect(self):
        self.select()

    def select(self):
        self.buttonx.select()

    def new_command(self):
        
        name = 'test{}.txt'.format(self.test_num)
        self.test_num += 1
        myfile = open(name, 'w')
        self.question_num = 0
        
    def quit_command(self):
        root.destroy()

    def quit_command2(self, event):
        root.destroy()
root = Tk()
test = Test()
root.mainloop()
