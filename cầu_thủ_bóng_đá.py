from guizero import App, Box, Text, Picture

app = App("Danh sách học sinh", width=700, height=400, bg="white")

main_box = Box(app, layout="grid")


Text(main_box, text="DANH SÁCH HỌC SINH", size=16, grid=[0,0], align="left")


Text(main_box, text="Ảnh", grid=[0,1])
Text(main_box, text="Tên", grid=[1,1])
Text(main_box, text="Tuổi", grid=[2,1])
Text(main_box, text="Trường", grid=[3,1])
Text(main_box, text="Lớp", grid=[4,1])
Text(main_box, text="Giới tính", grid=[5,1])
Text(main_box, text="Sở thích", grid=[6,1])


Picture(main_box, image="an.png", grid=[0,2], width=60, height=60)
Text(main_box, text="An", grid=[1,2])
Text(main_box, text="11", grid=[2,2])
Text(main_box, text="THCS Lý Thái Tổ", grid=[3,2])
Text(main_box, text="6.6", grid=[4,2])
Text(main_box, text="Nữ", grid=[5,2])
Text(main_box, text="Vẽ tranh", grid=[6,2])


Picture(main_box, image="tran.png", grid=[0,3], width=60, height=60)
Text(main_box, text="Trân", grid=[1,3])
Text(main_box, text="11", grid=[2,3])
Text(main_box, text="THCS Lý Thái Tổ", grid=[3,3])
Text(main_box, text="6.4", grid=[4,3])
Text(main_box, text="Nữ", grid=[5,3])
Text(main_box, text="Chơi game", grid=[6,3])


Picture(main_box, image="bich.png", grid=[0,4], width=60, height=60)
Text(main_box, text="Bích", grid=[1,4])
Text(main_box, text="11", grid=[2,4])
Text(main_box, text="THCS Lý Thái Tổ", grid=[3,4])
Text(main_box, text="6.2", grid=[4,4])
Text(main_box, text="Nữ", grid=[5,4])
Text(main_box, text="Đọc sách", grid=[6,4])

app.display()
