from tkinter import *
from tkinter import ttk
from train import Train
from PIL import Image, ImageTk
from student import Student
from face_recognition import Face_Recognition
from attendance import Attendance
import os

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("SmartTrack Attendance System")

        # Relative path to the images folder
        image_folder = os.path.join(os.path.dirname(__file__), 'Images_GUI')

        # Image labels setting start
        # First header image
        img = Image.open(os.path.join(image_folder, 'banner.jpg'))
        img = img.resize((1280, 500), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        # Set image as label
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        # Background image
        bg1 = Image.open(os.path.join(image_folder, 'bg3.jpg'))
        bg1 = bg1.resize((1366, 768), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # Set image as label
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)

        # Title section
        title_lb1 = Label(bg_img, text="SmartTrack Attendance System Using Facial Recognition", font=("Times New Roman", 25, "bold"), bg="black", fg="white")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        # Buttons below the title
        # Student button
        std_img_btn = Image.open(os.path.join(image_folder, 'std1.jpg'))
        std_img_btn = std_img_btn.resize((180, 180), Image.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, command=self.student_pannels, image=self.std_img1, cursor="hand2")
        std_b1.place(x=250, y=100, width=180, height=180)

        std_b1_1 = Button(bg_img, command=self.student_pannels, text="Student Management", cursor="hand2", font=("Times New Roman", 10, "bold"), bg="black", fg="white")
        std_b1_1.place(x=250, y=280, width=180, height=45)

        # Detect Face button
        det_img_btn = Image.open(os.path.join(image_folder, 'det1.jpg'))
        det_img_btn = det_img_btn.resize((180, 180), Image.LANCZOS)
        self.det_img1 = ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img, command=self.face_rec, image=self.det_img1, cursor="hand2")
        det_b1.place(x=480, y=100, width=180, height=180)

        det_b1_1 = Button(bg_img, command=self.face_rec, text="Face Scan", cursor="hand2", font=("Times New Roman", 10, "bold"), bg="black", fg="white")
        det_b1_1.place(x=480, y=280, width=180, height=45)

        # Attendance System button
        att_img_btn = Image.open(os.path.join(image_folder, 'att.jpg'))
        att_img_btn = att_img_btn.resize((180, 180), Image.LANCZOS)
        self.att_img1 = ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img, command=self.attendance_pannel, image=self.att_img1, cursor="hand2")
        att_b1.place(x=710, y=100, width=180, height=180)

        att_b1_1 = Button(bg_img, command=self.attendance_pannel, text="Attendance Management", cursor="hand2", font=("Times New Roman", 10, "bold"), bg="black", fg="white")
        att_b1_1.place(x=710, y=280, width=180, height=45)

        # Train button
        tra_img_btn = Image.open(os.path.join(image_folder, 'tra1.jpg'))
        tra_img_btn = tra_img_btn.resize((180, 180), Image.LANCZOS)
        self.tra_img1 = ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img, command=self.train_pannels, image=self.tra_img1, cursor="hand2")
        tra_b1.place(x=250, y=330, width=180, height=180)

        tra_b1_1 = Button(bg_img, command=self.train_pannels, text="Data Training", cursor="hand2", font=("Times New Roman", 10, "bold"), bg="black", fg="white")
        tra_b1_1.place(x=250, y=510, width=180, height=45)

        # Photo button
        pho_img_btn = Image.open(os.path.join(image_folder, 'qr1.png'))
        pho_img_btn = pho_img_btn.resize((180, 180), Image.LANCZOS)
        self.pho_img1 = ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(bg_img, command=self.open_img, image=self.pho_img1, cursor="hand2")
        pho_b1.place(x=480, y=330, width=180, height=180)

        pho_b1_1 = Button(bg_img, command=self.open_img, text="Data Set", cursor="hand2", font=("Times New Roman", 10, "bold"), bg="black", fg="white")
        pho_b1_1.place(x=480, y=510, width=180, height=45)

        # Exit button
        exi_img_btn = Image.open(os.path.join(image_folder, 'exi.jpg'))
        exi_img_btn = exi_img_btn.resize((180, 180), Image.LANCZOS)
        self.exi_img1 = ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img, command=self.Close, image=self.exi_img1, cursor="hand2")
        exi_b1.place(x=710, y=330, width=180, height=180)

        exi_b1_1 = Button(bg_img, command=self.Close, text="Exit", cursor="hand2", font=("Times New Roman", 10, "bold"), bg="black", fg="white")
        exi_b1_1.place(x=710, y=510, width=180, height=45)

# ==================Function for Open Images Folder==================
    def open_img(self):
        os.startfile("data_img")

# ==================Functions for Buttons===========================
    def student_pannels(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_pannels(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_rec(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_pannel(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def Close(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
