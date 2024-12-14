from PyQt5.QAxContainer import *
from PyQt5.QtCore import *

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        
        print('Kiwoom 클래스 입니다.')
        
        self.get_ocx_instance()
        self.event_slots()
        
        self.signal_login_commConnect
        
        
    def get_ocx_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1") #응용프로그램 제어 할수 있게 해준다. 경로 지정해준다.
        
    def event_slots(self):
        self.OnEventConnect.connect(self.login_slot) # 
        
    def login_slot(self,errCode):
        if errCode == 0:
            print('connected')
        else:
            print('not connected')

        self.login_event_loop.exit()
        
    def signal_login_commConnect(self):
        self.dynamicCall('CommConnect()')
        
        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()