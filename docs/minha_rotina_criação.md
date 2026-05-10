## MINHA ROTINA
1. criar estrutura
2. criar venv (ambiente virtual)
3. ativar venv .\venv\script\active.ps1
4. atualizar pip: python.exe -m pip install --upgrade pip
5. instalar PyGame: pip install pygame
6. gravar arquivo com requisitos: pip freeze > requirements.txt

## Estrutura game
meu_jogo/
│
├── venv/
├── src/
│   ├── main.py
│   ├── entities/
│   ├── scenes/
│   └── systems/
│   └── assets/
│       ├── images/
│       ├── sounds/
│       └── fonts/
│
├── requirements.txt
└── README.md
