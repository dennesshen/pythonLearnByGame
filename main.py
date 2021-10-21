# sprite
import pygame

# 遊戲幀數
FPS = 60
# 遊戲外框參數
width = 500
height = 600
# 顏色參數
colorOfWhite = (255, 255, 255)
colorOfGreen = (0, 255, 0)
# 遊戲運行狀態
running = True

# 遊戲初始化 and 創建視窗
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("第一個遊戲")


# sprite 定義遊戲內物體物件
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(colorOfGreen)
        self.rect = self.image.get_rect()
        """
        self.rect.x = 200
        self.rect.y = 200
        """
        self.rect.centerx = width / 2
        self.rect.bottom = height - 10
        self.speedx = 5  # 移動速度的參數

    def update(self):
        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx

        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= width:
            self.rect.right = width


# 將定義好的物件放入 pygame 的 sprite 群組
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# 其他遊戲相關設置-遊戲幀數控制
clock = pygame.time.Clock()

# 遊戲迴圈
while running:
    clock.tick(FPS)
    # 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新遊戲
    all_sprites.update()

    # 畫面顯示
    screen.fill(colorOfWhite)
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()
