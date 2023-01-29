from pygame.math import Vector2

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
TILE_SIZE = 64

# ui 
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
UI_FONT = 'font/Pixeltype.ttf'
UI_font_size = 40

#
WATER_COLOR = '71ddee'
UI_BG_COLOR  = '#222222'
UI_BORDER_COLOR = '#111111'
# General Colors 
HEALTH_COLOR = 'red'
SCORE = f'kill all enemy if done GG restart'
NUM_ENEMY = 10

WORLD_MAP = [
    ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
    ['x','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','x'],
    ['x','0','z','e','0','0','0','0','0','0','0','0','0','0','0','0','e','e','0','x'],
    ['x','0','e','e','0','0','0','0','0','0','0','0','0','0','0','0','e','0','0','x'],
    ['x','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','x'],
    ['x','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','x'],
    ['x','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','x'],
    ['x','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','e','0','0','x'],
    ['x','0','e','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','x'],
    ['x','0','e','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','x'],
    ['x','0','0','e','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','x'],
    ['x','0','0','0','0','0','0','0','0','0','0','0','0','0','e','0','0','0','0','x'],
    ['x','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','x'],
    ['x','0','0','0','0','0','0','0','0','0','e','0','0','0','0','0','0','0','0','x'],
    ['x','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','x'],
    ['x','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','x'],
    ['x','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','x'],
    ['x','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','e','e','0','x'],
    ['x','0','z','e','0','0','0','0','0','0','0','0','0','0','0','0','e','0','0','x'],
    ['x','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','x'],
    ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']
]

#ENEMY

monster_data = {
    'demon': {'health': 50, 'damage':10, 'attack_type': 'slash','resistance': 3,'speed': 2, 'attack_radius': 60, 'notice_radius': 360 },
    'oger': {'health': 50, 'damage':10, 'attack_type': 'slash','resistance': 3,'speed': 2, 'attack_radius': 60, 'notice_radius': 360 }
}