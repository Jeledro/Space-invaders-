import pygame
import random
import math
from pygame import mixer

# initializing pygame
pygame.init()

# creating screen
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# caption and icon
pygame.display.set_caption("Juego")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Fuentes
font = pygame.font.Font(None, 40)
small_font = pygame.font.Font('freesansbold.ttf', 30)

# Score
score_val = 0
scoreX = 5
scoreY = 775
monedaX = 5
monedaY = 750
vidasX = 1100
vidasY = 775
fontp = pygame.font.Font('freesansbold.ttf', 20)
shoot_count = 0
monedas = 20

# Game Over
game_over_font = pygame.font.Font('freesansbold.ttf', 64)


global salir
vidas = 3
bullet_vel = 1
salir = False
velocidad = 1

def show_score(x, y):
	score = fontp.render("Puntos: " + str(score_val),
						True, (255,255,255))
	screen.blit(score, (x , y))

def show_monedas(x, y):
	score = fontp.render("Dinero: " + str(monedas),
						True, (255,255,255))
	screen.blit(score, (x , y))

def show_vidas(x, y):
	score = fontp.render("Vidas: " + str(vidas),
						True, (255,255,255))
	screen.blit(score, (x , y))

def game_over():
	game_over_text = game_over_font.render("GAME OVER",
										True, (255,255,255))
	screen.blit(game_over_text, (190, 250))

# Background Sound
mixer.music.load('data/background.wav')
mixer.music.play(-1)

# player
playerImage = pygame.image.load('data/spaceship.png')
player_X = 370
player_Y = 720
player_Xchange = 0
global menu
global mejora
mejora = False
menu = False
desp = 1
vect_mejoras = [desp, velocidad, bullet_vel, vidas, monedas]

# Invader1
invader1Image = []
invader1_X = []
invader1_Y = []
invader1_Xchange = []
invader1_Ychange = []
no_of_invaders1 = 20
no_of_invaders1_init = 20

# Invader2
invader2Image = []
invader2_X = []
invader2_Y = []
invader2_Xchange = []
invader2_Ychange = []
no_of_invaders2 = 20
no_of_invaders2_init = 0 

total_invaders = no_of_invaders1 + no_of_invaders2

for num in range(no_of_invaders1):
	invader1Image.append(pygame.image.load('Alien.png'))
	invader1_X.append(random.randint(64, 1150))
	invader1_Y.append(random.randint(30, 100))
	invader1_Xchange.append(0.1)
	invader1_Ychange.append(50)
	
for num in range(no_of_invaders2):
	invader2Image.append(pygame.image.load('ufo.png'))
	invader2_X.append(random.randint(64, 1150))
	invader2_Y.append(random.randint(30, 100))
	invader2_Xchange.append(0.1)
	invader2_Ychange.append(50)

# Bullet
bulletImage = pygame.image.load('data/bullet.png')
bullet_X = 0
bullet_Y = 750
bullet_Xchange = 0
bullet_Ychange = 3
bullet_state = "rest"

ebulletImage = pygame.image.load('data/bullet.png')
ebullet_X = 0
ebullet_Y = 750
ebullet_Xchange = 0
ebullet_Ychange = 3
ebullet_state = "rest"

# Función para mostrar texto en la pantalla
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

# Collision Concept
def isCollision(x1, x2, y1, y2):
	distance = math.sqrt((math.pow(x1 - x2,2)) +
						(math.pow(y1 - y2,2)))
	if distance <= 50:
		return True
	else:
		return False

def player(x, y):
	screen.blit(playerImage, (x - 16, y + 10))

def invader1(x, y, i):
	screen.blit(invader1Image[i], (x, y))
	
def invader2(x, y, i):
	screen.blit(invader2Image[i], (x, y))

def bullet(x, y):
	global bullet_state
	screen.blit(bulletImage, (x, y))
	bullet_state = "fire"

def ebullet(x, y):
	global ebullet_state
	screen.blit(ebulletImage, (x, y))
	ebullet_state = "fire"

def menucito():
	pygame.draw.rect(screen, white, (295,195,610,410))
	pygame.draw.rect(screen, black, (300,200,600,400))
	draw_text("Menú", font, white, 560, 210)
	draw_text("Lo siento, si esperabas un menú de", small_font, white, 335, 280)
	draw_text("pausa no puedo ofrecertelo :c", small_font, white, 375, 320)
	draw_text("Pero si pulsas 'TAB' en este momento", small_font, white, 315, 400)
	draw_text("Podras cerrar el juego :D", small_font, white, 425, 440)
	draw_text("Salida", font, white, 550, 550)
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_TAB:		
			pygame.quit()

def mejoras(vector):
	desp = vector[0]
	velocidad = vector[1]
	bullet_vel = vector[2]
	vidas = vector[3]
	monedas = vector[4]
	cambio = 0

	pygame.draw.rect(screen, white, (295,195,610,410))
	pygame.draw.rect(screen, black, (300,200,600,400))
	draw_text("MEJORAS", font, white, 535, 210)
	op1 = draw_text("Vel. Desplazamiento", small_font, white, 335, 300)
	op2 = draw_text("Vel. Disparo", small_font, white, 335, 360)
	op3 = draw_text("Comprar vidas", small_font, white, 335, 420)
	draw_text("Lvl.", small_font, white, 750, 300)
	draw_text("Lvl.", small_font, white, 750, 360)
	draw_text("Lvl.", small_font, white, 750, 420)
	draw_text(str(velocidad), small_font, white, 830, 300)
	draw_text(str(bullet_vel), small_font, white, 830, 360)
	draw_text(str(vidas), small_font, white, 830, 420)
	draw_text("Comprar (Enter)", font, white, 485, 510)
	draw_text("Cerrar (Ctrl)", font, white, 515, 550)
	draw_text("Cada compra cuenta 20 monedas", small_font, white, 360, 620)
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_UP:
			pygame.time.wait(1)
			desp -= 1
		if event.key == pygame.K_DOWN:
			pygame.time.wait(1)
			desp += 1
	if desp <= 0:
		desp = 3
	if desp >= 4:
		desp = 1

	if desp == 1:
		op1 = draw_text("Vel. Desplazamiento", small_font, red, 335, 300)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				if monedas >= 20:
					pygame.time.wait(1)
					velocidad += 0.25
					monedas -= 20
					cambio = 1

	if desp == 2:
		op2 = draw_text("Vel. Disparo", small_font, red, 335, 360)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				if monedas >= 20:
					pygame.time.wait(1)
					bullet_vel += 0.5
					monedas -= 20
					cambio = 1

	if desp == 3:
		op3 = draw_text("Comprar vidas", small_font, red, 335, 420)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				if monedas >= 20:
					pygame.time.wait(1)
					vidas += 1
					monedas -= 20
					cambio = 1

	if 	cambio == 1:
		pygame.time.wait(1)
		cambio = 0		

	return [desp, velocidad, bullet_vel, vidas, monedas]
				
no_of_invaders2 = 0
# game loop

running = True
while running:

	player_change = 1.5
	# RGB
	screen.fill((0, 0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		# Controlling the player movement
		# from the arrow keys
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player_Xchange = -player_change*velocidad
			if event.key == pygame.K_RIGHT:
				player_Xchange = player_change*velocidad
			if event.key == pygame.K_SPACE:
				# Fixing the change of direction of bullet
				if bullet_state is "rest":
					bullet_X = player_X
					bullet(bullet_X, bullet_Y)
					bullet_sound = mixer.Sound('data/bullet.wav')
					bullet_sound.play()

			if event.key == pygame.K_ESCAPE:
				menu = not menu
				mejora = False		
			if menu == False:
				if event.key == pygame.K_LCTRL:
					mejora = not mejora
				if event.key == pygame.K_RCTRL:
					mejora = not mejora

		if event.type == pygame.KEYUP:
			player_Xchange = 0

	# adding the change in the player position
	player_X += player_Xchange
	for i in range(no_of_invaders1):
		invader1_X[i] += invader1_Xchange[i] + (score_val*0.03*invader1_Xchange[i])
	
	for i in range(no_of_invaders2):
		invader2_X[i] += invader2_Xchange[i] + (score_val*0.03*invader2_Xchange[i])

	# bullet movement
	if bullet_Y <= 0:
		bullet_Y_init = 600
		bullet_Y = bullet_Y_init * bullet_vel
		bullet_state = "rest"
	if bullet_state is "fire":
		bullet(bullet_X, bullet_Y)
		bullet_Y -= bullet_Ychange
			
	#movement of the invader 
	for i in range(no_of_invaders1):
		
		draw_text("Menú (Esc)", font, white, 15, 15)
		draw_text("Mejoras (Ctrl)", font, white, 980, 15)

		if menu:
			menucito()
		
		if mejora:
			vect_mejoras = mejoras(vect_mejoras)
			desp = vect_mejoras[0]
			velocidad = vect_mejoras[1]
			bullet_vel = vect_mejoras[2]
			vidas = vect_mejoras[3]
			monedas = vect_mejoras[4]
		
        # Collision
		collision = isCollision(bullet_X, invader1_X[i],
								bullet_Y, invader1_Y[i])
		if collision:
			score_val += 1
			monedas += 1
			bullet_Y = 750
			bullet_state = "rest"
			invader1_X[i] = random.randint(64, 1100)
			invader1_Y[i] = random.randint(30, 50)
			invader1_Xchange[i] *= -1
			no_of_invaders1 = no_of_invaders1_init - int(score_val*0.1)
			no_of_invaders2 = no_of_invaders2_init + int((score_val)*0.1)
			if no_of_invaders2 < 0:
				no_of_invaders2 = 0
			total_invaders = no_of_invaders1 + no_of_invaders2
			
		invader1(invader1_X[i], invader1_Y[i], i)
		
		if invader1_Y[i] >= 750 :
			if abs(player_X-invader1_X[i]) < 80:
				for j in range(no_of_invaders1):
					invader1_Y[j] = 2000
					explosion_sound = mixer.Sound('data/explosion.wav')
					explosion_sound.play()
				vidas -= 1
				break

		if invader1_X[i] >= 1150 or invader1_X[i] <= 0:
			invader1_Xchange[i] *= -1
			invader1_Y[i] += invader1_Ychange[i]
	
	for i in range (no_of_invaders2):

		draw_text("Menú (Esc)", font, white, 15, 15)
		draw_text("Mejoras (Ctrl)", font, white, 980, 15)

		if menu:
			menucito()

		shoot_count += 1
		
		if invader2_X[i] >= 1150 or invader2_X[i] <= 0:
			invader2_Xchange[i] *= -1
			invader2_Y[i] += invader2_Ychange[i]

		if invader2_Y[i] >= 750 :
			if abs(player_X-invader2_X[i]) < 80:
				for j in range(no_of_invaders2):
					invader2_Y[j] = 2000
					explosion_sound = mixer.Sound('data/explosion.wav')
					explosion_sound.play()
				vidas -= 1
				break

		invader2(invader2_X[i], invader2_Y[i], i)

		# Collision
		collision = isCollision(bullet_X, invader2_X[i],
								bullet_Y, invader2_Y[i])
		if collision: 
			score_val += 1
			monedas += 1
			bullet_Y = 750
			bullet_state = "rest"
			invader2_X[i] = random.randint(64, 1100)
			invader2_Y[i] = random.randint(30, 50)
			invader2_Xchange[i] *= -1
			no_of_invaders1 = no_of_invaders1_init - int(score_val*0.1)
			no_of_invaders2 = no_of_invaders2_init + int((score_val)*0.1)
			if no_of_invaders2 < 0:
				no_of_invaders2 = 0
			total_invaders = no_of_invaders1 + no_of_invaders2
            
	if vidas == 0:
		game_over()	
	# restricting the spaceship so that
	# it doesn't go out of screen
	if player_X <= 16:
		player_X = 16
	elif player_X >= 1150:
		player_X = 1150

	vect_mejoras = [desp, velocidad, bullet_vel, vidas, monedas]
		
	player(player_X, player_Y)
	
	show_score(scoreX, scoreY)
	show_monedas(monedaX, monedaY)
	show_vidas(vidasX, vidasY)
	pygame.display.update()