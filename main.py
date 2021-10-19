import pygame

FPS = 60
width = 500
height = 600
colorOfWhite = (255, 255, 255)
# 遊戲初始化 and 創建視窗
pygame.init()
screen = pygame.display.set_mode((width, height))
running = True
clock = pygame.time.Clock()
x = 0

# 遊戲迴圈
while running:
    clock.tick(FPS)
    # 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新遊戲

    # 畫面顯示
    screen.fill(colorOfWhite)
    pygame.display.update()

pygame.quit()
