import sys,random,pygame

def create_pipe():
	random_pipe_pos = random.choice(pipe_height)
	bottom_pipe = pipe_surface.get_rect(midtop = (700,random_pipe_pos))
	top_pipe = pipe_surface.get_rect(midbottom = (700,random_pipe_pos - 300))
	return bottom_pipe,top_pipe

def move_pipes(pipes):
	for pipe in pipes:
		pipe.centerx -= 5
	return pipes

def blit_pipes(pipes):
	for pipe in pipes:
		if pipe.bottom >= 1024:
			screen.blit(pipe_surface,pipe)
		else:
			flip_pipe = pygame.transform.flip(pipe_surface,False,True)
			screen.blit(flip_pipe,pipe)

def remove_pipes(pipes):
	for pipe in pipes:
		if pipe.centerx == -600:
			pipes.remove(pipe)
	return pipes

def check_collision(pipes):
	for pipe in pipes:
		if bird_rect.colliderect(pipe):
			return False
	if bird_rect.top <= 0 or bird_rect.bottom >= 1024:
		return False
	return True

def bird_animation():
	new_bird = bird_frames[bird_index]
	new_bird_rect = new_bird.get_rect(center = (100,bird_rect.centery))
	return new_bird,new_bird_rect

def score_display(game_state):
	if game_state == 'main_game':
		score_surface = game_font.render(str(int(score)),True,(0,0,255))
		score_rect = score_surface.get_rect(center = (288,150))
		screen.blit(score_surface,score_rect)
	else: 
		top_score_background = pygame.transform.scale((pygame.image.load("score.png").convert_alpha()),(400,200))
		top_score_surface = game_font.render(str(top_score),True,"White")
		top_score_background_rect = top_score_background.get_rect(center=(288,725))
		top_score_rect = top_score_surface.get_rect(center=(288,725))
		screen.blit(top_score_background,top_score_background_rect)
		screen.blit(top_score_surface,top_score_rect)


pygame.init()
music=pygame.mixer.Sound("music.mp3")
screen = pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()
game_font = pygame.font.SysFont('comicsans',40)

gravity = 0.55
bird_movement = 0
game_active = False
score = 0

bg_surface = pygame.image.load('background.png').convert()
floor_x_pos = 0

bird_downflap = pygame.transform.scale2x(pygame.image.load('downflap.png').convert_alpha())
bird_midflap = pygame.transform.scale2x(pygame.image.load('midflap.png').convert_alpha())
bird_upflap = pygame.transform.scale2x(pygame.image.load('upflap.png').convert_alpha())
bird_frames = [bird_downflap,bird_midflap,bird_upflap]
#defining
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center = (100,512))

FLAP = pygame.USEREVENT + 1
pygame.time.set_timer(FLAP,200)

pipe_surface = pygame.image.load('pipe.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWN = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN,1200)
pipe_height = [400,600,800]

game_over_surface1 = pygame.transform.scale2x(pygame.image.load('message1.png').convert_alpha())
game_over_rect1 = game_over_surface1.get_rect(center = (288,500))
game_over_surface2 = pygame.transform.scale2x(pygame.image.load('message2.png').convert_alpha())
game_over_rect2 = game_over_surface2.get_rect(center = (288,400))
x=-54
top_score=0
top_score_state=0

while True:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				top_score_state=1
				x=-54
			if event.key == pygame.K_SPACE and game_active:
				bird_movement = 0
				bird_movement -= 12
			

			if event.key == pygame.K_SPACE and game_active == False:
				game_active = True
				pipe_list.clear()
				bird_rect.center = (100,512)
				bird_movement = 0
				score = 0
			if event.key == pygame.K_ESCAPE:  
				pygame.quit()
				sys.exit()

		if event.type == SPAWN:
			pipe_list.extend(create_pipe())

		if event.type == FLAP:
			if bird_index < 2:
				bird_index += 1
			else:
				bird_index = 0

			bird_surface,bird_rect = bird_animation()

	screen.blit(bg_surface,(0,0))
	music.set_volume(0.1)
	music.play(-1)
	if game_active:
		bird_movement += gravity
		bird_rect.y += bird_movement
		screen.blit(bird_surface,bird_rect)
		game_active = check_collision(pipe_list)
		pipe_list = move_pipes(pipe_list)
		pipe_list = remove_pipes(pipe_list)
		blit_pipes(pipe_list)
		score += 0.01
		score_display('main_game')
		if top_score<int(score):
			top_score=int(score)
	else:
		screen.blit(game_over_surface1,game_over_rect1)
		screen.blit(game_over_surface2,game_over_rect2)
		
		if x<576:
			x+=1
		else:
			x=-54
		screen.blit(bird_surface,(x,512))

		if top_score_state == 1:
			score_display('start_screen')

	pygame.display.update()
	clock.tick(120)