import pgzrun

# Variables
TITLE = "Platform Game"
WIDTH = 800
HEIGHT = 500
player = Rect((100, 400), (40, 40))
velocity_y = 10
gravity = 1
on_ground = False
lava = Rect((350, 450), (100, 20))
platforms = [
    Rect((0, 470), (800, 30)),
    Rect((200, 380), (150, 20)),
    Rect((450, 300), (150, 20)),
    Rect((650, 220), (100, 20))
]
coins = [
    Rect((250, 340), (20, 20)),
    Rect((500, 260), (20, 20)),
    Rect((690, 180), (20, 20))
]

score = 0

def draw():
    screen.clear()
    screen.draw.filled_rect(player, "blue")

    for platform in platforms:
        screen.draw.filled_rect(platform, "purple")

    for coin in coins:
        screen.draw.filled_rect(coin, "yellow")
    
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")
    screen.draw.filled_rect(lava, "red")

def update():
    global velocity_y, on_ground, score
    
    velocity_y += gravity
    player.y += velocity_y

    if keyboard.left:
        player.x -= 5

    if keyboard.right:
        player.x += 5

    if player.left < 0:
        player.left = 0

    if player.right > WIDTH:
        player.right = WIDTH

    if player.bottom > HEIGHT:
        player.bottom = HEIGHT
        velocity_y = 0
        on_ground = True

    if keyboard.space and on_ground:
        velocity_y = -15
        on_ground = False

    for platform in platforms:
        if player.colliderect(platform) and velocity_y > 0:
            player.bottom = platform.top
            velocity_y = 0
            on_ground = True

    for coin in coins[:]:
        if player.colliderect(coin):
            coins.remove(coin)
            score += 1

    if player.colliderect(lava):
        player.x = 100
        player.y = 400
        velocity_y = 0

pgzrun.go()
