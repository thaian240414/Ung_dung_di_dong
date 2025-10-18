from guizero import App, Box, Text, Picture

app = App("Album cầu thủ bóng đá nổi tiếng", width=700, height=450, bg="white")

main_box = Box(app, layout="grid")

title_box = Box(main_box, border=True, width=660, height=50, grid=[0,0,3,1])
title_text = Text(title_box, text="ALBUM CẦU THỦ BÓNG ĐÁ NỔI TIẾNG", size=14)

box1 = Box(main_box, border=True, width=220, height=120, grid=[0,1])
picture1 = Picture(box1, image="ms.png", width=100, height=100)

box2 = Box(main_box, border=True, width=220, height=120, grid=[1,1])
picture2 = Picture(box2, image="ronaldo.png", width=100, height=100)

box3 = Box(main_box, border=True, width=220, height=120, grid=[2,1])
picture3 = Picture(box3, image="mbappe.png", width=100, height=100)

box4 = Box(main_box, border=True, width=220, height=50, grid=[0,2])
text4 = Text(box4, text="Messi")
box5 = Box(main_box, border=True, width=220, height=50, grid=[1,2])
text5 = Text(box5, text="Ronaldo")
box6 = Box(main_box, border=True, width=220, height=50, grid=[2,2])
text6 = Text(box6, text="Mbappe")

box7 = Box(main_box, border=True, width=220, height=50, grid=[0,3])
text7 = Text(box7, text="Argentina")
box8 = Box(main_box, border=True, width=220, height=50, grid=[1,3])
text8 = Text(box8, text="Bồ Đào Nha")
box9 = Box(main_box, border=True, width=220, height=50, grid=[2,3])
text9 = Text(box9, text="Pháp")

box10 = Box(main_box, border=True, width=220, height=50, grid=[0,4])
text10 = Text(box10, text="Tiền đạo")
box11 = Box(main_box, border=True, width=220, height=50, grid=[1,4])
text11 = Text(box11, text="Tiền đạo")
box12 = Box(main_box, border=True, width=220, height=50, grid=[2,4])
text12 = Text(box12, text="Tiền đạo")

app.display()
