import pygame
import sys
from Environment import Environment
from Level import Level

pygame.init()

def drawLevel(matrix_to_draw):
    base = myEnvironment.getPath() + '/themes/' + theme + '/images/'

    wall = pygame.image.load(base + 'wall.png').convert_alpha()
    box = pygame.image.load(base + 'box.png').convert_alpha()
    box_on_target = pygame.image.load(base + 'box_on_target.png').convert_alpha()
    space = pygame.image.load(base + 'space.png').convert_alpha()
    target = pygame.image.load(base + 'target.png').convert_alpha()
    player = pygame.image.load(base + 'player.png').convert_alpha()

    # Auto-resize tiles if needed
    cols, rows = myLevel.getSize()
    scale_limit = 36
    max_w = myEnvironment.size[0] // scale_limit
    max_h = myEnvironment.size[1] // scale_limit

    if cols > max_w or rows > max_h:
        newSize = min(myEnvironment.size[0] // cols,
                      myEnvironment.size[1] // rows)
        newSize = int(newSize)

        wall = pygame.transform.scale(wall, (newSize, newSize))
        box = pygame.transform.scale(box, (newSize, newSize))
        box_on_target = pygame.transform.scale(box_on_target, (newSize, newSize))
        space = pygame.transform.scale(space, (newSize, newSize))
        target = pygame.transform.scale(target, (newSize, newSize))
        player = pygame.transform.scale(player, (newSize, newSize))

    images = {
        '#': wall,
        ' ': space,
        '$': box,
        '.': target,
        '@': player,
        '*': box_on_target
    }

    box_size = wall.get_width()
    myEnvironment.screen.fill((0, 0, 0))

    for row in range(len(matrix_to_draw)):
        for col in range(len(matrix_to_draw[row])):
            tile = matrix_to_draw[row][col]
            if tile in images:
                myEnvironment.screen.blit(images[tile], (col * box_size, row * box_size))

    pygame.display.update()


def movePlayer(direction, myLevel):
    global target_under_player, current_level

    matrix = myLevel.getMatrix()
    myLevel.addToHistory(matrix)

    px, py = myLevel.getPlayerPosition()

    # Direction vectors
    dirs = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}
    dx, dy = dirs[direction]

    nx, ny = px + dx, py + dy       # tile ahead
    fx, fy = px + dx*2, py + dy*2   # tile after box

    # Protect against index error
    def safeGet(y, x):
        if y < 0 or y >= len(matrix):
            return '#'
        if x < 0 or x >= len(matrix[y]):
            return '#'
        return matrix[y][x]

    target_tile = safeGet(ny, nx)
    after_tile = safeGet(fy, fx)

    # --- Player Movement Rules ---
    # Move into empty space or target
    if target_tile in (" ", "."):
        matrix[py][px] = "." if target_under_player else " "
        target_under_player = (target_tile == ".")

        matrix[ny][nx] = "@"

    # --- Box Pushing Rules ---
    elif target_tile in ("$", "*"):
        if after_tile in (" ", "."):
            # Move the box
            matrix[fy][fx] = "*" if after_tile == "." else "$"

            # Move the player
            matrix[py][px] = "." if target_under_player else " "
            target_under_player = (target_tile == "*")

            matrix[ny][nx] = "@"

    drawLevel(matrix)

    # --- Check if all boxes are on targets ---
    remaining = myLevel.getBoxes()
    print("Boxes remaining:", len(remaining))

    if len(remaining) == 0:
        print("Level Completed!")
        current_level += 1
        initLevel(level_set, current_level)


def initLevel(level_set, level):
    global myLevel, target_under_player
    myLevel = Level(level_set, level)
    target_under_player = False
    drawLevel(myLevel.getMatrix())


# --------------------------------
# Game Initialization
# --------------------------------
myEnvironment = Environment()
theme = "default"
level_set = "original"
current_level = 1

initLevel(level_set, current_level)
pygame.display.set_caption('Sokoban')
# --------------------------------
# Game Loop
# --------------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                movePlayer("L", myLevel)
            elif event.key == pygame.K_RIGHT:
                movePlayer("R", myLevel)
            elif event.key == pygame.K_UP:
                movePlayer("U", myLevel)
            elif event.key == pygame.K_DOWN:
                movePlayer("D", myLevel)

            elif event.key == pygame.K_u:   # Undo
                drawLevel(myLevel.getLastMatrix())

            elif event.key == pygame.K_r:   # Restart
                initLevel(level_set, current_level)

            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
