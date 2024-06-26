import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import time
sea = 0
lvl = 0 
mastery_new_lvl = 70
master = 0
mastery_now_lvl = 68
mob_boss = 0

mastery_mob_kill = {"gelley_captain": 0,
                    "royal_soldier": 0,
                    "royal_squa": 0}

mastery_boss_kill = {"cyborg": 0,
                     "thunder_god": 0,
                     "wysper": 0
                    }

kill_info = {"gelley_captain": 0,
            "royal_soldier": 0,
            "royal_squa": 0}

boss_kill_info = {"cyborg": 0,
                  "thunder_god": 0,
                  "wysper": 0}

lvl_kill = {}

mob_sea_1 = {"gelley captain": random.randint(22000,25000),
             "royal_soldier": random.randint(20000,25000),
             "royal_squa": random.randint(17000,22000)
            }

boss_sea_1 = {"cyborg": random.randint(150000,180000),
              "thunder_god": random.randint(100000,150000),
              "wysper": random.randint(85000,90000)
             }

mob_sea_2 = {"water_fighter": random.randint(65000,75000),
             "sea_soldier": random.randint(65000,70000),
             "snow_lurker": random.randint(63000,70000)
            }

mastery_mob_kill_sea_2 = {"water_fighter": 0,
                          "sea_soldier": 0,
                          "snow_lurker": 0
                    }

mob_kill_sea_2 = {"water_fighter": 0,
                  "sea_soldier": 0,
                  "snow_lurker": 0
                  }

boss_sea_2 = {"ice_admiral": random.randint(900000,950000),
              "tide_keeper": random.randint(850000,900000),
              "smoke_admiral": random.randint(800000,900000)
              }

mastery_boss_kill_sea_2 = {"ice_admiral": 0,
                           "tide_keeper": 0,
                           "smoke_admiral": 0
                           }

boss_kill_sea_2 = {"ice_admiral": 0,
                   "tide_keeper": 0,
                   "smoke_admiral": 0
                   }

def now_lvl(): 
        global lvl
        global mastery_now_lvl 
        if int(lvl) >= 1 and int(lvl) <= 99:
            mastery_now_lvl = 70
            for i in range(int(lvl)):
                mastery_now_lvl += i*16
        elif int(lvl) >=100 and int(lvl) <= 199:
            mastery_now_lvl = 80000
            for i in range(int(lvl)-10):
                mastery_now_lvl += i*2
        elif int(lvl) >=200 and int(lvl) <= 299:
            mastery_now_lvl = 260000
            for i in range(int(lvl)-100):
                mastery_now_lvl += i*4           
        elif int(lvl) >=300 and int(lvl) <= 399:
            mastery_now_lvl = 320000
            for i in range(int(lvl)-100):
                mastery_now_lvl += i*5
        elif int(lvl) >=400 and int(lvl) <= 499:
            mastery_now_lvl = 541265
            for i in range(int(lvl)-100):
                mastery_now_lvl += i*6         
        elif int(lvl) >=500 and int(lvl) <= 599:
            mastery_now_lvl = 1015283
            for i in range(int(lvl)-100):
                mastery_now_lvl += i*7            
        elif int(lvl) >=600 and int(lvl) <= 700:
            mastery_now_lvl = 1881554
            for i in range(int(lvl)-100):
                mastery_now_lvl += i*8
        return mastery_now_lvl

def mastory_mob_sea_1():
    global mastery_mob_kill
    global lvl
    global lvl_kill
    global mob_sea_1
    global kill_info

    old_lvl = int(lvl)

    lvl_lok_1 = int(lvl)
    lvl_lok_2 = int(lvl)
    lvl_lok_3 = int(lvl)

    lvl_kill["gelley_captain"] = int(lvl)
    lvl_kill["royal_soldier"] = int(lvl)
    lvl_kill["royal_squa"] = int(lvl)

    while lvl_lok_1 <= 699:
            if now_lvl() > mastery_mob_kill["gelley_captain"]:
                mastery_mob_kill["gelley_captain"] += mob_sea_1["gelley captain"]
                kill_info["gelley_captain"] += 1
            else:
                mastery_mob_kill["gelley_captain"] -= now_lvl()
                lvl_lok_1 += 1
                lvl_kill["gelley_captain"] += 1
                lvl = str(lvl_lok_1)

    lvl = old_lvl

    while lvl_lok_2 <= 699:
        if now_lvl() > mastery_mob_kill["royal_soldier"]:
            mastery_mob_kill["royal_soldier"] += mob_sea_1["royal_soldier"]
            kill_info["royal_soldier"] += 1
        else:
            mastery_mob_kill["royal_soldier"] -= now_lvl()
            lvl_lok_2 += 1
            lvl_kill["royal_soldier"] += 1
            lvl = str(lvl_lok_2)

    lvl = old_lvl
    
    while lvl_lok_3 <= 699:
        if now_lvl() > mastery_mob_kill["royal_squa"]:
            mastery_mob_kill["royal_squa"] += mob_sea_1["royal_squa"]
            kill_info["royal_squa"] += 1
        else:
            mastery_mob_kill["royal_squa"] -= now_lvl()
            lvl_lok_3 += 1
            lvl_kill["royal_squa"] += 1
            lvl = str(lvl_lok_3)

    return f"Gelley Captain - {kill_info['gelley_captain']} \nRoyal Soldier - {kill_info['royal_soldier']} \nRoyal Squa - {kill_info['royal_squa']}"

def mastory_boss_sea_1():
    global mastery_boss_kill
    global lvl
    global lvl_kill
    global boss_sea_1
    global boss_kill_info

    old_lvl = int(lvl)

    lvl_lok_1 = int(lvl)
    lvl_lok_2 = int(lvl)
    lvl_lok_3 = int(lvl)

    lvl_kill["cyborg"] = int(lvl)
    lvl_kill["thunder_god"] = int(lvl)
    lvl_kill["wysper"] = int(lvl)

    while lvl_lok_1 <= 699:
            if now_lvl() > mastery_boss_kill["cyborg"]:
                mastery_boss_kill["cyborg"] += boss_sea_1["cyborg"]
                boss_kill_info["cyborg"] += 1
            else:
                mastery_boss_kill["cyborg"] -= now_lvl()
                lvl_lok_1 += 1
                lvl_kill["cyborg"] += 1
                lvl = str(lvl_lok_1)

    lvl = old_lvl
    
    while lvl_lok_2 <= 699:
        if now_lvl() > mastery_boss_kill["thunder_god"]:
            mastery_boss_kill["thunder_god"] += boss_sea_1["thunder_god"]
            boss_kill_info["thunder_god"] += 1
        else:
            mastery_boss_kill["thunder_god"] -= now_lvl()
            lvl_lok_2 += 1
            lvl_kill["thunder_god"] += 1
            lvl = str(lvl_lok_2)
    
    lvl = old_lvl

    while lvl_lok_3 <= 699:
        if now_lvl() > mastery_boss_kill["wysper"]:
            mastery_boss_kill["wysper"] += boss_sea_1["wysper"]
            boss_kill_info["wysper"] += 1
        else:
            mastery_boss_kill["wysper"] -= now_lvl()
            lvl_lok_3 += 1
            lvl_kill["wysper"] += 1
            lvl = str(lvl_lok_3)

    return f"Cyborg - {boss_kill_info['cyborg']} \nThunder God - {boss_kill_info['thunder_god']} \nWysper - {boss_kill_info['wysper']}"

def mastory_mob_sea_2():
    global mastery_mob_kill_sea_2 
    global lvl
    global lvl_kill
    global mob_sea_2
    global mob_kill_sea_2

    old_lvl = int(lvl)

    lvl_kol_1 = int(lvl)
    lvl_kol_2 = int(lvl)
    lvl_kol_3 = int(lvl)

    lvl_kill["water_fighter"] = int(lvl)
    lvl_kill["sea_soldier"] = int(lvl)
    lvl_kill["snow_lurker"] = int(lvl)

    while lvl_kol_1 <= 699:
            if now_lvl() > mastery_mob_kill_sea_2["water_fighter"]:
                mastery_mob_kill_sea_2["water_fighter"] += mob_sea_2["water_fighter"]
                mob_kill_sea_2["water_fighter"] += 1
            else:
                mastery_mob_kill_sea_2["water_fighter"] -= now_lvl()
                lvl_kol_1 += 1
                lvl_kill["water_fighter"] += 1
                lvl = str(lvl_kol_1)

    lvl = old_lvl
    
    while lvl_kol_2 <= 699:
        if now_lvl() > mastery_mob_kill_sea_2["sea_soldier"]:
            mastery_mob_kill_sea_2["sea_soldier"] += mob_sea_2["sea_soldier"]
            mob_kill_sea_2["sea_soldier"] += 1
        else:
            mastery_mob_kill_sea_2["sea_soldier"] -= now_lvl()
            lvl_kol_2 += 1
            lvl_kill["sea_soldier"] += 1
            lvl = str(lvl_kol_2)
    
    lvl = old_lvl

    while lvl_kol_3 <= 699:
        if now_lvl() > mastery_mob_kill_sea_2["snow_lurker"]:
            mastery_mob_kill_sea_2["snow_lurker"] += mob_sea_2["snow_lurker"]
            mob_kill_sea_2["snow_lurker"] += 1
        else:
            mastery_mob_kill_sea_2["snow_lurker"] -= now_lvl()
            lvl_kol_3 += 1
            lvl_kill["snow_lurker"] += 1
            lvl = str(lvl_kol_3)

    return f"Water Fighter - {mob_kill_sea_2['water_fighter']} \nSea Soldier - {mob_kill_sea_2['sea_soldier']} \nSnow Lurker - {mob_kill_sea_2['snow_lurker']}"

def mastory_boss_sea_2():
    global mastery_boss_kill_sea_2
    global lvl
    global lvl_kill
    global boss_sea_2
    global boss_kill_sea_2

    old_lvl = int(lvl)

    lvl_lok_1 = int(lvl)
    lvl_lok_2 = int(lvl)
    lvl_lok_3 = int(lvl)
    
    lvl_kill["tide_keeper"] = int(lvl)
    lvl_kill["ice_admiral"] = int(lvl)
    lvl_kill["smoke_admiral"] = int(lvl)

    while lvl_lok_1 <= 699:
            if now_lvl() > mastery_boss_kill_sea_2["tide_keeper"]:
                mastery_boss_kill_sea_2["tide_keeper"] += boss_sea_2["tide_keeper"]
                boss_kill_sea_2["tide_keeper"] += 1
            else:
                mastery_boss_kill_sea_2["tide_keeper"] -= now_lvl()
                lvl_lok_1 += 1
                lvl_kill["tide_keeper"] += 1
                lvl = str(lvl_lok_1)
    
    lvl = old_lvl

    while lvl_lok_2 <= 699:
        if now_lvl() > mastery_boss_kill_sea_2["ice_admiral"]:
            mastery_boss_kill_sea_2["ice_admiral"] += boss_sea_2["ice_admiral"]
            boss_kill_sea_2["ice_admiral"] += 1
        else:
            mastery_boss_kill_sea_2["ice_admiral"] -= now_lvl()
            lvl_lok_2 += 1
            lvl_kill["ice_admiral"] += 1
            lvl = str(lvl_lok_2)
    
    lvl = old_lvl

    while lvl_lok_3 <= 699:
        if now_lvl() > mastery_boss_kill_sea_2["smoke_admiral"]:
            mastery_boss_kill_sea_2["smoke_admiral"] += boss_sea_2["smoke_admiral"]
            boss_kill_sea_2["smoke_admiral"] += 1
        else:
            mastery_boss_kill_sea_2["smoke_admiral"] -= now_lvl()
            lvl_lok_3 += 1
            lvl_kill["smoke_admiral"] += 1
            lvl = str(lvl_lok_3)

    return f"Tide Keeper - {boss_kill_sea_2["tide_keeper"]} \nIce Admiral - {boss_kill_sea_2["ice_admiral"]} \nSmoke Admiral - {boss_kill_sea_2["smoke_admiral"]}"

class FourWindow(QWidget):
    def __init__(self):
        super().__init__()
        global mob_sea_1
        global lvl
        global sea
        global mob_boss
        global mastery_new_lvl

        layout = QVBoxLayout()
        self.setLayout(layout)
        self.text = QLabel(" ")
        self.text.setFont(QFont('Arial', 10)) 
        layout.addWidget(self.text)

        if sea == 1:
            if mob_boss == 1:
                self.setWindowTitle("результаты")
                self.text.setText(mastory_mob_sea_1())

            if mob_boss == 2:
                self.setWindowTitle("результаты")
                self.text.setText(mastory_boss_sea_1())

        if sea == 2:
            if mob_boss == 1:
                self.setWindowTitle("результаты")
                self.text.setText(mastory_mob_sea_2())
            
            if mob_boss == 2:
                self.setWindowTitle("результаты")
                self.text.setText(mastory_boss_sea_2())


class ThreeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("На ком вы качаетесь")

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.main_window = QWidget()
        self.stacked_widget.addWidget(self.main_window)

        layout = QVBoxLayout()
        self.main_window.setLayout(layout)
        self.text = QLabel("             На ком вы качаетесь?")
        layout.addWidget(self.text)

        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        self.button1 = QPushButton("Мобы")
        self.button1.clicked.connect(self.mob)
        self.button1.clicked.connect(self.open_four_window) 
        self.button2 = QPushButton("Боссы")
        self.button2.clicked.connect(self.boss)
        self.button2.clicked.connect(self.open_four_window)

        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)

    def mob(self):
        global mob_boss
        mob_boss = 1
    def boss(self):
        global mob_boss
        mob_boss = 2

    def open_four_window(self):
        self.four_window = FourWindow()
        self.stacked_widget.addWidget(self.four_window)
        self.stacked_widget.setCurrentIndex(1)


class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Сколько у вас mastery")

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.text = QLabel("                   Какой у вас лвл mastery?")
        self.LE = QLineEdit() 

        self.LE.textChanged.connect(self.mastery_lvl)

        layout.addWidget(self.text)
        layout.addWidget(self.LE)

        self.button = QPushButton("расчитываем mastery", self)
        self.button.clicked.connect(self.open_three_window)
        layout.addWidget(self.button)

    def mastery_lvl(self, text):
        global lvl
        lvl = text

    def open_three_window(self):
        global  main_window
        self.close()
        main_window.close()
        main_window = ThreeWindow()
        main_window.show()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Выбор что вы хотите качать")

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.main_window = QWidget()
        self.stacked_widget.addWidget(self.main_window)

        layout = QVBoxLayout()
        self.main_window.setLayout(layout)
        self.text = QLabel("                         Где вы качаетесь?")
        layout.addWidget(self.text)

        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        self.button1 = QPushButton("1е море")
        self.button1.clicked.connect(self.open_second_window)
        self.button1.clicked.connect(self.sea_one)
        self.button2 = QPushButton("2е море")
        self.button2.clicked.connect(self.open_second_window)
        self.button2.clicked.connect(self.sea_two)
        self.button3 = QPushButton("3е море")
        self.button3.clicked.connect(self.open_second_window)
        self.button3.clicked.connect(self.sea_three)

        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)
        button_layout.addWidget(self.button3)

    def sea_one(self):
        global sea
        sea = 1
    def sea_two(self):
        global sea
        sea = 2
    def sea_three(self):
        global sea
        sea = 3

    def open_second_window(self):
        self.second_window = SecondWindow()
        self.stacked_widget.addWidget(self.second_window)
        self.stacked_widget.setCurrentIndex(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
    