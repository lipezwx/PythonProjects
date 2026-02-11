import pgzrun
import math
import random
from pygame import Rect

# --- CONSTANTES GLOBAIS ---
WIDTH, HEIGHT = 800, 600
GRAVITY = 0.8
TITLE = "SUPER BOY: ULTIMATE"

STATE_MENU, STATE_GAME, STATE_GAMEOVER = "MENU", "GAME", "GAMEOVER"
game_state = STATE_MENU
audio_on = True
score = 0
camera_x = 0
difficulty_level = 1
mouse_pos = (0, 0)

buttons = {
    "start": Rect(250, 220, 300, 60),
    "audio": Rect(250, 310, 300, 60),
    "exit": Rect(250, 400, 300, 60),
    "retry": Rect(250, 350, 300, 60)
}


class WindParticle:
    """Partículas de vento que dão sensação de dinamismo ao cenário."""
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.speed = random.uniform(2, 5)
        self.length = random.randint(10, 30)

    def update(self):
        self.x -= self.speed
        if self.x < -self.length:
            self.x = WIDTH + self.length
            self.y = random.randint(0, HEIGHT)

    def draw(self):
        screen.draw.line((self.x, self.y), (self.x + self.length, self.y), (255, 255, 255))

class Particle:
    def __init__(self, x, y, color, vy=-1, size=None):
        self.x, self.y = x, y
        self.color = color
        self.size = size or random.randint(2, 6)
        self.life = 1.0
        self.vel_x = random.uniform(-1.5, 1.5)
        self.vel_y = vy

    def update(self, dt):
        self.life -= dt * 1.8
        self.x += self.vel_x
        self.y += self.vel_y

    def draw(self, cam_x):
        alpha = int(self.life * 255)
        if self.life > 0:
            screen.draw.filled_circle((self.x - cam_x, self.y), int(self.size * self.life + 1), self.color)

class Player:
    def __init__(self):
        self.size = 110
        self.reset()
        self.frames_idle = ["texturas/breathing_one", "texturas/breathing_two", "texturas/eye_left", "texturas/eye_right"]
        self.frames_run_r = [f"texturas/boy_running_right_{i}" for i in range(1, 4)]
        self.frames_run_l = [f"texturas/boy_running_left_{i}" for i in range(1, 4)]

    def reset(self):
        self.actor = Actor("texturas/boy_idle", pos=(100, 400))
        self.vel_y = 0
        self.world_x = 100
        self.powerup_timer = 0
        self.idle_timer = self.anim_timer = self.frame_idx = 0
        self.particles = []
        self.ghosts = [] 

    def update(self, platforms, powerups, birds, dt):
        dx = (keyboard.right - keyboard.left) * 380 * dt
        self.world_x += dx
        self.vel_y += GRAVITY
        self.actor.y += self.vel_y
        
        is_powered = self.powerup_timer > 0
        if is_powered: 
            self.powerup_timer -= dt
            if random.random() < 0.3:
                self.ghosts.append({'x': self.world_x, 'y': self.actor.y, 'life': 0.5, 'img': self.actor.image})

        
        if dx != 0:
            self.anim_timer += dt
            if self.anim_timer > 0.07:
                self.anim_timer = 0
                self.frame_idx = (self.frame_idx + 1) % 3
            self.actor.image = self.frames_run_r[self.frame_idx] if dx > 0 else self.frames_run_l[self.frame_idx]
            self.particles.append(Particle(self.world_x, self.actor.y + 30, (255, 255, 255) if not is_powered else (255, 215, 0), vy=random.uniform(-0.5, 0.5)))
        else:
            self.actor.image = "texturas/boy_idle"

        for g in self.ghosts[:]:
            g['life'] -= dt * 2
            if g['life'] <= 0: self.ghosts.remove(g)

        for p in self.particles[:]:
            p.update(dt)
            if p.life <= 0: self.particles.remove(p)

        on_ground = False
        foot = Rect(self.world_x - 15, self.actor.y + 35, 30, 15)
        for plat in platforms:
            if foot.colliderect(plat) and self.vel_y > 0:
                self.actor.y = plat.top - 50
                self.vel_y = 0
                on_ground = True
                break

        if on_ground and (keyboard.up or keyboard.space):
            self.vel_y = -24 if is_powered else -17
            
            for _ in range(5): self.particles.append(Particle(self.world_x, self.actor.y + 40, (255,255,255), vy=1))

        
        hitbox = Rect(self.world_x - 20, self.actor.y - 30, 40, 60)
        for p in powerups[:]:
            if hitbox.colliderect(Rect(p.world_x-20, p.y-20, 40, 40)):
                self.powerup_timer = 7.0
                powerups.remove(p)
        
        for b in birds:
            if hitbox.colliderect(Rect(b.world_x-15, b.actor.y-15, 30, 30)): return True
        return False

    def draw(self, cam_x):
        # Draw Ghosts
        for g in self.ghosts:
            alpha_val = int(g['life'] * 100)
            screen.blit(g['img'], (g['x'] - cam_x - 64, g['y'] - 64)) # Simples blit para ghost
        
        for p in self.particles: p.draw(cam_x)
        self.actor.x = self.world_x - cam_x
        self.actor.draw()

class World:
    def __init__(self):
        self.platforms = [Rect(0, 550, 1000, 50)]
        self.powerups = []
        self.birds = []
        self.wind = [WindParticle() for _ in range(15)]
        self.last_x, self.last_y = 1000, 550

    def generate(self, px, lv):
        for w in self.wind: w.update()
        if px + 900 > self.last_x:
            w = random.randint(150, 350)
            nx = self.last_x + random.randint(160, 280 + (lv * 10))
            ny = max(220, min(540, self.last_y + random.randint(-130, 120)))
            self.platforms.append(Rect(nx, ny, w, 40))
            if random.random() < 0.2:
                p = Actor("texturas/powerup", pos=(nx + w//2, ny - 40))
                p.world_x = nx + w//2
                self.powerups.append(p)
            if random.random() < (0.25 + lv*0.05):
                self.birds.append(Bird(nx+1000, random.randint(100, 450), 1.1 + lv*0.1))
            self.last_x, self.last_y = nx + w, ny

class Bird:
    def __init__(self, x, y, sm):
        self.actor = Actor("texturas/birds", pos=(x, y))
        self.world_x, self.base_y = x, y
        self.speed = random.randint(180, 260) * sm
        self.off = random.uniform(0, 10)

    def update(self, dt):
        self.world_x -= self.speed * dt
        self.actor.y = self.base_y + math.sin(self.world_x * 0.04 + self.off) * 40
        self.actor.x = self.world_x - camera_x

player = Player()
world = World()

def draw():
    screen.clear()
    if game_state == STATE_MENU:
        screen.fill((10, 10, 25))
        screen.draw.text("ULTIMATE BOY", center=(400, 150), fontsize=80, color="cyan", shadow=(3,3))
        draw_ui_button(buttons["start"], "INICIAR")
        draw_ui_button(buttons["audio"], "ÁUDIO: " + ("ON" if audio_on else "OFF"))
        draw_ui_button(buttons["exit"], "SAIR")

    elif game_state == STATE_GAME:
        
        screen.fill((30, 40, 80))
        for w in world.wind: w.draw()
        
        for i in range(5):
            cx = (i * 300 - camera_x * 0.3) % (WIDTH + 400) - 200
            screen.blit("texturas/clouds", (cx, 100 + i*20))

        
        for plat in world.platforms:
            if plat.right > camera_x and plat.left < camera_x + WIDTH:
                rx = plat.x - camera_x
                 
                screen.draw.filled_rect(Rect(rx+8, plat.y+8, plat.w, plat.h), (20, 20, 40))
                
                screen.draw.filled_rect(Rect(rx, plat.y, plat.w, plat.h), (60, 80, 150))
                
                screen.draw.filled_rect(Rect(rx, plat.y, plat.w, 4), (100, 200, 255))
        
        for p in world.powerups:
            p.x = p.world_x - camera_x
            p.draw()
            screen.draw.circle((p.x, p.y), 25 + math.sin(score)*5, (255, 255, 0)) # Glow do item
            
        for b in world.birds: b.actor.draw()
        player.draw(camera_x)
        
        
        screen.draw.filled_rect(Rect(20, 20, 180, 60), (0,0,0, 100))
        screen.draw.text(f"{int(score)}m", (40, 30), fontsize=45, color="white")
        if player.powerup_timer > 0:
            bar_w = (player.powerup_timer / 7.0) * 180
            screen.draw.filled_rect(Rect(20, 85, bar_w, 5), (255, 215, 0))

    elif game_state == STATE_GAMEOVER:
        screen.fill((10, 0, 0))
        screen.draw.text("GAME OVER", center=(400, 200), fontsize=100, color="red", owidth=2)
        draw_ui_button(buttons["retry"], "TENTAR NOVAMENTE")
        draw_ui_button(buttons["exit"], "SAIR")

def draw_ui_button(rect, text):
    is_h = rect.collidepoint(mouse_pos)
    color = (0, 200, 255) if is_h else (0, 100, 180)
    screen.draw.filled_rect(rect, color)
    screen.draw.rect(rect, (255, 255, 255))
    screen.draw.text(text, center=rect.center, fontsize=35, color="white", shadow=(1,1))

def update(dt):
    global camera_x, game_state, score, difficulty_level, world
    if game_state == STATE_GAME:
        difficulty_level = 1 + int(score // 200)
        dead = player.update(world.platforms, world.powerups, world.birds, dt)
        world.generate(player.world_x, difficulty_level)
        for b in world.birds: b.update(dt)
        score = max(score, player.world_x / 10)
        
        camera_x += (player.world_x - 280 - camera_x) * 0.05
        if player.actor.y > HEIGHT + 150 or dead:
            game_state = STATE_GAMEOVER

def on_mouse_move(pos):
    global mouse_pos
    mouse_pos = pos

def on_mouse_down(pos):
    global game_state, audio_on, world, camera_x, score
    if game_state == STATE_MENU:
        if buttons["start"].collidepoint(pos):
            game_state = STATE_GAME
            if audio_on: 
                try: music.play("bgmusic")
                except: pass
        elif buttons["audio"].collidepoint(pos): audio_on = not audio_on
        elif buttons["exit"].collidepoint(pos): exit()
    elif game_state == STATE_GAMEOVER:
        if buttons["retry"].collidepoint(pos):
            player.reset(); world = World(); camera_x = score = 0; game_state = STATE_GAME
        elif buttons["exit"].collidepoint(pos): exit()

pgzrun.go()