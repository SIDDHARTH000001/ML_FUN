import cv2
import numpy as np
import pygame
import random
import math
from pygame.locals import *

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.uniform(2, 4)
        self.size = random.randint(2, 4)
        self.color = (135, 206, 235)  # Light blue for air particles

class AerodynamicVisualizer:
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Aerodynamic Visualization")
        
        # Initialize camera
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, self.width)
        self.cap.set(4, self.height)
        
        # Initialize particles
        self.particles = []
        self.init_particles()
        
        # Colors
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 0, 255)
        self.BLACK = (0, 0, 0)
        
        self.clock = pygame.time.Clock()
        
    def init_particles(self):
        """Initialize air flow particles"""
        for _ in range(500):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            self.particles.append(Particle(x, y))
    
    def detect_shape(self, frame):
        """Detect shapes in the camera frame"""
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)
        
        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        if contours:
            # Get the largest contour
            largest_contour = max(contours, key=cv2.contourArea)
            
            # Approximate the shape
            epsilon = 0.02 * cv2.arcLength(largest_contour, True)
            approx = cv2.approxPolyDP(largest_contour, epsilon, True)
            
            # Identify shape based on number of vertices
            vertices = len(approx)
            
            if vertices == 3:
                return "pyramid", approx
            elif vertices > 6:
                return "cylinder", approx
                
        return None, None
    
    def update_particles(self, shape_type, shape_contour):
        """Update particle positions based on shape"""
        for particle in self.particles:
            # Basic movement
            particle.x += particle.speed
            
            # Reset particles that go off screen
            if particle.x > self.width:
                particle.x = 0
            
            # If shape detected, adjust particle movement
            if shape_type and shape_contour is not None:
                point = (int(particle.x), int(particle.y))
                distance = cv2.pointPolygonTest(shape_contour, point, True)
                
                # Deflect particles near the shape
                if -50 < distance < 0:
                    if shape_type == "pyramid":
                        # Flow around pyramid
                        particle.y += random.uniform(-2, 2)
                        particle.speed *= 1.1  # Accelerate around tip
                    elif shape_type == "cylinder":
                        # Smooth flow around cylinder
                        particle.y += random.uniform(-1, 1)
                        
                # Prevent particles from entering the shape
                if distance >= 0:
                    particle.x -= particle.speed * 2
                    particle.y += random.uniform(-3, 3)
    
    def run(self):
        """Main loop"""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            
            # Get camera frame
            ret, frame = self.cap.read()
            if not ret:
                continue
                
            # Mirror the frame
            frame = cv2.flip(frame, 1)
            
            # Detect shape
            shape_type, shape_contour = self.detect_shape(frame)
            
            # Clear screen
            self.screen.fill(self.BLACK)
            
            # Draw camera frame
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = np.rot90(frame)
            frame = pygame.surfarray.make_surface(frame)
            self.screen.blit(frame, (0, 0))
            
            # Update and draw particles
            self.update_particles(shape_type, shape_contour)
            for particle in self.particles:
                pygame.draw.circle(
                    self.screen,
                    particle.color,
                    (int(particle.x), int(particle.y)),
                    particle.size
                )
            
            # Draw shape outline if detected
            if shape_contour is not None:
                points = shape_contour.reshape(-1, 2)
                pygame.draw.polygon(self.screen, self.BLUE, points, 2)
            
            pygame.display.flip()
            self.clock.tick(60)
        
        # Cleanup
        self.cap.release()
        pygame.quit()

if __name__ == "__main__":
    visualizer = AerodynamicVisualizer()
    visualizer.run()