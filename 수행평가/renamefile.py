import tkinter as tk
import csv
import os

win=tk.Tk()
win.title("프로그램")

def find():
    def find_get():
        global filepath
        global filenames
        filepath=Find_input.get()       #파일 경로를 Find_input으로 부터 받음
        filenames=os.listdir(filepath)  #filename에 list 형태로 파일 이름을 읽어옴
        print(filenames)
    def find_changefile():            #반복문을 사용하여 파일 이름을 수정
        for name in filenames:
            for j in datalist:
                if j[0]==name:
                    file_oldname=os.path.join(filepath,name)
                    file_newname_newfile = os.path.join(filepath, j[1])
                    os.rename(file_oldname, file_newname_newfile)
    Find=tk.Tk()
    Find_name=tk.Label(Find,text="경로를 입력해주세요").pack()
    Find_input=tk.Entry(Find,width=30)
    Find_input.pack()
    Find_ok=tk.Button(Find,text="확인",command=find_get).pack()
    Find_open=tk.Button(Find,text="파일 이름바꾸기",command=find_changefile).pack()

def make_list():
    def make_get():
        filepath=make_entry.get()
        filenames=os.listdir(filepath)
        
        k=0
        for i in filenames:                  #읽어온 filenames 를 통해 datalist를 수정
            k+=1
            datalist[k][0]=i
        print(datalist)

        g=open("list.csv","w",newline='')              #수정된 datalist를 통해 csv파일을 재생성한다.
        writer=csv.writer(g)
        for i in datalist:
            print(i)
            writer.writerow(i)
        g.close()

    Make=tk.Tk()
    make_entry=tk.Entry(Make)
    make_entry.pack()
    make_ok=tk.Button(Make,text="확인",command=make_get).pack()
 
def help():
    Help=tk.Tk()
    Help_help=tk.Label(Help,text="같은 파일에 들어있는 엑셀파일에서 첫번째 줄에 정확한 이름을 입력하고 2번째 줄에는 바꿀 이름을 입력하여 저장해주세요")
    Help_help.pack()

global filepath
global filenames

f=open("list.csv")
global datalist
datalist=[]
data=csv.reader(f)

for i in data:  #datalist에 [[원래이름],[바꿀 이름]] 형태로 csv를 받아옴
    a=[]
    a.append(i[0])
    a.append(i[1])
    datalist.append(a)
print(datalist)

f.close()

win_find=tk.Button(win,text="파일이름 바꾸기",command=find)
win_find.pack()

win_make_list=tk.Button(win,text="파일 엑셀 만들기",command=make_list)
win_make_list.pack()

win_setting=tk.Button(win,text="도움말",command=help)
win_setting.pack()
