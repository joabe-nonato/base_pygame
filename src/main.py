# src\main.py
#--------------------------------------------
# módulos
#--------------------------------------------
from systems.program import aplicacao
import sys
import os

def main():    
    aplicacao(os.path.dirname(__file__))
    sys.exit    

if __name__ == "__main__":
    main()