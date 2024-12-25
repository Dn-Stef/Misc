import pygame
from math import pi, sin, cos, copysign

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pendulum Simulation")
clock = pygame.time.Clock()

L, g, m, k = 350, 9.8, 10, 50
theta, omega, alpha = pi / 4, 0, 0
origin = (width // 2, height // 4)
br = 30

font = pygame.font.Font(None, 36)
dt = 0.05

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    alpha = -(g / L) * sin(theta) - ((g / L) * sin(theta)) / ((g / L) * sin(theta)) * (k / (m * L)) * omega
    omega += alpha * dt
    theta += omega * dt
    x = origin[0] + L * sin(theta)
    y = origin[1] + L * cos(theta)
    axi_velocity = L * omega
    x_velocity = abs(omega * L * cos(theta))  # magnitude!
    y_velocity = abs(omega * L * sin(theta))  # magnitude!

    screen.fill((192, 192, 192))
    pygame.draw.line(screen, (64, 64, 64), origin, (x, y), 4)
    pygame.draw.circle(screen, (0, 0, 0), (int(x), int(y)), br)
    pygame.draw.line(screen, (255, 0, 0), (int(x), int(y)),
                     (int(x), int(y - 2000 * sin(theta) * sin(omega))), 4)
    pygame.draw.line(screen, (0, 0, 255), (int(x), int(y)),
                     (int(x + 500 * cos(theta) * sin(omega)), int(y)), 4)
    stat_text1 = font.render(f"X-Axis Velocity: {x_velocity:.2f} px/s", True, (51, 51, 255))
    screen.blit(stat_text1, (20, 20))
    stat_text2 = font.render(f"Y-Axis Velocity: {y_velocity:.2f} px/s", True, (255, 51, 51))
    screen.blit(stat_text2, (20, 50))
    stat_text3 = font.render(f"Drag Force: {abs((k / (m * L)) * omega):.5f} N", True, (0, 0, 0))
    screen.blit(stat_text3, (20, 80))

    pygame.display.flip()
    clock.tick(144)

pygame.quit()
