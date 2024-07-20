import pygame
import random

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("벽돌 깨기 게임")

# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# 공 설정
ball_size = 10
ball_speed = [5, 5]
ball_pos = [screen_width // 2, screen_height // 2]

# 패들 설정
paddle_width = 100
paddle_height = 10
paddle_speed = 10
paddle_pos = [screen_width // 2 - paddle_width // 2, screen_height - 50]

# 벽돌 설정
brick_rows = 5
brick_cols = 8
brick_width = screen_width // brick_cols
brick_height = 30
bricks = []

for i in range(brick_rows):
    for j in range(brick_cols):
        bricks.append(pygame.Rect(j * brick_width, i * brick_height, brick_width, brick_height))

# 게임 루프
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_pos[0] > 0:
        paddle_pos[0] -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_pos[0] < screen_width - paddle_width:
        paddle_pos[0] += paddle_speed

    # 공 위치 업데이트
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # 공이 화면 경계에 닿았을 때 반사
    if ball_pos[0] <= 0 or ball_pos[0] >= screen_width - ball_size:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] <= 0:
        ball_speed[1] = -ball_speed[1]

    # 공이 패들에 닿았을 때 반사
    paddle_rect = pygame.Rect(paddle_pos[0], paddle_pos[1], paddle_width, paddle_height)
    if paddle_rect.collidepoint(ball_pos[0], ball_pos[1] + ball_size):
        ball_speed[1] = -ball_speed[1]

    # 공이 벽돌에 닿았을 때 반사 및 벽돌 제거
    for brick in bricks[:]:
        if brick.collidepoint(ball_pos[0], ball_pos[1]):
            bricks.remove(brick)
            ball_speed[1] = -ball_speed[1]
            break

    # 공이 화면 아래로 떨어졌을 때 게임 종료
    if ball_pos[1] >= screen_height:
        running = False

    # 화면 그리기
    screen.fill(black)
    pygame.draw.circle(screen, white, ball_pos, ball_size)
    pygame.draw.rect(screen, blue, paddle_rect)
    for brick in bricks:
        pygame.draw.rect(screen, green, brick)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
