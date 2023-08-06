from collections import defaultdict
from queue import PriorityQueue
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
    def __init__(self, name, par=None, g=0):
        self.name = name
        self.par = par
        self.g = g


    def __lt__(self, other):
        if(other == None):
            return False
        return self.g < other.g 

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




def RUN(S=Node(name='25'), G=Node(name='1')):
    global chiphi
    Open = PriorityQueue()
    Close = PriorityQueue()
    Open.put(S)
    while True:
        if(Open.empty() == True):
            print("Tìm kiếm thất bại")
            return False
        O = Open.get()
        Close.put(O)
        print("Duyet: ", O.name, O.g)
        state.append(int(O.name))
        if(Sosanhbang(O, G) == True):
            print("Tìm kiếm thành công")
            DuongDi(O)
            print("Chi phí: ", (O.g))
            chiphi = O.g
            return True
        i = 0
        while i < len(data[O.name]):
            name = data[O.name][i]  # đỉnh ở chỉ số chẳn
            node_tmp = Node(name=name) # tạo node tmp
            vt1 = KiemTraTonTai(node_tmp, Open) #kiem tra co trong Open
            vt2 = KiemTraTonTai(node_tmp, Close) #kiem tra co trong Close
            if(vt2 == -1 and vt2 != None): # khong co trong close
                if( vt1 == -1 and vt1 != None): #  khong co trong open
                    node_tmp.g = O.g + data[O.name][i+1]
                    node_tmp.par = O
                    Open.put(node_tmp)
                elif(Open.queue[vt1].g > O.g + data[O.name][i+1]): # co trong Open kiem tra g
                    Open.queue.remove(node_tmp) # Xoá node_tmp trong Open
                    node_tmp.g = O.g + data[O.name][i+1]
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
