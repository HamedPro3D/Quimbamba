"""
Guarda los ajustes del programa que son constantes.
"""
Ancho    = 1280	
Largo   = 720
FPS      = 60
TILESIZE = 64

alturavida = 25
anchovida = 250
anchobarraenergia=160
tamañocorazon = 90
ubicacion = "./Grafico/font/joystix.ttf"
tamañofuente = 20

WORLD_MAP = [
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ','p',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ','x','','','','','',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ','x',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ','x',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ','x',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ','x',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ','x',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ','x',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ','x',' ',' ',' ',' ','x','x','x',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ','x',' ','x',' ','x',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
]

informacionmosutros={
    "squid":  {"vida": 50,"xp": 200, "daño": 10,"tipoataque": "golpe","velocidad":5,"radioataque":60,"deteccion":500,"resistencia":0},
    "raccoon":  {"vida": 600,"xp": 300, "daño": 80,"tipoataque": "patron","velocidad":3,"radioataque":120,"deteccion":400,"resistencia":3},
    "spirit": {"vida": 100,"xp": 100, "daño": 3,"tipoataque": "rap","velocidad":0,"radioataque":360,"deteccion":200,"resistencia":9},
    "bamboo": {"vida": 40,"xp": 1000, "daño": 20,"tipoataque": "matriz","velocidad":3,"radioataque":360,"deteccion":450,"resistencia":30}
}