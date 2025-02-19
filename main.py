import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True
dt = 1 #delta time = time change since last frame - init set to 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #closes the window if you X it out
            running = False

    screen.fill("lightgreen")

    pygame.draw.circle(screen, "red", player_pos, 10)

#player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 10 * dt
    if keys[pygame.K_s]:
        player_pos.y += 10 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 10 * dt
    if keys[pygame.K_d]:
        player_pos.x += 10 * dt



    pygame.display.flip() #flips the display

    clock.tick(60)

pygame.quit()
