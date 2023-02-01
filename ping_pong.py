#Пинг понг
#винзу экрана будет прямоугольник с которым нужно будет отбивать шарик, который отбивается от трех сторон
from superwires import games, color
games.init(screen_width = 480, screen_height = 360, fps = 50)
class Rectangle(games.Sprite):
    '''Прямоугольник с которым надо отбивать шарик.'''
    image = games.load_image('rectangle.png')
    def __init__(self):
        '''Инициализирует объект Rectangle и создает объект Text для отображения счета.'''
        super(Rectangle, self).__init__(image = Rectangle.image,x=games.mouse.x, bottom = games.screen.height)

    def update(self):
        '''Перемещает объект в позицию указателя.'''
        self.x = games.mouse.x

        if self.left<0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
        self.check_catch()
    def check_catch(self):
         '''Проверяет поимал ли игрок бокал.'''
         for ball in self.overlapping_sprites:

             ball.handle_caught()

class Ball(games.Sprite):
    '''Шарик который нужно отбивать.'''
    image = games.load_image('ball.png')
    speed = 1
    def __init__(self):
        '''Инициализирует объект шарик.'''
        super(Ball, self).__init__(image = Ball.image, x=games.screen.width / 2, y=games.screen.height / 2, dx=Ball.speed, dy=Ball.speed)
        self.score = games.Text(value=0, size=25, color=(0, 100, 0), top=5, right=games.screen.width - 10)
        games.screen.add(self.score)
    def update(self):
        '''Проверяет, не коснулась ли нижняя кромка спрайта нижней границы экрана.'''
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
        if self.top < 0:
            self.dy = -self.dy
        if self.bottom>games.screen.height:
            self.end_game()
            self.destroy()
    def handle_caught(self):
        '''заставляет шарик отбиваться.'''
        self.dy = -self.dy*1.2
        self.score.value += 10
        self.score.right = games.screen.width - 10

    def end_game(self):
        '''Завершает игру.'''
        end_message =games.Message(value = 'Game Over', size = 90, color =(100,0,0),
                                   x= games.screen.width/2, y =games.screen.height/2,
                                   lifetime = 5*games.screen.fps,after_death = games.screen.quit)
        games.screen.add(end_message)
def main():
    '''Собственно игровой процесс.'''

    back_image = games.load_image('back.bmp', transparent=False)
    games.screen.background = back_image
    rectangle= Rectangle()
    games.screen.add(rectangle)
    ball = Ball()
    games.screen.add(ball)
    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()
#поехали!
if __name__=='__main__':
    main()
