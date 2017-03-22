# --- MAIN PARAMETERS ---
# game window
WIN_X = 800
WIN_Y = 600
BACKGROUND_COLOR = (150, 150, 150)
PRINT_AVG_FPS_AT_EXIT = True

# number of iterations of the main loop per second
# this also limits the number of frames per second
GAME_SPEED = 60

# bacteria's appearance and behavior
NUMBER_OF_CELLS = 25
CELL_SIZE = 8  # tip: cells look better when even number
CELLS_MOVING = True  # False freezes all movement
CELLS_NON_ROTATED = False  # True makes cells start from non-rotated positions
PNG_IMAGE = ''  # 'black_test3.png'  # empty string if drawing using shapes
MORPHOLOGY = 'bacillus'  # in case drawing using pygame's shapes
CELL_COLOR = (50, 50, 50)  # in case drawing using pygame's shapes
# --- --------------- ---
