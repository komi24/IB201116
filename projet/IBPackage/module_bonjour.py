# -*- coding: utf-8 -*-

def dire_bonjour(name):
    print(f"Bonjour {name}")
    
    
def apply(liste, operation):
    for i in liste:
        operation(i)
        

print(__name__)    
if __name__ == "__main__":
    dire_bonjour("Thomas")
    apply(["Roger", "Gwendoline"], dire_bonjour)
