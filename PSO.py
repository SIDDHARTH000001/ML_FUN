# import cv2
# import mediapipe as mp
# import pygame
# import numpy as np
# import random
# import math

# class Particle:
#     def __init__(self, width, height):
#         self.reset_position(width, height)
#         self.size = random.randint(2, 4)
#         self.color = (135, 206, 235)  
#         self.max_speed = 5
#         self.attraction_strength = 0.5

#     def reset_position(self, width, height):
#         self.x = random.randint(0, width)
#         self.y = random.randint(0, height)
#         self.vx = random.uniform(-2, 2)
#         self.vy = random.uniform(-2, 2)

# class HandParticleSystem:
#     def __init__(self):

#         pygame.init()
#         self.width = 800
#         self.height = 600
#         self.screen = pygame.display.set_mode((self.width, self.height))
#         pygame.display.set_caption("Hand Particle Attraction")

#         self.mp_hands = mp.solutions.hands
#         self.hands = self.mp_hands.Hands(
#             max_num_hands=2,
#             min_detection_confidence=0.7,
#             min_tracking_confidence=0.5
#         )
#         self.mp_draw = mp.solutions.drawing_utils

#         self.cap = cv2.VideoCapture(0)
#         self.cap.set(3, self.width)
#         self.cap.set(4, self.height)

#         self.num_particles = 300
#         self.particles = []
#         self.init_particles()
        
#         self.BLACK = (0, 0, 0)
        
#         self.clock = pygame.time.Clock()
#         self.hand_present = False
#         self.hand_position = None

#     def init_particles(self):
#         self.particles = [Particle(self.width, self.height) 
#                          for _ in range(self.num_particles)]

#     def detect_hand(self, frame):
#         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         results = self.hands.process(rgb_frame)
        
#         if results.multi_hand_landmarks:
#             hand_landmarks = results.multi_hand_landmarks[0]  
#             x_coords = [int(lm.x * self.width) for lm in hand_landmarks.landmark]
#             y_coords = [int(lm.y * self.height) for lm in hand_landmarks.landmark]

#             mid_x = sum(x_coords) // len(x_coords)
#             mid_y = sum(y_coords) // len(y_coords)


#             mid_x = self.width - mid_x  
#             self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

#             return True, (mid_x, mid_y)
        
#         return False, None

        
#     def _update_particle(self, particle, hand_pos=None):
#         if hand_pos:
#             dx = particle.x - hand_pos[0] 
#             dy = particle.y - hand_pos[1]  
#             distance = math.sqrt(dx*dx + dy*dy)
            
#             if distance > 0:
#                 particle.vx -= (dx/distance) * particle.attraction_strength 
#                 particle.vy -= (dy/distance) * particle.attraction_strength  
#         else:
#             particle.vx += random.uniform(-0.1, 0.1)
#             particle.vy += random.uniform(-0.1, 0.1)

#         speed = math.sqrt(particle.vx*particle.vx + particle.vy*particle.vy)
#         if speed > particle.max_speed:
#             particle.vx = (particle.vx/speed) * particle.max_speed
#             particle.vy = (particle.vy/speed) * particle.max_speed

#         particle.x += particle.vx
#         particle.y += particle.vy

#         particle.x = particle.x % self.width
#         particle.y = particle.y % self.height

#     def update_particle(self, particle, hand_pos=None):
#         if hand_pos:
#             dx = hand_pos[0] - particle.x  
#             dy = hand_pos[1] - particle.y  
#             distance = math.sqrt(dx * dx + dy * dy)
            
#             if distance > 0:
#                 particle.vx += (dx / distance) * particle.attraction_strength 
#                 particle.vy += (dy / distance) * particle.attraction_strength  
#         else:
#             particle.vx += random.uniform(-0.1, 0.1)
#             particle.vy += random.uniform(-0.1, 0.1)
            
#         speed = math.sqrt(particle.vx * particle.vx + particle.vy * particle.vy)
#         if speed > particle.max_speed:
#             particle.vx = (particle.vx / speed) * particle.max_speed
#             particle.vy = (particle.vy / speed) * particle.max_speed

  
#         particle.x += particle.vx
#         particle.y += particle.vy

#         particle.x = particle.x % self.width
#         particle.y = particle.y % self.height


#     def run(self):
#         """Main loop"""
#         running = True
#         while running:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False

#             ret, frame = self.cap.read()
#             if not ret:
#                 continue

      

#             self.hand_present, self.hand_position = self.detect_hand(frame)

#             self.screen.fill(self.BLACK)

#             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             frame = np.rot90(frame)
#             frame = pygame.surfarray.make_surface(frame)
#             self.screen.blit(frame, (0, 0))

#             for particle in self.particles:
#                 self.update_particle(particle, self.hand_position if self.hand_present else None)
#                 pygame.draw.circle(
#                     self.screen,
#                     particle.color,
#                     (int(particle.x), int(particle.y)),
#                     particle.size
#                 )

#             pygame.display.flip()
#             self.clock.tick(60)

#         self.cap.release()
#         self.hands.close()
#         pygame.quit()

# if __name__ == "__main__":
#     system = HandParticleSystem()
#     system.run()


import cv2
import mediapipe as mp
import pygame
import numpy as np
import random
import math

class Particle:
    def __init__(self, width, height):
        self.reset_position(width, height)
        self.size = random.randint(2, 4)
        self.color = (135, 206, 235)  
        self.max_speed = 5
        self.attraction_strength = 0.5

    def reset_position(self, width, height):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)

class HandParticleSystem:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Multi-Hand Particle Attraction")

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=2, 
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.mp_draw = mp.solutions.drawing_utils

        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, self.width)
        self.cap.set(4, self.height)

        self.num_particles = 600
        self.particles = []
        self.init_particles()
        
        self.BLACK = (0, 0, 0)
        
        self.clock = pygame.time.Clock()
        self.hand_positions = []  

    def init_particles(self):
        self.particles = [Particle(self.width, self.height) 
                         for _ in range(self.num_particles)]

    def detect_hands(self, frame):
        """Detect multiple hands in the frame"""
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)
        
        hand_positions = []
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                x_coords = [int(lm.x * self.width) for lm in hand_landmarks.landmark]
                y_coords = [int(lm.y * self.height) for lm in hand_landmarks.landmark]

                mid_x = sum(x_coords) // len(x_coords)
                mid_y = sum(y_coords) // len(y_coords)

                mid_x = self.width - mid_x

                self.mp_draw.draw_landmarks(
                    frame, 
                    hand_landmarks, 
                    self.mp_hands.HAND_CONNECTIONS
                )

                hand_positions.append((mid_x, mid_y))
        
        return hand_positions

    def update_particle(self, particle, hand_positions=None):
        if hand_positions:
            for hand_pos in hand_positions:
                dx = hand_pos[0] - particle.x  
                dy = hand_pos[1] - particle.y  
                distance = math.sqrt(dx * dx + dy * dy)
                
                if distance > 0:
                    particle.vx += (dx / distance) * particle.attraction_strength 
                    particle.vy += (dy / distance) * particle.attraction_strength  
        else:
            
            particle.vx += random.uniform(-0.1, 0.1)
            particle.vy += random.uniform(-0.1, 0.1)
            
        speed = math.sqrt(particle.vx * particle.vx + particle.vy * particle.vy)
        if speed > particle.max_speed:
            particle.vx = (particle.vx / speed) * particle.max_speed
            particle.vy = (particle.vy / speed) * particle.max_speed

        particle.x += particle.vx
        particle.y += particle.vy

        particle.x = particle.x % self.width
        particle.y = particle.y % self.height

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            ret, frame = self.cap.read()
            if not ret:
                continue

            self.hand_positions = self.detect_hands(frame)

            self.screen.fill(self.BLACK)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = np.rot90(frame)
            frame = pygame.surfarray.make_surface(frame)
            self.screen.blit(frame, (0, 0))

            for particle in self.particles:
                self.update_particle(
                    particle, 
                    self.hand_positions if self.hand_positions else None
                )
                pygame.draw.circle(
                    self.screen,
                    particle.color,
                    (int(particle.x), int(particle.y)),
                    particle.size
                )

            pygame.display.flip()
            self.clock.tick(60)

        self.cap.release()
        self.hands.close()
        pygame.quit()

if __name__ == "__main__":
    system = HandParticleSystem()
    system.run()