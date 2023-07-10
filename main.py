import pygame
import items

def game():
    pygame.init()
    reaction = {'happy': pygame.image.load("img/emotion/happy.png"), 'sad': pygame.image.load("img/emotion/sad.png")}

    dirs = ['simple'] * 6

    #exit = items.Button((10, 10), 'img/buttons/exit.png')
    #button_2 = items.Button((110, 10), 'img/buttons/clothes.png')

    head = pygame.image.load("img/head.png")
    fringe = items.Item('fringe', (495, 117), "img/fringe/")
    hair = items.Item('hair', (452, 140), "img/hair/")

    eyes = items.Eyes((545, 252))
    eyelids = items.Eyelids()
    body = items.Breath()
    hears = items.Hears()
    iron = items.Iron()
    nouse = items.Pull([(592, 303)], [(25, 17)], (600, 303), "img/cursor/poke.png", "happy")
    pull_jowls_left = items.Pull([(535, 290), (540, 309), (545, 328)], [(48, 20), (43, 20), (38, 10)], (500, 295),
                                 "img/cursor/pull_left.png")
    pull_jowls_right = items.Pull([(636, 285), (636, 304), (636, 323)], [(48, 20), (45, 20), (40, 10)], (658, 280),
                                  "img/cursor/pull_right.png")
    pull_hear_left = items.Pull([(434, 136), (444, 150), (464, 169), (484, 183)],
                                [(120, 15), (110, 20), (70, 15), (45, 20)], (425, 150),
                                "img/cursor/pull_left.png", "sad", 50)
    pull_hear_right = items.Pull([(704, 98), (670, 107), (650, 121), (650, 140), (650, 159)],
                                 [(40, 10), (70, 15), (85, 20), (75, 20), (65, 20)], (655, 110),
                                 "img/cursor/pull_right.png", "sad", -40)

    pull_activity = [pull_jowls_left, pull_jowls_right, pull_hear_left, pull_hear_right, iron, nouse]

    mouse = items.Mouse()

    pygame.mouse.set_visible(False)

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1200, 720), pygame.SCALED)
    end_game = True
    while end_game:
        clock.tick(30)
        screen.fill((255, 255, 255))

        hair.draw(screen)
        eyes.draw(screen, pygame.mouse.get_pos())

        button_press = -1
        for i in range(len(pull_activity)):
            if pull_activity[i].button_press:
                button_press = i
                break

        hears.draw(screen, pygame.mouse.get_pos(), button_press)
        screen.blit(head, (480, 133))

        body.draw(screen, 8)
        eyelids.draw(screen, 2)
        if button_press != -1:
            screen.blit(reaction[pull_activity[button_press].reaction], (506, 200))

        fringe.draw(screen)

        for i in pull_activity:
            i.action(screen, pygame.mouse.get_pos())
            if i.button_press:
                break

        collide = False
        for i in pull_activity:
            collide = i.collide(pygame.mouse.get_pos())
            if collide:
                break
        #if not collide:
         #   collide = exit.rect.collidepoint(pygame.mouse.get_pos())
        #if not collide:
         #   collide = button_2.rect.collidepoint(pygame.mouse.get_pos())

        #exit.draw(screen, pygame.mouse.get_pos())
        #button_2.draw(screen, pygame.mouse.get_pos())
        mouse.draw(screen, pygame.mouse.get_pos(), button_press, collide)

        for event in pygame.event.get():
            for i in pull_activity:
                i.button(pygame.mouse.get_pos(), event)

            #button_2.button(pygame.mouse.get_pos(), event)

            #exit.button(pygame.mouse.get_pos(), event)
            #if exit.button_press:
             #   end_game = False

            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                end_game = False

        pygame.display.update()
    pygame.quit()

game()

