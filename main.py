import pygame


pygame.init()

screen_width = 1500  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("ss")

# FPS
clock = pygame.time.Clock()

first_v1 = int(input("가하는 힘 :" ))
v1 = first_v1
p1 = 10
p2 = 10
v2 = 0
p3 = 10
p4 = 10
time_interval = 0.16
gravity = 9.8
running = True
while running:
    # 2. 키 입력 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
               
            # checking if key "A" was pressed
            if event.key == pygame.K_SPACE:
                p2 = 10
                p4 = 10
            if event.key == pygame.K_r:
                p1 = 10
                p2 = 10
                p4 = 10
                v1 = first_v1
                

    screen.fill((255,255,255))
    pygame.draw.circle(screen, (0,0,255), [p1, p2], 10)
    pygame.draw.circle(screen, (255,0,0), [p3, p4], 10)
    pygame.display.update()
    v2 = v2 + gravity * time_interval
    p2 = p2 + v2 * time_interval
    p4 = p4 + v2 * time_interval
    p1 = p1 + v1
    if p2 >= 630:
        p2 = 630
        v1 = 0
        v2 = 0
    if p4 >= 630:
        p4 = 630
        v1 = 0
        v2 = 0
    
        
    clock.tick(60)
    
    

    
