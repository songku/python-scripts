# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


  #      def print_hi(name):
            # Use a breakpoint in the code line below to debug your script.
   #         print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


        # Press the green button in the gutter to run the script.
#        if __name__ == '__main__':
 #           print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from random import  random
def printInfo():
    print("这是一个A与B的体育竞技比赛")
    print("程序运行需要A与B的能力值(以0到1之间的小数表示)")

def inputInfo():
    a=eval(input("请输入A的能力值{0-1}: "))
    b=eval(input("请输入B的能力值{0-1}: "))
    n=eval(input("请输入比赛次数: "))
    return  a,b,n

def gameOver(a,b):
    return a == 15 or b == 15
def simOnegame(a,b):
    scoreA,scoreB=0,0
    serving="A"
    while not gameOver(scoreA,scoreB):
        if serving == "A":
            if random()<a:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < b:
                scoreB += 1
            else:
                serving="A"
    return scoreA,scoreB

def simNgames(a,b,n):
    wina,winb=0,0
    for i in range(n):
        scorea, scoreb = simOnegame(a,b)
        if scorea>scoreb:
            wina += 1
        else:
            winb += 1
    return wina,winb

def printWin(wa,wb):
        n=wa+wb
        print("共统计比赛次数为{}".format(n))
        print("A共赢得比赛次数为{}，其胜率为{:0.1%}".format(wa, wa/n))
        print("B共赢得比赛次数为{}，其胜率为{:0.1%}".format(wb, wb/n))

if __name__=='__main__':
    printInfo()
    pa, pb, n=inputInfo()
    wa, wb = simNgames(pa, pb, n)
    printWin(wa, wb)