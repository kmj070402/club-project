import pygame


pygame.init()

screen_width = 1000  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("ss")

# FPS
clock = pygame.time.Clock()

#ball = pygame.pygame.draw.circle((0,0,0), (10,10), 10)
# V_1 = 10
# G = 9.8
# V_2 = 0 + 9.8
# t = 0
# t_t = 0.1
# P1 = 0
a = 640
v1 = 10
v2 = 0
g = 0.5
running = True
while running:
    # 2. 키 입력 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    pygame.draw.circle(screen, (0,0,0), [10 + v1, v2], 10)
    pygame.display.update()
    v1 += 10
    v2 += g * ((640 - a)/ (g + v2))

    clock.tick(30)
    
    

    