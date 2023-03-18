import pygame

# pygameを初期化する
pygame.init()

# 画面サイズを設定する
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 画像を読み込む
image = pygame.image.load("bondo.png")

# ゲームのメインループを作成する
while True:
    # イベント処理などを行う
    # ...

    # 画面を塗りつぶす
    screen.fill((255, 255, 255))

    # 画像を表示する
    screen.blit(image, (0, 0))

    # 画面を更新する
    pygame.display.flip()

# pygameを終了する
pygame.quit()
