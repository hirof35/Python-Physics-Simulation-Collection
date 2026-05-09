"""import pygame
import sys
import numpy as np

# 画面のサイズ
WIDTH = 800
HEIGHT = 600
FPS = 60

# 色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# ボールの初期値
ball_radius = 10
ball_color = RED
ball_start_pos = np.array([100, HEIGHT - ball_radius], dtype=float)  # 初期位置をfloat型で
initial_velocity = np.array([50, -100], dtype=float)  # 初速度をfloat型で
gravity = np.array([0, 9.8], dtype=float)  # 重力加速度をfloat型で

# 時間の刻み幅
dt = 1 / FPS

class Ball:
    def __init__(self, position, radius, color):
        self.position = np.array(position, dtype=float)
        self.radius = radius
        self.color = color
        self.velocity = np.array([0, 0], dtype=float)  # ここを修正

    def update(self):
        # 速度の更新（重力の影響）
        self.velocity += gravity * dt
        # 位置の更新
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position[0]), int(self.position[1])), self.radius)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("放物運動シミュレーション")
clock = pygame.time.Clock()

ball = Ball(ball_start_pos, ball_radius, ball_color)
ball.velocity = initial_velocity.copy()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ボールの更新
    ball.update()

    # 画面の描画
    screen.fill(WHITE)
    ball.draw(screen)

    # 画面外に出た場合の処理（簡単なリセット）
    if ball.position[1] > HEIGHT + ball_radius:
        ball.position = np.array([100, HEIGHT - ball_radius], dtype=float)
        ball.velocity = initial_velocity.copy()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()"""
"""
import pygame
import sys
import numpy as np

# 画面のサイズ
WIDTH = 800
HEIGHT = 600
FPS = 60

# 色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# ボールの初期値
ball_radius = 15
ball_color1 = RED
ball_start_pos1 = np.array([200, HEIGHT - ball_radius], dtype=float)
initial_velocity1 = np.array([80, -120], dtype=float)

ball_color2 = BLUE
ball_start_pos2 = np.array([600, HEIGHT - ball_radius * 3], dtype=float)
initial_velocity2 = np.array([-60, -90], dtype=float)

gravity = np.array([0, 9.8 * 10], dtype=float)  # 重力加速度を大きくして見やすく

# 時間の刻み幅
dt = 1 / FPS

class Ball:
    def __init__(self, position, radius, color):
        self.position = np.array(position, dtype=float)
        self.radius = radius
        self.color = color
        self.velocity = np.array([0, 0], dtype=float)

    def update(self):
        # 速度の更新（重力の影響）
        self.velocity += gravity * dt
        # 位置の更新
        self.position += self.velocity * dt

        # 壁との衝突判定
        if self.position[0] + self.radius > WIDTH or self.position[0] - self.radius < 0:
            self.velocity[0] *= -1
            self.position[0] = np.clip(self.position[0], self.radius, WIDTH - self.radius)
        if self.position[1] + self.radius > HEIGHT or self.position[1] - self.radius < 0:
            self.velocity[1] *= -1
            self.position[1] = np.clip(self.position[1], self.radius, HEIGHT - self.radius)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position[0]), int(self.position[1])), self.radius)

def check_collision(ball1, ball2):
    distance = np.linalg.norm(ball1.position - ball2.position)
    return distance < ball1.radius + ball2.radius

def resolve_collision(ball1, ball2):
    # 衝突時の法線ベクトル
    normal = ball2.position - ball1.position
    norm_squared = np.dot(normal, normal)
    if norm_squared == 0:
        return  # ボールが完全に重なっている場合は処理しない

    normal = normal / np.sqrt(norm_squared)
    tangent = np.array([-normal[1], normal[0]])

    # 各ボールの法線方向と接線方向の速度成分
    v1n = np.dot(ball1.velocity, normal)
    v1t = np.dot(ball1.velocity, tangent)
    v2n = np.dot(ball2.velocity, normal)
    v2t = np.dot(ball2.velocity, tangent)

    # 1次元の弾性衝突後の法線方向の速度 (質量は同じと仮定)
    v1n_new = v2n
    v2n_new = v1n

    # 新しい速度ベクトル
    ball1.velocity = v1n_new * normal + v1t * tangent
    ball2.velocity = v2n_new * normal + v2t * tangent

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("衝突シミュレーション")
clock = pygame.time.Clock()

ball1 = Ball(ball_start_pos1, ball_radius, ball_color1)
ball1.velocity = initial_velocity1.copy()

ball2 = Ball(ball_start_pos2, ball_radius, ball_color2)
ball2.velocity = initial_velocity2.copy()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ボールの更新
    ball1.update()
    ball2.update()

    # 衝突判定と処理
    if check_collision(ball1, ball2):
        resolve_collision(ball1, ball2)

    # 画面の描画
    screen.fill(WHITE)
    ball1.draw(screen)
    ball2.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()"""

"""import pygame
import sys
import numpy as np
import random

# 画面のサイズ
WIDTH = 800
HEIGHT = 600
FPS = 60

# 色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
COLORS = [RED, BLUE, GREEN, YELLOW]

# 粒子の数
NUM_PARTICLES = 100

# 粒子の初期値の範囲
PARTICLE_RADIUS_RANGE = (5, 15)
INITIAL_SPEED_RANGE = (-50, 50)

# 重力加速度 (一旦なし)
gravity = np.array([0, 0], dtype=float)

# 時間の刻み幅
dt = 1 / FPS

class Particle:
    def __init__(self, position, radius, color):
        self.position = np.array(position, dtype=float)
        self.radius = radius
        self.color = color
        self.velocity = np.array([random.uniform(*INITIAL_SPEED_RANGE), random.uniform(*INITIAL_SPEED_RANGE)], dtype=float)

    def update(self):
        # 速度の更新（重力の影響）
        self.velocity += gravity * dt
        # 位置の更新
        self.position += self.velocity * dt

        # 壁との衝突判定 (簡易版)
        if self.position[0] + self.radius > WIDTH or self.position[0] - self.radius < 0:
            self.velocity[0] *= -1
            self.position[0] = np.clip(self.position[0], self.radius, WIDTH - self.radius)
        if self.position[1] + self.radius > HEIGHT or self.position[1] - self.radius < 0:
            self.velocity[1] *= -1
            self.position[1] = np.clip(self.position[1], self.radius, HEIGHT - self.radius)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position[0]), int(self.position[1])), int(self.radius))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("多数の粒子シミュレーション")
clock = pygame.time.Clock()

particles = []
for _ in range(NUM_PARTICLES):
    radius = random.randint(*PARTICLE_RADIUS_RANGE)
    position = [random.randint(radius, WIDTH - radius), random.randint(radius, HEIGHT - radius)]
    color = random.choice(COLORS)
    particles.append(Particle(position, radius, color))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 全ての粒子の更新
    for particle in particles:
        particle.update()

    # 画面の描画
    screen.fill(BLACK)  # 背景を黒に
    for particle in particles:
        particle.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()"""

"""import pygame
import sys
import numpy as np

# 画面のサイズとFPS
WIDTH = 800
HEIGHT = 600
FPS = 60

# 色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 振り子のパラメータ
L = 200  # 糸の長さ (ピクセル)
m = 10   # おもりの質量 (任意の値)
g = 9.8 * 50  # 重力加速度 (ピクセル/秒^2 に調整)
theta = np.pi / 4  # 初期角度 (ラジアン)
omega = 0.0      # 初期角速度 (ラジアン/秒)
alpha = 0.0      # 角加速度 (ラジアン/秒^2)

# 吊り下げ点
pivot_x = WIDTH / 2
pivot_y = 100

# 時間刻み幅
dt = 1 / FPS

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("単振り子シミュレーション")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 角加速度の計算
    alpha = -(g / L) * np.sin(theta)

    # 角速度と角度の更新 (オイラー法)
    omega += alpha * dt
    theta += omega * dt

    # おもりの位置の計算
    ball_x = pivot_x + L * np.sin(theta)
    ball_y = pivot_y + L * np.cos(theta)

    # 画面の描画
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, (pivot_x, pivot_y), (int(ball_x), int(ball_y)), 2)
    pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), 20)
    pygame.draw.circle(screen, BLACK, (pivot_x, pivot_y), 5) # 吊り下げ点を描画

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()"""

"""
import pygame
import sys
import numpy as np

# 画面のサイズとFPS
WIDTH = 800
HEIGHT = 600
FPS = 60

# 色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 振り子のパラメータ
L1 = 200.0  # 上側の糸の長さ
L2 = 200.0  # 下側の糸の長さ
m1 = 10.0   # 上側のおもりの質量
m2 = 10.0   # 下側のおもりの質量
g = 9.8 * 50.0  # 重力加速度

theta1 = np.pi / 2  # 上側の初期角度
theta2 = np.pi / 2 + 0.1 # 下側の初期角度 (少しずらすと面白い動きになる)
omega1 = 0.0       # 上側の初期角速度
omega2 = 0.0       # 下側の初期角速度

# 吊り下げ点
pivot_x = WIDTH / 2
pivot_y = 100

# 時間刻み幅
dt = 1 / FPS

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("複振り子シミュレーション")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 角加速度の計算
    num1 = -g * (2 * m1 + m2) * np.sin(theta1) - m2 * g * np.sin(theta1 - 2 * theta2) - 2 * np.sin(theta1 - theta2) * m2 * (omega2**2 * L2 + omega1**2 * L1 * np.cos(theta1 - theta2))
    den1 = L1 * (2 * m1 + m2 - m2 * np.cos(2 * theta1 - 2 * theta2))
    alpha1 = num1 / den1

    num2 = 2 * np.sin(theta1 - theta2) * (omega1**2 * L1 * (m1 + m2) + g * (m1 + m2) * np.cos(theta1) + omega2**2 * L2 * m2 * np.cos(theta1 - theta2))
    den2 = L2 * (2 * m1 + m2 - m2 * np.cos(2 * theta1 - 2 * theta2))
    alpha2 = num2 / den2

    # 角速度と角度の更新 (オイラー法)
    omega1 += alpha1 * dt
    omega2 += alpha2 * dt
    theta1 += omega1 * dt
    theta2 += omega2 * dt

    # おもりの位置の計算
    x1 = pivot_x + L1 * np.sin(theta1)
    y1 = pivot_y + L1 * np.cos(theta1)
    x2 = x1 + L2 * np.sin(theta2)
    y2 = y1 + L2 * np.cos(theta2)

    # 画面の描画
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, (pivot_x, pivot_y), (int(x1), int(y1)), 2)
    pygame.draw.circle(screen, RED, (int(x1), int(y1)), 15)
    pygame.draw.line(screen, BLACK, (int(x1), int(y1)), (int(x2), int(y2)), 2)
    pygame.draw.circle(screen, BLUE, (int(x2), int(y2)), 15)
    pygame.draw.circle(screen, BLACK, (pivot_x, pivot_y), 5) # 吊り下げ点を描画

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()"""

import pygame
import sys
import numpy as np

# 画面のサイズとFPS
WIDTH = 800
HEIGHT = 600
FPS = 60

# 色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# バネと物体のパラメータ
k = 10.0      # バネ定数
m = 1.0       # 物体の質量
rest_length = 200.0 # バネの自然長 (静止時の長さ)
amplitude = 100.0 # 初期振幅
initial_position = HEIGHT / 2 - rest_length - amplitude # 初期位置
velocity = 0.0    # 初期速度

# 固定点
anchor_x = WIDTH / 2
anchor_y = HEIGHT / 2 - rest_length

# 時間刻み幅
dt = 1 / FPS

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("単振動シミュレーション")
clock = pygame.time.Clock()

position = initial_position

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # フックの法則による力の計算
    extension = position - anchor_y
    force = -k * extension

    # ニュートンの運動方程式による加速度の計算
    acceleration = force / m

    # 速度と位置の更新 (オイラー法)
    velocity += acceleration * dt
    position += velocity * dt

    # 画面の描画
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, (anchor_x, anchor_y), (anchor_x, int(position)), 5) # バネ
    pygame.draw.rect(screen, RED, (anchor_x - 20, int(position) - 20, 40, 40)) # 物体
    pygame.draw.circle(screen, BLACK, (anchor_x, anchor_y), 10) # 固定点

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
