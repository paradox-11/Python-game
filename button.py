class Button(object):
    def __init__(self, text, color, font, width, height, x=None, y=None, **kwargs):
        self.surface = font.render(text, True, color)

        self.WIDTH = self.surface.get_width()
        self.HEIGHT = self.surface.get_height()

        if 'centered_x' in kwargs and kwargs['centered_x']:
            self.x = width // 2 - self.WIDTH // 2
        else:
            self.x = x

        if 'centered_y' in kwargs and kwargs['cenntered_y']:
            self.y = height // 2 - self.HEIGHT // 2
        else:
            self.y = y

    def display(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def check_click(self, position):
        x_match = self.x < position[0] < self.x + self.WIDTH
        y_match = self.y < position[1] < self.y + self.HEIGHT

        if x_match and y_match:
            return True
        else:
            return False

