from tkinter import *

import A_Star as Asao
from tkinter import messagebox
import time
import UCS

luachon = 0 # 0 chua chon map, 1 chon map A, 2 chon ma
class GiaoDien(Tk):
    def __init__(self):
        super().__init__()
        self.resizable(0, 0)  # disable min/max
        # Lấy chiều rộng của màn hình
        widthdisplay = self.winfo_screenwidth()
        x = int(widthdisplay/2-1200/2)
        self.title("Tìm đường trên bản đồ giao thông - Nhóm 02")
        # Hiện cửa xổ
        self.geometry("1200x680+{}+{}".format(x, 0))
        self.configure(background='#49A')
        # Load logo
        self.iconbitmap("./resources/icon_maps.ico")
        # Tạo canvas
        self.canva = Canvas(self, width=1001, height=583)
        # Đặt canvas
        self.canva.place(x=0, y=100)
        # load image. Note khai bao self de cho khi xoa rac tk khong xoa luon anh ==> luon giu tham chieu den anh
        self.img_bg1 = PhotoImage(file="./resources/MapA.png")
        # image map trong so
        self.img_ts1 = PhotoImage(file="./resources/MapA_TS.png")
        self.img_bg2 = PhotoImage(file="./resources/MapB.png")
        # image map trong so
        self.img_ts2 = PhotoImage(file="./resources/MapB_TS.png")
        # image BD va KT
        self.img_bd = PhotoImage(file="./resources/BatDau.png")
        self.img_kt = PhotoImage(file="./resources/KetThuc.png")
        # Su kien nhan chuot trai
        self.canva.bind('<Button-1>', self.draw_location)
        # Luu dinh dau va cuoi
        self.locate = []
        # Tạo canva tieu de
        self.canvaTD = Canvas(self, width=1001, height=100)
        self.canvaTD.place(x=0, y=0)
        # tao label tieu de
        nd = "Phần Mềm Tìm Đường Đi Trên Bản Đồ Giao Thông Dùng Thuật Toán A-Star và Uniform Cost Search"
        self.Tieu_de = self.canvaTD.create_text(
            1000, 15, text=nd, font=("Helvetica", 15), anchor=NW, fill="#d22089")
        ten = "Huỳnh Thanh Tuấn 20110120 - Nguyễn Thành Đạt 20110121 - Phan Hồng Sơn 20110560"
        self.TacGiac = self.canvaTD.create_text(
            20, 60, text=ten, font=("Helvetica", 15), anchor=NW, fill="blue")
        self.DiChuyen()
        # Tao button tim duong A star
        self.bt_MapA = Button(self, text='Map A', font=(
            'Showcard Gothic', 14), fg='blue', command = lambda:self.Kichhoat(1), background="#856ff8")
        self.bt_MapA.place(x=1020, y=100)
        # Tao button tim duong UCS
        self.bt_MapB = Button(self, text='Map B', font=(
            'Showcard Gothic', 14), fg='gold', command=lambda:self.Kichhoat(2), background="#856ff8")
        self.bt_MapB.place(x=1120, y=100)
         # Tao button tim duong A star
        self.bt_timduong_Star = Button(self, text='A Star', font=(
            'Showcard Gothic', 14), fg='Lavender', command=self.draw_path_Astar, background="#856ff8")
        self.bt_timduong_Star.place(x=1020, y=175)
        # Tao button tim duong UCS
        self.bt_timduong_UCS = Button(self, text='UCS', font=(
            'Showcard Gothic', 14), fg='SKY BLUE', command=self.draw_path_UCS, background="#856ff8")
        self.bt_timduong_UCS.place(x=1135, y=175)
        # Tao button reload
        self.bt_reload = Button(self, text="Reload", font=(
            'Showcard Gothic', 14), fg='Plum', background="#856ff8", command=self.Reload)
        self.bt_reload.place(x=1055, y=250)
        # Tao button thoat chuong trinh
        bt_exit = Button(self, text='Exit', font=(
            'Showcard Gothic', 14), fg='lime', command=self.destroy, background="#856ff8")
        bt_exit.place(x=1130, y=540)
        # tao label Tieu de time
        self.label_Tieude_time = Label(
            self, text="Thời Gian Tìm\nKiếm", fg='Orange', font=("Showcard Gothic", 15), background="#49A")
        self.label_Tieude_time.place(x=1030, y=300)
        # tao label thoi gian
        self.label_Time = Label(
            self, text="", font=("Helvetica", 15), background="#49A")
        # An lable
        self.label_Time.place_forget()
        self.label_Time.place(x=1040, y=350)
        # Tao lable so dinh duyet qua
        self.label_Tieude_Duyet = Label(
            self, text="Số đỉnh đã duyệt", fg='light blue', font=("Showcard Gothic", 15), background="#49A")
        self.label_Tieude_Duyet.place(x=1020, y=375)
        # tao label Duyet
        self.label_Duyet = Label(
            self, text="",  font=("Helvetica", 15), background="#49A")
        # An lable
        self.label_Duyet.place_forget()
        self.label_Tieude_Chiphi = Label(
            self, text="Chi Phí", fg='yellow', font=("Showcard Gothic", 15), background="#49A")
        self.label_Tieude_Chiphi.place(x=1060, y=430)
        # tao label ChiPhi
        self.label_Chiphi = Label(
            self, text="",  font=("Helvetica", 15), background="#49A")
        # An lable
        self.label_Chiphi.place_forget()
        messagebox.showinfo('Hướng dẫn sử dụng', 'Hãy chọn map A hoặc B bên góc phải trên của chương trình')

    def Kichhoat(self, check):
        global luachon
        luachon = check
        if(check == 1):
            Asao.DocToaDo(r'./data/ToaDo_Map1.txt')
            Asao.DocTrongSo(r'./data/TrongSo_Map1.txt')
            UCS.DocToaDo(r'./data/ToaDo_Map1.txt')
            UCS.DocTrongSo(r'./data/TrongSo_Map1.txt')
            self.canva.create_image(0, 0, anchor=NW, image=self.img_bg1)
        elif(check == 2):
            Asao.DocToaDo(r'./data/ToaDo_Map2.txt')
            Asao.DocTrongSo(r'./data/TrongSo_Map2.txt')
            UCS.DocToaDo(r'./data/ToaDo_Map2.txt')
            UCS.DocTrongSo(r'./data/TrongSo_Map2.txt')
            self.canva.create_image(0, 0, anchor=NW, image=self.img_bg2)
        self.bt_MapA['state'] = DISABLED
        self.bt_MapB['state'] = DISABLED
    def DiChuyen(self):
        x1, y1, x2, y2 = self.canvaTD.bbox(self.Tieu_de)
        if(x2 < 5):
            x1 = 1000
            y1 = 15
            # Di chuyen Tieu de den vi tri x1, y1
            self.canvaTD.coords(self.Tieu_de, x1, y1)
        else:
            # di chuyen Tieu de moi lan x se tru 2 va y giu nguyen
            self.canvaTD.move(self.Tieu_de, -2, 0)
        # sau 20 miligiay thi goi lai DiChuyen
        self.canvaTD.after(20, self.DiChuyen)

    def draw_location(self, event):
        global temp
        if(temp == 2  or luachon == 0):
            return
        x = event.x
        y = event.y
        for i in range(len(Asao.Todo)):
            temx = Asao.Todo[i][0]
            temy = Asao.Todo[i][1]
            if(x >= temx-10) and (x <= temx + 10 and (y >= temy - 8) and (y <= temy + 8)):
                print("lick vào số {}".format(i+1))
                # them vi tri bat dau va ket thuc vao
                self.locate.append(str(i+1))
                # ve dia diem bat dau va ket thuc
                if(temp == 0):
                    self.canva.create_image(
                        temx-24, temy - 48, anchor=NW, image=self.img_bd)
                elif(temp == 1):
                    self.canva.create_image(
                        temx-24, temy - 48, anchor=NW, image=self.img_kt)
                temp += 1
                return
        messagebox.showwarning(
            "Chọn Lại", "Hay click chuột vào giữa các vị trí đánh số đã tô màu!!!")

    def check_TonTai(self, x, ThuatToan):  # thuattoan = 1 Asao, thuattoan != 1 UCS
        tem = Asao.path
        if ThuatToan != 1:
            tem = UCS.path
        for item in tem:
            if(item == x):  # ton tai
                return True
        return False  # khong ton tai

    def draw_path_Astar(self):
        if temp == 2:
            self.bt_timduong_UCS['state'] = DISABLED
            self.bt_timduong_Star['state'] = DISABLED
            t1 = time.time()
            check = Asao.RUN(S=Asao.Node(name=self.locate[0]), G=Asao.Node(
                name=self.locate[1]))
            t2 = time.time()
            if(check == False):
                messagebox.showinfo(
                    "Thông báo", "Không tìm thấy được đường đi!!!")
                return
            # Thoi gian
            self.label_Time['text'] = str(round((t2-t1), 6))+" giây"
            self.label_Time.place(x=1040, y=350)
            # So luong duyet
            self.label_Duyet['text'] = str(len(Asao.state))
            self.label_Duyet.place(x=1085, y=400)
            # Chi phi
            self.label_Chiphi['text'] = str(Asao.chiphi)
            self.label_Chiphi.place(x=1085, y=455)
            # ve lai nen co trong so
            if(luachon == 1):
                self.canva.create_image(0, 0, anchor=NW, image=self.img_ts1)
            elif(luachon == 2):
                self.canva.create_image(0, 0, anchor=NW, image=self.img_ts2)
            # ve lai toa do dinh dau va cuoi
            # locate luu ten dinh bat dau tu 1 kieu du lieu string
            self.canva.create_image(
                Asao.Todo[int(self.locate[0]) - 1][0]-24, Asao.Todo[int(self.locate[0]) - 1][1] - 48, anchor=NW, image=self.img_bd)
            self.canva.create_image(
                Asao.Todo[int(self.locate[1]) - 1][0]-24, Asao.Todo[int(self.locate[1]) - 1][1] - 48, anchor=NW, image=self.img_kt)
            # tô các đỉnh duyệt
            j = 0
            while j < len(Asao.state):
                x1 = Asao.Todo[Asao.state[j]-1][0] - 10
                y1 = Asao.Todo[Asao.state[j]-1][1] - 8
                x2 = Asao.Todo[Asao.state[j]-1][0] + 10
                y2 = Asao.Todo[Asao.state[j]-1][1] + 8
                if(self.check_TonTai(Asao.state[j], 1) == True):
                    self.canva.create_oval(x1, y1, x2, y2,
                                           fill="red")
                else:
                    self.canva.create_oval(x1, y1, x2, y2,
                                           fill="blue")
                self.canva.after(100)
                self.canva.update()
                j += 1
            # Vẽ đường đi
            i = 0
            while i < len(Asao.path)-1:
                time.sleep(0.05)
                x1 = Asao.Todo[Asao.path[i]-1][0]
                y1 = Asao.Todo[Asao.path[i]-1][1]
                x2 = Asao.Todo[Asao.path[i+1]-1][0]
                y2 = Asao.Todo[Asao.path[i+1]-1][1]
                self.canva.create_line(
                    x1, y1, x2, y2, fill="#26e009", width=3, arrow=LAST)
                self.canva.after(300)
                self.canva.update()
                i += 1

    def draw_path_UCS(self):
        if temp == 2:
            self.bt_timduong_Star['state'] = DISABLED
            self.bt_timduong_UCS['state'] = DISABLED
            t1 = time.time()
            check = UCS.RUN(S=UCS.Node(name=self.locate[0]), G=UCS.Node(
                name=self.locate[1]))
            t2 = time.time()
            if(check == False):
                messagebox.showinfo(
                    "Thông báo", "Không tìm thấy được đường đi!!!")
                return
            # Thoi gian
            self.label_Time['text'] = str(round((t2-t1), 6))+" giây" #lay 6 so sao dau phay
            self.label_Time.place(x=1040, y=350)
            # So luong duyet
            self.label_Duyet['text'] = str(len(UCS.state))
            self.label_Duyet.place(x=1085, y=400)
            # Chi phi
            self.label_Chiphi['text'] = str(UCS.chiphi)
            self.label_Chiphi.place(x=1085, y=455)
            if(luachon == 1):
                self.canva.create_image(0, 0, anchor=NW, image=self.img_ts1)
            elif(luachon == 2):
                self.canva.create_image(0, 0, anchor=NW, image=self.img_ts2)
            # ve lai toa do dinh dau va cuoi
            # locate luu ten dinh bat dau tu 1 kieu du lieu string
            self.canva.create_image(
                UCS.Todo[int(self.locate[0]) - 1][0]-24, UCS.Todo[int(self.locate[0]) - 1][1] - 48, anchor=NW, image=self.img_bd)
            self.canva.create_image(
                UCS.Todo[int(self.locate[1]) - 1][0]-24, UCS.Todo[int(self.locate[1]) - 1][1] - 48, anchor=NW, image=self.img_kt)
            # tô các đỉnh duyệt
            j = 0
            while j < len(UCS.state):
                x1 = UCS.Todo[UCS.state[j]-1][0] - 10
                y1 = UCS.Todo[UCS.state[j]-1][1] - 8
                x2 = UCS.Todo[UCS.state[j]-1][0] + 10
                y2 = UCS.Todo[UCS.state[j]-1][1] + 8
                if(self.check_TonTai(UCS.state[j], 2) == True):
                    self.canva.create_oval(x1, y1, x2, y2,
                                           fill="red")
                else:
                    self.canva.create_oval(x1, y1, x2, y2,
                                           fill="blue")
                self.canva.after(100)
                self.canva.update()
                j += 1
             # Vẽ đường đi
            i = 0
            while i < len(UCS.path)-1:
                x1 = UCS.Todo[UCS.path[i]-1][0]
                y1 = UCS.Todo[UCS.path[i]-1][1]
                x2 = UCS.Todo[UCS.path[i+1]-1][0]
                y2 = UCS.Todo[UCS.path[i+1]-1][1]
                self.canva.create_line(
                    x1, y1, x2, y2, fill="#26e009", width=3, arrow=LAST)
                self.canva.after(300)
                self.canva.update()
                i += 1

    def Reload(self):
        global luachon
        luachon = 0
        self.bt_timduong_UCS['state'] = NORMAL
        self.bt_timduong_Star['state'] = NORMAL
        self.bt_MapA['state'] = NORMAL
        self.bt_MapB['state'] = NORMAL
        self.label_Time.place_forget()
        self.label_Duyet.place_forget()
        self.label_Chiphi.place_forget()
        global temp  # khai bao de chinh sua gia tri bien temp
        temp = 0
        # xoa
        self.canva.delete('all')
        # reset ten diem dau va cuoi
        self.locate = []
        # reset
        Asao.state = []
        Asao.path = []
        UCS.state = []
        UCS.path = []
        Asao.Todo = []
        Asao.data.clear()
        UCS.Todo = []
        UCS.data.clear()


if __name__ == "__main__":
    temp = 0
    App = GiaoDien()
    App.mainloop()
