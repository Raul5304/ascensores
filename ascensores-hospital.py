#! /C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

from display import display

class boton:
    pass

class botonera:
    pass

class botoneraExterior(botonera):
    pass

class botoneraInterior(botonera):
    pass

class elevator:
    pass

class bigControlElevators:
    pass

if __name__ == "__main__":
    
    # ["-","↑","↓"]
    
    d = display()
    print(d)
    
    d.setWhere(0)
    print(d)
    
    d.setWhereTo("↑")
    print(d)