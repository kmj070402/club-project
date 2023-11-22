import pygame


pygame.init()

screen_width = 1440  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Mechanical Energy Motion Simulation")

# FPS
clock = pygame.time.Clock()

# 기본 설정
first_v1 = int(input("가하는 힘 :" ))
v1 = first_v1  #수평 방향 속도
p1 = 20  #파란공 x좌표
p2 = 20  #파란공 y좌표
v2 = 0   #연직 방향 속도
p3 = 20  #빨간공 x좌표
p4 = 20  #빨간공 y좌표
time_interval = 0.16  #임의의 시간 간격
gravity = 9.8  #중력가속도
running = True
ball_list = []
count = 0


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
               
            # 자유 낙하 운동 리플레이
            if event.key == pygame.K_SPACE:  
                p2 = 20
                p4 = 20
                ball_list = []
            
            # 시뮬레이션 리플레이
            if event.key == pygame.K_r:
                p1 = 20
                p2 = 20
                p4 = 20
                v1 = first_v1
                ball_list = []

    # 10번 반복할 때마다 원의 좌표 저장             
    count += 1
    if count == 10:
        ball_list.append([[p1,p2],[p3,p4]])
        count = 0
            
    #화면 설정
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (0,0,255), [p1, p2], 20)
    pygame.draw.circle(screen, (255,0,0), [p3, p4], 20)
    for i in ball_list:
        pygame.draw.circle(screen,(0,0,255),[i[0][0],i[0][1]],20)
        pygame.draw.circle(screen,(255,0,0),[i[1][0],i[1][1]],20)
    for i in range(150):
        pygame.draw.line(screen, (0,0,0), [0 + (40 * i),0], [0 + (40 * i),640], 1)
        pygame.draw.line(screen, (0,0,0), [0,0 + (40 * i)], [1500,0 + (40 * i)], 1)
        pygame.draw.line(screen, (0,0,0), [0 + (200 * i),0], [0 + (200 * i),1500], 2)
    pygame.display.update()

    #역학적 운동값 계산
    v2 = v2 + gravity * time_interval  
    p2 = p2 + v2 * time_interval
    p4 = p4 + v2 * time_interval
    p1 = p1 + v1 

    #시뮬레이션 중지 
    if p2 >= 620:
        p2 = 620
        v1 = 0
        v2 = 0
    if p4 >= 620:
        p4 = 620
        v1 = 0
        v2 = 0
        
    clock.tick(60)
    
    

    
    
    

    
