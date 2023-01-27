import pygame, sys
from setting import *
from level import level

pygame.init()
#title
clock = pygame.time.Clock()
# Main SCREEN
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#SCREEN CONTROL
ctr_login = True
ctr_register = False
ctr_gameloop = False
# LOGIN SCREEN BackGround
# btn Image in login
exit_btn = pygame.image.load('Button/0_exit_btn.png').convert_alpha()
exit_scaled = pygame.transform.scale(exit_btn,(100,50))

login_btn = pygame.image.load('Button/1_login_btn.png').convert_alpha()
login_scaled = pygame.transform.scale(login_btn,(100,50))

register_btn = pygame.image.load('Button/2_register_btn.png').convert_alpha()
register_scaled = pygame.transform.scale(register_btn,(150,50))

button_pressed_login = False
button_pressed_register = False
#GLOBAL FONT
base_font = pygame.font.Font('font/Pixeltype.ttf',50) # initialize the font fonttype, Fontsize
#FONT
login_surface = base_font.render('Login', False, 'black') # login AA color
register_surface = base_font.render('register', False, 'black') # login AA color
login_rect = login_surface.get_rect(center = (SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2 - 100))
register_rect = register_surface.get_rect(center = (SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2 - 100))


# Login From
#FONT USERINPUT
user_font = pygame.font.Font('font/Pixeltype.ttf',30) # initialize the font fonttype, Fontsize
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
user_input = 'Username'
user_surface_rect = pygame.Rect(SCREEN_WIDTH/2 - 100,300,190,32)

pass_input = 'Password'
pass_surface_rect = pygame.Rect(SCREEN_WIDTH/2 - 100, 350,190,32)

user_active = False
pass_active = False

#RegisterForm
user_input_reg = 'Username'
user_surface_rect_reg = pygame.Rect(SCREEN_WIDTH/2 - 100,300,190,32)

pass_input_reg = 'Password'
pass_surface_rect_reg = pygame.Rect(SCREEN_WIDTH/2 - 100, 350,190,32)

user_active_reg = False
pass_active_reg = False
# LEVEL
level_surface = level()


while True:
    # MAIN SCREEN
    SCREEN.fill('white')
    if ctr_login:
        # LOGIN SCREEN
        pygame.draw.rect(SCREEN, '#55CEFF', pygame.Rect(320,180,640,400),0,10)
        pygame.draw.rect(SCREEN, '#00ABF0', pygame.Rect(320,180,640,400),5,10)
        # Draw in login_surf
        # placement and printing btn
        exit_center_rect = exit_scaled.get_rect(center = (640,500))
        SCREEN.blit(exit_scaled, exit_center_rect)
        login_center_rect = login_scaled.get_rect(center = (400, 460))
        SCREEN.blit(login_scaled, login_center_rect)
        register_center_rect = register_scaled.get_rect(center = (850, 460))
        SCREEN.blit(register_scaled, register_center_rect)
        #login text
        SCREEN.blit(login_surface, login_rect)
        #Login Input text box
        pygame.draw.rect(SCREEN, 'blue',user_surface_rect,2)
        user_surface =  user_font.render(user_input,False,(255,250,250))
        SCREEN.blit(user_surface,(user_surface_rect.x + 5, user_surface_rect.y + 10))
        
        pygame.draw.rect(SCREEN, 'blue',pass_surface_rect,1,5)
        pass_surface =  user_font.render(pass_input,False,(255,250,250))
        SCREEN.blit(pass_surface,(pass_surface_rect.x + 5, pass_surface_rect.y + 10))

    if ctr_register:
        # Register Screen

        pygame.draw.rect(SCREEN, '#55CEFF', pygame.Rect(320,180,640,400),0,10)
        pygame.draw.rect(SCREEN, '#00ABF0', pygame.Rect(320,180,640,400),5,10)
        # Draw in login_surf
        #btn
        login_center_rect = login_scaled.get_rect(center = (400, 460))
        SCREEN.blit(login_scaled, login_center_rect)
        exit_center_rect = exit_scaled.get_rect(center = (640,500))
        SCREEN.blit(exit_scaled, exit_center_rect)
        register_center_rect = register_scaled.get_rect(center = (600,600))
        SCREEN.blit(register_scaled, register_center_rect)
        #login text
        SCREEN.blit(register_surface, register_rect)
        #Login Input text box
        pygame.draw.rect(SCREEN, 'blue',user_surface_rect_reg,2)
        user_surface_reg =  user_font.render(user_input_reg,False,(255,250,250))
        SCREEN.blit(user_surface_reg,(user_surface_rect.x + 5, user_surface_rect.y + 10))
        
        pygame.draw.rect(SCREEN, 'blue',pass_surface_rect,1,5)
        pass_surface_reg =  user_font.render(pass_input_reg,False,(255,250,250))
        SCREEN.blit(pass_surface_reg,(pass_surface_rect.x + 5, pass_surface_rect.y + 10))

    # Game Loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Login Interface user INPUTS

        if ctr_login:
            mouse_pos = pygame.mouse.get_pos()
            # Button Inputs
            if login_center_rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    if user_input == user_input_reg and pass_input_reg == pass_input:
                        ctr_gameloop = True  
                    button_pressed_login = True
            if register_center_rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    button_pressed_register = True
                    ctr_login = False
                    ctr_register = True
            if exit_center_rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.quit()
                    sys.exit()
            # Typing Inputs
            if event.type == pygame.MOUSEBUTTONDOWN:
                if user_surface_rect.collidepoint(event.pos):
                    user_active = True
                    if(user_input == 'Username'):
                        user_input = ''
                else:
                    user_active = False
                if pass_surface_rect.collidepoint(event.pos):
                    pass_active = True
                    if(pass_input == 'Password'):
                        pass_input = ''
                else:
                    pass_active = False
            if event.type == pygame.KEYDOWN:
                if user_active == True:
                    if len(user_input) < 16:
                        if event.key == pygame.K_BACKSPACE:
                            user_input = user_input[:-1]
                        else:
                            user_input += event.unicode
                        print(user_input)
                if pass_active == True:
                    if len(pass_input) < 16:
                        if event.key == pygame.K_BACKSPACE:
                            pass_input = pass_input[:-1]
                        else:
                            pass_input += event.unicode
        if ctr_register:
            mouse_pos = pygame.mouse.get_pos()
            # Button Inputs
            if login_center_rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    ctr_register = False
                    ctr_login = True
                    button_pressed_login = True
            if register_center_rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    button_pressed_register = True
            if exit_center_rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.quit()
                    sys.exit()
            # Typing Inputs
            if event.type == pygame.MOUSEBUTTONDOWN:
                if user_surface_rect_reg.collidepoint(event.pos):
                    user_active_reg = True
                    if user_input_reg == 'Username':
                        user_input_reg = ''
                else:
                    user_active_reg = False
                if pass_surface_rect_reg.collidepoint(event.pos):
                    if pass_input_reg == 'Password':
                        pass_input_reg = ''
                    pass_active_reg = True
                else:
                    pass_active_reg = False
            if event.type == pygame.KEYDOWN:
                if user_active_reg == True:
                    if len(user_input_reg) < 16:
                        if event.key == pygame.K_BACKSPACE:
                            user_input_reg = user_input_reg[:-1]
                        else:
                            user_input_reg += event.unicode
                        print(user_input)
                if pass_active_reg == True:
                    if len(pass_input_reg) < 16:
                        if event.key == pygame.K_BACKSPACE:
                            pass_input_reg = pass_input_reg[:-1]
                        else:
                            pass_input_reg += event.unicode

        # Main game command loop
        # if ctr_gameloop:
    dt = clock.tick()/1000
    if ctr_gameloop:
        level_surface.run(dt)
    pygame.display.update()
