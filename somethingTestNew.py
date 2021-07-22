import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from flask import Flask as Fl
from flask import render_template
from flask import request
from flask import session
import requests as rq
import csv
import shutil
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat
from pylatex.utils import italic
app= Fl(__name__)
app.secret_key= b'qsaz^qw!ea@nk,lj'
#def usernamee():
    #username=session['username]
username=None
@app.route('/signup1')
def signup1():
    with app.app_context():
        return render_template('signup.html', text="" )
@app.route('/login1')
def login1():
    with app.app_context():
        return render_template('login.html', text="" )
@app.route('/signup', methods=['Post'])
def signup():
    username= request.form['username']
    for folder in os.listdir(directory+'\\data'):
        if folder==username:
            with app.app_context():
                return render_template('signup.html', text='pick a different username')
    os.mkdir(directory + '\\data\\' + username)
    with app.app_context():
        return render_template('login.html')

class login():
    @app.route("/login", methods=['Post'])
    def login():
        username=session['username']=request.form['username']
        for folder in os.listdir(directory+'\\data'):
            if folder==username:
                filenames = []
                iter = 0
                for file in os.listdir(directory + '\\data\\' + folder): 
                    filenames.append([file,iter])
                    iter+=1
                with app.app_context():
                    return render_template('NPRreportWithText.html', list=filenames)
        with app.app_context():
            return render_template('login.html', text= 'the written username or password is incorrect. please try again')
    @app.route("/login", methods=['Post'])
    def username():
        username=session['username']=request.form['username']
        return(username)
@app.route('/enter')
def enter():
    with app.app_context():
        return render_template('enter.html')
@app.route('/')#methods=["Post"])
def NPRreport():
    if 'username' in session: 
        username=session['username']
        print ('yes')
        filenames = []
        iter = 0
        for filename in os.listdir(directory + "\\data\\" + username):
            filenames.append([filename,iter])
            iter+=1
        with app.app_context():
            return render_template('NPRreportWithText.html', list=filenames)
    else:
        print ('no')
        return render_template('enter.html')
@app.route('/reload/', methods=['Post'])
def reload():
    #username= session['username']=request.form['username'] 
    file=request.files['fileadd']
    file_name=session['file.filename']= file.filename
    import csv
    #with open(directory+"\\data"+filename, 'wb') as csvFile:
    #    writer= csv.writer(csvFile)
    #    writer.writerows(csvstff)
    addfile(file)
    #file.save(directory + "\\data\\" + username + '\\' + file_name)
#    os.path.join(directory + "\\data", file)
#    filenames = []
 #   iter= 0
#    for filename in os.listdir(directory + "\\data\\" + username):
 #       filenames.append([filename,iter])
  #      iter+=1
    filenames=makelist()
        #shutil.copy(directory+'\\work\\'+filename, directory+'\\data\\')
    with app.app_context():
        return render_template('NPRreportWithText.html', list=filenames)
def addfile(file):
    filename=str(file.filename)
    username=str(session['username'])
    file.save(directory + "\\data\\" + username + '\\' + filename)
    #shutil.move(file, directory+'\\data\\'+username)
def makelist():
    username=session['username']
    filenames=[]
    iter=0
    for filename in os.listdir(directory + "\\data\\" + username):
        filenames.append([filename,iter])
        iter+=1
    return (filenames)
class User:
    def __init__(self, per, entl, octn):
        self.per = per
        self.entl = entl
        self.octn = octn
        
    def compare(self, other):
        ret = 0;
        if self.per ==  other.per and self.entl == other.entl:
            ret+=1
            if self.octn == other.octn:
                ret+=1
        return ret

    def __repr__(self):
        return "["+str(self.per)+ ' ' + str(self.entl) + ' ' + str(self.octn)+"]"

class LinkedListIterator:
    def __init__(self, head):
        self.current = head
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            item = self.current
            self.current = self.current.next
            return item

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        out = "["
        if not self.head is None:
            iter = self.head
            while iter:
                out += str(iter.val)
                iter = iter.next
                if (iter):
                    out += "->"
        return out+"]"

    def __iter__(self):
        return LinkedListIterator(self.head)

    def __len__(self):
        count = 0
        for i in self:
            count+=1
        return count

    def add(self, num):
        if self.head == None:
            self.head = Node(num)
        elif self.tail == None:
            node = Node(num, self.head, None)
            self.head.next = node
            self.tail = node
        else: 
            node = Node(num, self.tail, None)
            self.tail.next = node
            self.tail = node
    
    def fadd(self, num):
        if self.head == None:
            self.head = Node(num)
        else:
            node = Node(num, None, self.head)
            self.head = node

    def toVector(self, num):
        vec = []
        for i in range(num):
            vec.append(0)
        if not self.head == None:
            iter = self.head
            while iter:
                vec[iter.val.octn-1]+=1
                iter = iter.next
        return vec
class Node:
    def __init__(self, val = None , prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next
    

directory = r'C:\Users\Administrator\NPRreporting\Costidity\NPRCube'

''' USE THIS SECTION TO DEFINE THE NAMES OF THE OCTANTS ON THE HORIZONTAL AXIS OF THE GRAPH'''
#For all colos visit https://matplotlib.org/stable/gallery/color/named_colors.html and scroll down a little
OCTANT_ONE = '1,1,1 \nGO'
OCTANT_ONE_COLOR = "lime"

OCTANT_TWO = '1,1,0 \nGo\nBlock'
OCTANT_TWO_COLOR = "greenyellow"

OCTANT_THREE = '1,0,1 \nException\nGo'
OCTANT_THREE_COLOR = "yellow"

OCTANT_FOUR = '1,0,0 \nException\nStop'
OCTANT_FOUR_COLOR = "orange"

OCTANT_FIVE = '0,1,1 \nVulnerability\nGo'
OCTANT_FIVE_COLOR = "greenyellow"

OCTANT_SIX = '0,1,0 \nVulnerability\nBlock'
OCTANT_SIX_COLOR = "yellow"

OCTANT_SEVEN = '0,0,1 \nVulnerablity\nException'
OCTANT_SEVEN_COLOR = 'red'

OCTANT_EIGHT = '0,0,0 \nALL STOP\nBlock'
OCTANT_EIGHT_COLOR = "lime"




'''TITLE'''
TITLE = "Number of values in octant"




'''USE THIS SECTION TO CUSTOMISE THE X AND Y LABELS'''
#For all colos visit https://matplotlib.org/stable/gallery/color/named_colors.html and scroll down a little
LABELSIZE = 10
X_AXIS = "Octant Name"
X_COLOR = "Black"

Y_AXIS_NUM = "Amount of users in Octant "
Y_AXIS_MON = "Amount of dollars"
Y_COLOR = "Black"



COSTIDITY_COEFF = [1,2,3,4,2,3,5,1]
constant = 100
         

@app.route("/report/", methods=['POST'])
def main():
    print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
    print(request.form)
    boxes=[]
    for key in request.form:
        boxes.append(request.form[key])
    file = boxes[0]
    print (boxes[1])
    lines = ""
    counter, altc = plot('file_path', file)
    plotmoney(constant, COSTIDITY_COEFF, counter, [0,0,0,0,0,0,0,0])
    print("boxes "+str(len(boxes)))
    if len(boxes)>2:
        A, c1, c2, b1, b2 = compare(boxes)
        geometry_options = {"tmargin": "1cm", "lmargin": "10cm"}
        #doc = Document(geometry_options=geometry_options)

        print("It should be creating the thing")
        #with doc.create(Section('Matrix Equation')):
         #   with doc.create(Subsection('Correct matrix equations')):
          #      doc.append(Math(data=[Matrix(c2), "=", Matrix(A), '(', Matrix(c1), "-", Matrix(b1), "+", Matrix(b2)]))
        #doc.generate_pdf(compiler='pdflatex')
        ''' I dont know what this does, I don't think we need it? I'm not sure. We'll see if stuff breaks...
        np.savetxt('compare.txt',c2,fmt='%.2f')
        np.savetxt('compare.txt',A,fmt='%.2f')
        np.savetxt('compare.txt',c1,fmt='%.2f')
        np.savetxt('compare.txt',b1,fmt='%.2f')
        np.savetxt('compare.txt',b2,fmt='%.2f')
        '''
        return render_template("compare.html", list = [A,c1,c2,b1,b2])
        
    #for filename in os.listdir(directory):
    #    if filename == "compare.txt":
    #        file = open(directory+"//"+filename, "r")
    #        lines = file.readlines()
    #        A, c1, c2, b1, b2 = compare(lines)
    #   else:
    #       continue
    plots=[]
    shit = "\\templates\\test\\output\\"
    for file in os.listdir(directory + "\\static\\"):
        os.remove(directory + "\\static\\"+file)
    #for file in os.listdir(directory + "\\data\\"):
    #   os.remove(directory + "\\data\\"+file)
    for file in os.listdir(directory + shit):
        plots.append(file)
        shutil.move(directory+shit+file, directory+"\\static\\")
    with app.app_context():
        return render_template('resolution.html', list=plots)
#        return render_template('file:///C:/Users/Administrator/NPRreporting/Costidity/NPRCube/templates/test/output/', list=plots)
    

def difference(lst1, lst2):
    return list(set(lst1) - set(lst2))
 
def formatter(dirP):
    data = pd.read_csv(dirP, skiprows=2)
    data = data.drop(0)
    data['RequestID'] = data['RequestID'].astype(int)
    data['Need'] = data['Need'].astype(int)
    data['Policy'] = data['Policy'].astype(int)
    data['Result'] = data['Result'].astype(int)
    data['PersonID'] = data['PersonID'].astype(int)
    data['EntitlementID'] = data['EntitlementID'].astype(int)
    return data

def plot(file_path, file):
    f = open("demofile2.txt", "a")
    filenames = []
    username=session['username']
    for filename in os.listdir(directory + '\\data\\' + username):
        #if filename.endswith(".csv"):
        print ('3')
        print (filename)
        print (file)
        print ('3')
        if filename == file:
            print('2')
            print (filename)
            print (file)
            print ('2')
            filenames.append(os.path.join("", filename))
            f.write(filename+"\n")
        else:
            continue
    f.close()
    plt.rc('axes', labelsize=LABELSIZE) 
    plt.rc('xtick', labelsize=5)
    counter = [0,0,0,0,0,0,0,0]
    altc = [0,0,0,0,0,0,0,0]
   # username=session['username']
    print ('1')
    print (filenames)
    print ('1')
    dirP = directory + '\\data\\' + username + '\\' + filenames[0]
    data = formatter(dirP)
    for index, row in data.iterrows():
        counter[(7-(row[4]*4+row[5]*2+row[6]))]+=1
        if row[1]==0:
            altc[(7-(row[4]*4+row[5]*2+row[6]))]+=1
    
    tot1 = 0
    tot2 = 0
    for i in range(len(counter)):
        tot1+=counter[i]
        tot2+=altc[i]
    counter.append(tot1)
    altc.append(tot2)
    maximum = tot1
    boolean = True
    c=1
    while boolean:
        maximum = maximum//10
        c*=10
        if maximum<10:
            boolean = False
    maximum = tot1 + c

    filenames[0] = filenames[0].replace('.csv', '')
    labels = [OCTANT_ONE, OCTANT_TWO, OCTANT_THREE, OCTANT_FOUR, OCTANT_FIVE, OCTANT_SIX, OCTANT_SEVEN, OCTANT_EIGHT, "Total"]
    plotter(X_AXIS, Y_AXIS_NUM, TITLE, counter, labels, maximum, [OCTANT_ONE_COLOR, OCTANT_TWO_COLOR, OCTANT_THREE_COLOR, OCTANT_FOUR_COLOR, OCTANT_FIVE_COLOR, OCTANT_SIX_COLOR, OCTANT_SEVEN_COLOR, OCTANT_EIGHT_COLOR, "black"], filenames[0]+'Amount' )
    maximum = tot2
    boolean = True
    c=1
    while boolean:
        maximum = maximum//10
        c*=10
        if maximum<10:
            boolean = False
    maximum = tot2 + c
    plotter(X_AXIS, Y_AXIS_NUM, TITLE, altc, labels, maximum, [OCTANT_ONE_COLOR, OCTANT_TWO_COLOR, OCTANT_THREE_COLOR, OCTANT_FOUR_COLOR, OCTANT_FIVE_COLOR, OCTANT_SIX_COLOR, OCTANT_SEVEN_COLOR, OCTANT_EIGHT_COLOR, "black"], 'Amount_Modify' )
    return counter, altc

def plotter(x, y, tit, counter, labels, maximum, color, output):
    fig, ax = plt.subplots()    
    plt.title(tit, fontsize = 15)
    #ax.hist(x, n_bins, density=True, histtype='bar', color=colors, label=colors)
    ax.bar(labels, counter, width=0.9, color = color)
    plt.ylim(0,maximum)
    plt.xlabel(x, color = X_COLOR)
    plt.ylabel(y, color = Y_COLOR)
    for rect in ax.patches:
        height = rect.get_height()
        ax.annotate(f'{int(height)}', xy=(rect.get_x()+rect.get_width()/2, height), 
                xytext=(0, 5), textcoords='offset points', ha='center', va='bottom', color="blue", fontsize = 8)

    plt.tight_layout()
    plt.plot()
    plt.savefig(directory + '//templates//test//output//' + output+".svg")
    
def plotmoney(constant, constarr, counter, money):
    total = 0
    labels = [OCTANT_ONE, OCTANT_TWO, OCTANT_THREE, OCTANT_FOUR, OCTANT_FIVE, OCTANT_SIX, OCTANT_SEVEN, OCTANT_EIGHT, "Total"]
    for i in range(len(counter)-1):
        money[i] = constant*(constarr[i]-1)*counter[i]
        total+=constant*(constarr[i]-1)*counter[i]
    money.append(total)
    maximum = total
    boolean = True
    c=1
    while boolean:
        maximum = maximum//10
        c*=10
        if maximum<10:
            boolean = False
    maximum = total + c
    plotter(X_AXIS, Y_AXIS_MON, "Money Lost", money, labels, maximum, [OCTANT_ONE_COLOR, OCTANT_TWO_COLOR, OCTANT_THREE_COLOR, OCTANT_FOUR_COLOR, OCTANT_FIVE_COLOR, OCTANT_SIX_COLOR, OCTANT_SEVEN_COLOR, OCTANT_EIGHT_COLOR, "black"], 'MoneyLost' )
    
def compare(lines):
    lines[0] = lines[0].replace("\n", "")
    dirP1 = directory + "\\data\\" +lines[0]
    dirP2 = directory + "\\data\\" +lines[1]
    data1 = formatter(dirP1)
    data2 = formatter(dirP2)
    l1 = LinkedList()
    l2 = LinkedList()
    l3 = LinkedList()
    log = ""
    c1 = [0,0,0,0,0,0,0,0]
    c2 = [0,0,0,0,0,0,0,0]
    for index, row in data1.iterrows():
        l1.add(User(row[2], row[3],(8-(row[4]*4+row[5]*2+row[6]))))
        c1[(7-(row[4]*4+row[5]*2+row[6]))]+=1
    for index, row in data2.iterrows():
        l2.add(User(row[2], row[3],(8-(row[4]*4+row[5]*2+row[6]))))
        c2[(7-(row[4]*4+row[5]*2+row[6]))]+=1
    
    A = np.zeros((8,8))
    for i in l1:
        for j in l2:
            if (i.val.compare(j.val)==2):
                l1, l2, l3 = simplemethod(l1,l2, l3, i, j)
                A[j.val.octn-1, i.val.octn-1] += 1
            elif (i.val.compare(j.val)==1):
                log += str(i.val.octn) + "->" + str(j.val.octn) +"\n"
                l1, l2, l3 = simplemethod(l1,l2, l3, i, j)
                A[j.val.octn-1, i.val.octn-1] += 1
    b1 = np.array(l1.toVector(8))
    b2 = np.array(l2.toVector(8)) 
    c1 = np.array(c1)
    c2 = np.array(c2)
    common = np.array(l3.toVector(8))
    for i in range(8):
        if (c1-b1)[i] !=0:
            A[:,i] = A[:,i]/(c1-b1)[i]
    
    
    print('common')
    print(common)
    print('c')
    print(c1)
    print(c2)
    print('b')
    print(b1)
    print(b2)
    print("Answer")
    print(c2)
    print(A@c1 - A@b1 +b2)
    print()
    print(A)
    #(c2) = A(c1-b1)+b2
    print(log)
    return A, c1, c2, b1, b2
    
def simplemethod(l1, l2, l3, i, j):
    if (l2.head.val.compare(j.val)==2):
        if (j.next == None):
            l2.head = None
            l2.tail = None
            if (l1.head.val.compare(i.val)==2):
                if (i.next == None):
                    l1.head = None
                    l1.tail = None
                else:
                    l1.head = i.next
                    i.next.prev = None
            elif (l1.tail.val.compare(i.val)==2):
                l1.tail = i.prev
                i.prev.next = None
            else:
                i.prev.next = i.next
                i.next.prev = i.prev
        else: 
            l2.head = j.next
            j.next.prev = None
            l3.add(i.val)
            if (l1.head.val.compare(i.val)==2):
                    if (i.next == None):
                        l1.head = None
                        l1.tail = None
                    else:
                        l1.head = i.next
                        i.next.prev = None
            elif (l1.tail.val.compare(i.val)==2):
                l1.tail = i.prev
                i.prev.next = None
            else:
                i.prev.next = i.next
                i.next.prev = i.prev        
    elif (l2.tail.val.compare(j.val)==2):
        l2.tail = j.prev
        j.prev.next = None
        l3.add(i.val)
        if (l1.head.val.compare(i.val)==2):
            if (i.next == None):
                l1.head = None
                l1.tail = None
            else:
                l1.head = i.next
                i.next.prev = None
        elif (l1.tail.val.compare(i.val)==2):
            l1.tail = i.prev
            i.prev.next = None
        else:
            i.prev.next = i.next
            i.next.prev = i.prev      
    else:
        j.prev.next = j.next
        j.next.prev = j.prev
        l3.add(i.val)
        if (l1.head.val.compare(i.val)==2):
            if (i.next == None):
                print("fuckup1")
            else:
                l1.head = i.next
                i.next.prev = None
        elif (l1.tail.val.compare(i.val)==2):
            l1.tail = i.prev
            i.prev.next = None
        else:
            i.prev.next = i.next
            i.next.prev = i.prev
    return l1, l2, l3    
    
#main("Mockup_data_June1.csv")
