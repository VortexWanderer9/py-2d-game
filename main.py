    import pygame
    pygame.init()

    screen = pygame.display.set_mode((800, 800))

    player_x = 400
    player_y = 300
    speed = 5
    running = true
    while running: 
        for event in pygame.event.get():
            if event.type == player.QUIT():
                running = false
                
        
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= speed

    if keys[pygame.K_RIGHT]:
        player_x += speed

    if keys[pygame.K_UP]:
        player_y -= speed

    if keys[pygame.K_DOWN]:
        player_y += speed

    screen.fill((30, 30, 30))

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (player_x, player_y, 50, 50)
    )

    pygame.display.flip()

pygame.quit()        

