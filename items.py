import pygame
import random

reaction_pos = (506, 200)


class Item(object):
    def __init__(self, name, position, dir_name, image_name='simple'):
        self.name = name
        self.image = pygame.image.load(str(dir_name) + str(image_name) + '.png')
        self.dir_name = dir_name
        self.image_name = image_name
        self.position = position

    def set_image(self, image_name='simple'):
        if image_name != self.image_name:
            self.image_name = image_name
            self.image = pygame.image.load(str(self.dir_name) + str(self.image_name) + '.png')

    def draw(self, screen):
        screen.blit(self.image, self.position)


class Mouse(object):
    def __init__(self):
        self.image = [pygame.image.load("img/cursor/normal.png"), pygame.image.load("img/cursor/touch.png")]
        self.animation = 0

    def draw(self, screen, pos, stop_draw, collide):
        if stop_draw == -1:
            if collide:
                if self.animation == len(self.image) * 7:
                    self.animation = 0
                screen.blit(self.image[self.animation // 7],
                            (pos[0] - self.image[0].get_width() // 2, pos[1] - self.image[0].get_height() // 2))
                self.animation += 1
            else:
                self.animation = 0
                screen.blit(self.image[0],
                            (pos[0] - self.image[0].get_width() // 2, pos[1] - self.image[0].get_height() // 2))


class Eyes(object):
    def __init__(self, start_pos):
        self.image = pygame.image.load("img/eyes/normal.png")
        self.white = pygame.image.load("img/eyes/white.png")
        self.start_pos = (start_pos[0], start_pos[1])
        self.position = [self.start_pos[0], self.start_pos[0]]

    def set_image(self, image):
        self.image = image

    def draw(self, screen, mouse_pos):
        screen.blit(self.white, (self.start_pos[0] - 18, self.start_pos[1] - 7))
        self.position[0] = max(self.start_pos[0] - 17 + mouse_pos[0] // 28, self.start_pos[0] - 17)
        if self.position[0] > self.start_pos[0] - 17:
            self.position[0] = min(self.position[0], self.start_pos[0] + 17)
        self.position[1] = max(self.start_pos[1] - 12 + mouse_pos[1] // 24, self.start_pos[1] - 12)
        if self.position[1] > self.start_pos[1] - 12:
            self.position[1] = min(self.position[1], self.start_pos[1] + 12)
        screen.blit(self.image, self.position)


class Eyelids(object):
    def __init__(self):
        self.images = [pygame.image.load("img/eyelids/1.png"), pygame.image.load("img/eyelids/2.png"),
                       pygame.image.load("img/eyelids/3.png"), pygame.image.load("img/eyelids/4.png")]
        self.animation = [False, 0]
        self.rewers = False

    def draw(self, screen, tmp):
        if self.animation[1] == 0 and random.randrange(80) == 0:
            self.animation[0] = True
            self.rewers = False
            self.animation[1] += 1
        elif self.animation[1] != 0:
            if self.rewers:
                self.animation[1] -= 1
            else:
                self.animation[1] += 1
        self.animation[0] = self.animation[1] != 0
        if self.animation[1] // tmp != 0:
            screen.blit(self.images[self.animation[1] // tmp - 1], (531, 248))
        if self.animation[1] > len(self.images) * tmp:
            self.rewers = True


class Breath(object):
    def __init__(self):
        self.dir_name = ''
        self.images = []
        self.set_image('simple')
        self.position = (606 - self.images[0].get_width() // 2, 418)
        self.animation = 0
        self.pause = 0
        self.rewers = False

    def set_image(self, dir_name):
        if self.dir_name != dir_name:
            self.dir_name = dir_name
            self.images = [pygame.image.load("img/body/" + str(dir_name) + "_0.png"),
                           pygame.image.load("img/body/" + str(dir_name) + "_1.png"),
                           pygame.image.load("img/body/" + str(dir_name) + "_2.png")]

    def draw(self, screen, tmp):
        if self.rewers:
            self.animation -= 1
        elif not self.rewers and self.pause == 0:
            self.animation += 1
        if self.animation == 0:
            self.pause += 1
            self.rewers = False
        if self.pause == 15:
            self.pause = 0
        if self.animation >= len(self.images) * tmp:
            self.animation -= 1
            self.rewers = True
        screen.blit(self.images[self.animation // tmp], self.position)


class Hears(object):
    def __init__(self):
        self.dirs = ['', '']
        self.position = [(430, 65), (630, 65)]
        self.images = ['', '', '', '', '', '']
        self.set_image(('simple', 'simple'))

    def set_image(self, dirs_name):
        if self.dirs[0] != dirs_name[0] or self.images[0] == '':
            up_left = pygame.image.load("img/hear/" + str(dirs_name[0]) + "_left_up.png")
            middile_left = pygame.image.load("img/hear/" + str(dirs_name[0]) + "_left_middle.png")
            bottom_left = pygame.image.load("img/hear/" + str(dirs_name[0]) + "_left_bottom.png")
        if self.dirs[1] != dirs_name[1] or self.images[3] == '':
            up_right = pygame.image.load("img/hear/" + str(dirs_name[1]) + "_right_up.png")
            middile_right = pygame.image.load("img/hear/" + str(dirs_name[1]) + "_right_middle.png")
            bottom__right = pygame.image.load("img/hear/" + str(dirs_name[1]) + "_right_bottom.png")
        self.images = [up_left, up_right, middile_left, middile_right, bottom_left, bottom__right]

    def draw(self, screen, mouse_pos, stop_hears):
        image = 2
        if self.position[0][0] < mouse_pos[0] < self.position[1][0] + self.images[3].get_width():
            if mouse_pos[1] < 200:
                image = 4
            elif mouse_pos[1] > 490:
                image = 0
        if stop_hears != -1:
            image = 4
        screen.blit(self.images[image], self.position[0])
        screen.blit(self.images[image + 1], self.position[1])


class Pull(object):
    def __init__(self, hitboxes, size, position, image, emotion="sad", angle=0):
        self.rects = []
        for i in range(len(hitboxes)):
            self.rects.append(pygame.Rect(hitboxes[i][0], hitboxes[i][1], size[i][0], size[i][1]))
        self.button_press = False
        self.image = pygame.image.load(image)
        self.image_pos = position
        self.reaction = emotion
        self.angle = angle

    def collide(self, mouse_pos):
        for i in self.rects:
            rect = i.collidepoint(mouse_pos)
            if rect:
                return True
        return False

    def button(self, mouse_pos, event):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.button_press = False
        elif self.collide(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.button_press = True

    def action(self, screen, mouse_pos):
        if self.button_press:
            screen.blit(pygame.transform.rotate(self.image, self.angle), self.image_pos)


class Iron(object):
    def __init__(self):
        hitboxes = [(570, 127), (547, 143), (538, 162)]
        size = [(70, 17), (110, 20), (129, 20)]
        self.rects = []
        for i in range(len(hitboxes)):
            self.rects.append(pygame.Rect(hitboxes[i][0], hitboxes[i][1], size[i][0], size[i][1]))
        self.button_press = False
        self.image = pygame.image.load("img/cursor/iron.png")
        self.image_y = 125
        self.reaction = 'happy'

    def collide(self, mouse_pos):
        for i in self.rects:
            rect = i.collidepoint(mouse_pos)
            if rect:
                return True
        return False

    def button(self, mouse_pos, event):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.button_press = False
        elif self.collide(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.button_press = True

    def action(self, screen, mouse_pos):
        pos = min(mouse_pos[0] - self.image.get_width() // 2, 634 - self.image.get_width() // 2)
        pos = max(pos, 561 - self.image.get_width() // 2)
        if self.button_press:
            screen.blit(self.image, (pos, self.image_y))


class Button(object):
    def __init__(self, position, image):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 1.5, self.image.get_height() * 1.5))
        self.rect = pygame.Rect(position[0], position[1], self.image.get_width() + 8, self.image.get_height() + 8)
        self.button_press = False

    def button(self, mouse_pos, event):
        if self.rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.action()

    def action(self):
        print('hello')
        self.button_press = True

    def draw(self, screen, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (200, 150, 200), self.rect)
        else:
            pygame.draw.rect(screen, (238, 212, 238), self.rect)
        screen.blit(self.image, (self.rect.left + 4, self.rect.top + 4))
