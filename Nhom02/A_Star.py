from collections import defaultdict
from queue import PriorityQueue
import math
import time

# list lưu các đỉnh duyệt qua ép kiểu về int
state = []
# list lưu đường đi theo tên đỉnh ép kiểu về int
path = []
chiphi = 0

Todo = []
data = defaultdict(list)
def DocToaDo(path):
    with open(path, 'r') as fdatamap:
        line = fdatamap.readline()
        for i in range(int(line)):
            temp = []
            line = fdatamap.readline().split()
            for item in line:
                temp.append(int(item))
            Todo.append(temp)

def DocTrongSo(path):
    with open(path, 'r') as ftrongso:
        line = ftrongso.readline()
        for i in range(int(line)):
            temp =[]
            line = ftrongso.readline().split()
            dinh = line.pop(0)
            for item in range(len(line)):
                if(item % 2 == 0):
                    temp.append(line[item])
                else:
                    temp.append(float(line[item]))
            data[dinh] = temp


class Node:
    def __init__(self, name, par=None, g=0, h=0):
        self.name = name
        self.par = par
        self.g = g
        self.h = h

    def __lt__(self, other):
        if(other == None):
            return False
        return self.g + self.h < other.g + other.h

    def __eq__(self, other):
        if(other == None):
            return False
        return self.name == other.name


def Sosanhbang(O, G):
    if(O == G):
        return True
    return False


def KiemTraTonTai(tmp, c):
    if(tmp == None):
        return None
    for i in range(c.qsize()):
        if(tmp == c.queue[i]):
            return i
    return -1


def DuongDi(O):
    if(O.par != None):
        DuongDi(O.par)
    print(O.name)
    path.append(int(O.name))


def HX(X, G):
    # tất cả trừ 1 vì index trong list Todo bắt đầu từ 0
    vitriX = int(X) - 1  # số thứ tự theo đỉnh của nút hiện tại
    vitriG = int(G) - 1  # số thứ tự theo đỉnh của nút goal
    ###
    vitriX_x = Todo[vitriX][0]
    vitriX_y = Todo[vitriX][1]
    vitriG_x = Todo[vitriG][0]
    vitriG_y = Todo[vitriG][1]
    # tính khoảng cách theo đường chim bay dùng định lý pytago 2^3 = 2**3
    return math.sqrt((vitriX_x - vitriG_x)**2 + (vitriX_y - vitriG_y)**2)


def RUN(S=Node(name='25'), G=Node(name='1')):
    global chiphi
    Open = PriorityQueue()
    Close = PriorityQueue()
    S.h = HX(S.name, G.name)
    Open.put(S)
    while True:
        if(Open.empty() == True):
            print("Tìm kiếm thất bại")
            return False
        O = Open.get()
        Close.put(O)
        print("Duyet: ", O.name, O.g, O.h)
        state.append(int(O.name))
        if(Sosanhbang(O, G) == True):
            print("Tìm kiếm thành công")
            DuongDi(O)
            print("Chi Phí: ", (O.g))
            chiphi = O.g
            return True
        i = 0
        while i < len(data[O.name]):
            name = data[O.name][i]  # đỉnh ở chỉ số chẳn
            node_tmp = Node(name=name) # tao node tmp
            vt1 = KiemTraTonTai(node_tmp, Open) # kiem tra co trong Open
            vt2 = KiemTraTonTai(node_tmp, Close) # kiem tra co trong close
            if(vt2 == -1 and vt2 != None):# khong co trong close
                if(vt1 == -1 and vt1 != None): # khong co trong open
                    node_tmp.g = O.g + data[O.name][i+1]
                    node_tmp.h = HX(node_tmp.name, G.name)
                    node_tmp.par = O
                    Open.put(node_tmp)
                elif(Open.queue[vt1].g > O.g + data[O.name][i+1]): #co trong open
                    Open.queue.remove(node_tmp) # Xoá node_tmp trong Open
                    node_tmp.g = O.g + data[O.name][i+1]
                    node_tmp.h = HX(node_tmp.name, G.name)
                    node_tmp.par = O
                    Open.put(node_tmp)
            i += 2


if __name__ == "__main__":
    DocToaDo(r'./data/ToaDo_Map1.txt')
    DocTrongSo(r'./data/TrongSo_Map1.txt')
    t1 = time.time()
    RUN()
    t2 = time.time()
    print(t2-t1)
    print(path)
    print(state)
