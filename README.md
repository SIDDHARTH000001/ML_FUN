# Project: Particle Swarm with Hand Tracking
# PSO.py

## Description
This project combines computer vision and particle swarm optimization (PSO) to create an interactive visual experience. Using MediaPipe for hand tracking and OpenCV for visualization, the system detects a user's hands through a webcam and generates particle effects that are naturally attracted to hand positions.

![Hand Tracking PSO Demo](Source/demo_PSO.gif)

### Key Features
- Real-time hand tracking with MediaPipe's hand landmark detection
- Dynamic particle swarm simulation with customizable parameters
- Particles exhibit natural swarming behavior, accelerating toward hand positions
- Visual effects including particle trails, color changes based on velocity, and size variations

### Technical Implementation
- MediaPipe's hand landmark detection to precisely locate hand positions in space
- Custom PSO algorithm to guide particle movement with natural-looking acceleration and momentum
- OpenCV for rendering the visual elements and compositing onto the webcam feed

# Project: Air Flow Dynamics Simulator
# game.py

![Hand Tracking PSO Demo](Source/Game_Air_Flow_Dynamics_Simulator.gif)

## Description
This interactive simulator visualizes air particle flow dynamics around user-created objects. Using a webcam to detect shapes formed by the user's hands or objects, the system demonstrates how air particles behave when encountering different geometric shapes, creating an intuitive and educational demonstration of basic fluid dynamics.

### Key Features
- Real-time particle system that mimics air flow patterns
- Detection of user-created shapes (circles, triangles) via computer vision
- Realistic particle deflection and turbulence around obstacles
- Visual representation of pressure zones and flow velocity through particle density and color

### Technical Implementation
- Shape detection algorithms to identify user-created obstacles
- Physics-based particle system that simulates simplified fluid dynamics
- Color-mapping to represent different flow characteristics (speed, pressure, turbulence)
- Interactive feedback where changes to shapes immediately affect the particle flow pattern
