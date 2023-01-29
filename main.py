import pygame, sys
from setting import *
from level import level
class main:
    def __init__(self):
        pygame.init()
    #title
        self.clock = pygame.time.Clock()
    # Main SCREEN
        self.SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        surf = pygame.image.load('mouse/mouse.png').convert_alpha()
        cursor = pygame.cursors.Cursor((0,0), surf)
        pygame.mouse.set_cursor(cursor)
    #SCREEN CONTROL
        self.ctr_login = True
        self.ctr_register = False
        self.ctr_gameloop = False
    # LOGIN SCREEN BackGround
    # btn Image in login
        self.exit_btn = pygame.image.load('Button/0_exit_btn.png').convert_alpha()
        self.exit_scaled = pygame.transform.scale(self.exit_btn,(100,50))

        self.login_btn = pygame.image.load('Button/1_login_btn.png').convert_alpha()
        self.login_scaled = pygame.transform.scale(self.login_btn,(100,50))

        self.register_btn = pygame.image.load('Button/2_register_btn.png').convert_alpha()
        self.register_scaled = pygame.transform.scale(self.register_btn,(150,50))

        self.button_pressed_login = False
        self.button_pressed_register = False

        self.arrow = pygame.image.load('tutorial/1.png').convert_alpha()
        self.space = pygame.image.load('tutorial/2.png').convert_alpha()
    #GLOBAL FONT
        self.base_font = pygame.font.Font('font/Pixeltype.ttf',50) # initialize the font fonttype, Fontsize
    #FONT
        self.login_surface = self.base_font.render('Login', False, 'black') # login AA color
        self.register_surface = self.base_font.render('register', False, 'black') # login AA color
        self.restart_msg = self.base_font.render('RESTART GAME', False, 'black')
        self.login_rect = self.login_surface.get_rect(center = (SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2 - 100))
        self.register_rect = self.register_surface.get_rect(center = (SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2 - 100))
        self.restart_rect = self.restart_msg.get_rect(center = (SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2))


    # Login From    
    #FONT USERINPUT
        self.user_font = pygame.font.Font('font/Pixeltype.ttf',30) # initialize the font fonttype, Fontsize
        self.COLOR_INACTIVE = pygame.Color('lightskyblue3')
        self.COLOR_ACTIVE = pygame.Color('dodgerblue2')
        self.user_input = 'Username'
        self.user_surface_rect = pygame.Rect(SCREEN_WIDTH/2 - 100,300,190,32)

        self.pass_input = 'Password'
        self.pass_surface_rect = pygame.Rect(SCREEN_WIDTH/2 - 100, 350,190,32)

        self.user_active = False
        self.pass_active = False

    #RegisterForm
        self.user_input_reg = 'Username'
        self.user_surface_rect_reg = pygame.Rect(SCREEN_WIDTH/2 - 100,300,190,32)

        self.pass_input_reg = 'Password'
        self.pass_surface_rect_reg = pygame.Rect(SCREEN_WIDTH/2 - 100, 350,190,32)

        self.user_active_reg = False
        self.pass_active_reg = False
# LEVEL
        self.level_surface = level()

    def mainloop(self):
        while True:
            # MAIN SCREEN
            self.SCREEN.fill('#F9F9F3')
            if self.ctr_login:
                # LOGIN SCREEN
                pygame.draw.rect(self.SCREEN, '#55CEFF', pygame.Rect(320,180,640,400),0,10)
                pygame.draw.rect(self.SCREEN, '#00ABF0', pygame.Rect(320,180,640,400),5,10)
                # Draw in login_surf
                # placement and printing btn
                exit_center_rect = self.exit_scaled.get_rect(center = (640,500))
                self.SCREEN.blit(self.exit_scaled, exit_center_rect)
                login_center_rect = self.login_scaled.get_rect(center = (400, 460))
                self.SCREEN.blit(self.login_scaled, login_center_rect)
                register_center_rect = self.register_scaled.get_rect(center = (850, 460))
                self.SCREEN.blit(self.register_scaled, register_center_rect)
                
                # tutor
                self.SCREEN.blit(self.arrow, (40,100))
                self.SCREEN.blit(self.space, (40,200))
                #login text
                self.SCREEN.blit(self.login_surface, self.login_rect)
                #Login Input text box
                pygame.draw.rect(self.SCREEN, 'blue',self.user_surface_rect,2)
                user_surface =  self.user_font.render(self.user_input,False,(255,250,250))
                self.SCREEN.blit(user_surface,(self.user_surface_rect.x + 5, self.user_surface_rect.y + 10))
                
                pygame.draw.rect(self.SCREEN, 'blue',self.pass_surface_rect,2)
                pass_surface =  self.user_font.render(self.pass_input,False,(255,250,250))
                self.SCREEN.blit(pass_surface,(self.pass_surface_rect.x + 5, self.pass_surface_rect.y + 10))

            if self.ctr_register:
                # Register Screen

                pygame.draw.rect(self.SCREEN, '#765341', pygame.Rect(320,180,640,400),0,10)
                pygame.draw.rect(self.SCREEN, '#5b3e31', pygame.Rect(320,180,640,400),5,10)
                # Draw in login_surf
                #btn
                login_center_rect = self.login_scaled.get_rect(center = (400, 460))
                self.SCREEN.blit(self.login_scaled, login_center_rect)
                exit_center_rect = self.exit_scaled.get_rect(center = (640,500))
                self.SCREEN.blit(self.exit_scaled, exit_center_rect)
                register_center_rect = self.register_scaled.get_rect(center = (850, 460))
                self.SCREEN.blit(self.register_scaled, register_center_rect)
                #login text
                self.SCREEN.blit(self.register_surface, self.register_rect)
                #Login Input text box
                pygame.draw.rect(self.SCREEN, 'blue',self.user_surface_rect_reg,2)
                user_surface_reg =  self.user_font.render(self.user_input_reg,False,(255,250,250))
                self.SCREEN.blit(user_surface_reg,(self.user_surface_rect.x + 5, self.user_surface_rect.y + 10))
                
                pygame.draw.rect(self.SCREEN, 'blue',self.pass_surface_rect,2)
                pass_surface_reg =  self.user_font.render(self.pass_input_reg,False,(255,250,250))
                self.SCREEN.blit(pass_surface_reg,(self.pass_surface_rect.x + 5, self.pass_surface_rect.y + 10))
                

            # Game Loop

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Login Interface user INPUTS

                if self.ctr_login:
                    mouse_pos = pygame.mouse.get_pos()
                    # Button Inputs
                    if login_center_rect.collidepoint(mouse_pos):
                        if pygame.mouse.get_pressed()[0] == 1:
                            pygame.draw.rect(self.SCREEN, 'red',self.user_surface_rect_reg,2)
                            pygame.draw.rect(self.SCREEN, 'red',self.pass_surface_rect,2)
                            self.SCREEN.blit(self.user_font.render('Invalid', False, 'black'), (SCREEN_WIDTH / 2 - 50,SCREEN_HEIGHT / 2 + 50))
                            if self.user_input == self.user_input_reg and self.pass_input_reg == self.pass_input and self.user_input != 'Username' and self.pass_input != 'Password':
                                self.ctr_gameloop = True  
                    if register_center_rect.collidepoint(mouse_pos):
                        if pygame.mouse.get_pressed()[0] == 1:
                            self.ctr_login = False
                            self.ctr_register = True
                    if exit_center_rect.collidepoint(mouse_pos):
                        if pygame.mouse.get_pressed()[0] == 1:
                            pygame.quit()
                            sys.exit()
                    # Typing Inputs
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.user_surface_rect.collidepoint(event.pos):
                            self.user_active = True
                            pygame.draw.rect(self.SCREEN, 'green',self.user_surface_rect_reg,2)
                            if(self.user_input == 'Username'):
                                self.user_input = ''
                        else:
                            self.user_active = False
                        if self.pass_surface_rect.collidepoint(event.pos):
                            pygame.draw.rect(self.SCREEN, 'green',self.pass_surface_rect,2)
                            self.pass_active = True
                            if(self.pass_input == 'Password'):
                                self.pass_input = ''
                        else:
                            self.pass_active = False
                    if event.type == pygame.KEYDOWN:
                        if self.user_active == True:
                            if len(self.user_input) < 16:
                                if event.key == pygame.K_BACKSPACE:
                                    self.user_input = self.user_input[:-1]
                                else:
                                    self.user_input += event.unicode
                        if self.pass_active == True:
                            if len(self.pass_input) < 16:
                                if event.key == pygame.K_BACKSPACE:
                                    self.pass_input = self.pass_input[:-1]
                                else:
                                    self.pass_input += event.unicode
                
                if self.ctr_register:
                    mouse_pos = pygame.mouse.get_pos()
                    # Button Inputsq
                    if login_center_rect.collidepoint(mouse_pos):
                        if pygame.mouse.get_pressed()[0] == 1:
                            self.button_pressed_login = True
                            self.ctr_register = False
                            self.ctr_login = True
                    if register_center_rect.collidepoint(mouse_pos):
                        if pygame.mouse.get_pressed()[0] == 1:
                            self.button_pressed_register = True
                    if exit_center_rect.collidepoint(mouse_pos):
                        if pygame.mouse.get_pressed()[0] == 1:
                            pygame.quit()
                            sys.exit()
                    # Typing Inputs
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.user_surface_rect_reg.collidepoint(event.pos):
                            self.user_active_reg = True
                            if self.user_input_reg == 'Username':
                                self.user_input_reg = ''
                        else:
                            self.user_active_reg = False
                        if self.pass_surface_rect_reg.collidepoint(event.pos):
                            if self.pass_input_reg == 'Password':
                                self.pass_input_reg = ''
                            self.pass_active_reg = True
                        else:
                            self.pass_active_reg = False
                    if event.type == pygame.KEYDOWN:
                        if self.user_active_reg == True:
                            pygame.draw.rect(self.SCREEN, 'green',self.user_surface_rect_reg,2)
                            if len(self.user_input_reg) < 16:
                                if event.key == pygame.K_BACKSPACE:
                                    self.user_input_reg = self.user_input_reg[:-1]
                                else:
                                    self.user_input_reg += event.unicode
                        if self.pass_active_reg == True:
                            pygame.draw.rect(self.SCREEN, 'green',self.pass_surface_rect,2)
                            if len(self.pass_input_reg) < 16:
                                if event.key == pygame.K_BACKSPACE:
                                    self.pass_input_reg = self.pass_input_reg[:-1]
                                else:
                                    self.pass_input_reg += event.unicode
                
                if self.ctr_gameloop:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.ctr_gameloop = False
                # Main game command loop
                # if ctr_gameloop:
            dt = self.clock.tick(60)/1000
            # print(dt)
            if self.ctr_gameloop and self.level_surface.restart():
                self.level_surface.run()


            if not self.level_surface.restart():
                pygame.draw.rect(self.SCREEN, '#f94449', pygame.Rect(320,180,640,400),0,10)
                pygame.draw.rect(self.SCREEN, '#de0a26', pygame.Rect(320,180,640,400),5,10)
                self.SCREEN.blit(self.restart_msg, self.restart_rect)
                self.SCREEN.blit(self.base_font.render('GAME OVER', False, 'black'), (SCREEN_WIDTH / 2 - 100,SCREEN_HEIGHT / 2 - 100))

            pygame.display.update()

if __name__ == '__main__':
    game = main()
    game.mainloop()