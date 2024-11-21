#! /C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

class display:
    where = None
    whereTo = "-" # ["-","↑","↓"]
    
    def __str__(self) -> str:
        return f"<{str(self.where) + self.whereTo}>"
    
    def setWhere(self, planta = 0):
        self.where = planta
        
    def setWhereTo(self, to = "-"):
        self.whereTo = to