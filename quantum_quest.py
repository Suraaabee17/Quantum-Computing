import pygame
import sys
from qiskit import QuantumCircuit, execute
from qiskit.providers.aer import Aer

# Initialize pygame
pygame.init()

# Set up the display with a larger size
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Quantum Quest')

# Load images (Replace with your actual file paths)
coral_clusters_img = pygame.image.load('/path/to/coral_clusters_img.webp')
sunken_ship_img = pygame.image.load('/path/to/sunken_ship_img.webp')
seaweed_forest_img = pygame.image.load('/path/to/seaweed_forest_img.webp')
echo_caves_img = pygame.image.load('/path/to/echo_caves_img.webp')
teleportation_trench_img = pygame.image.load('/path/to/teleportation_trench_img.webp')
circuit_reef_img = pygame.image.load('/path/to/circuit_reef_img.webp')
bloch_sphere_img = pygame.image.load('/path/to/bloch_sphere_img.webp')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define font
font = pygame.font.Font(None, 28)  # Adjust font size to fit text better

# Define game states
INTRO, STATION1, STATION2, STATION3, STATION4, STATION5, STATION6, STATION7 = range(8)

# Initial game state
state = INTRO

def draw_text(text, x, y, max_width):
    words = text.split(' ')
    lines = []
    current_line = ''
    for word in words:
        if font.size(current_line + word)[0] < max_width:
            current_line += word + ' '
        else:
            lines.append(current_line)
            current_line = word + ' '
    lines.append(current_line)

    for i, line in enumerate(lines):
        text_surface = font.render(line, True, WHITE)
        screen.blit(text_surface, (x, y + i * font.get_linesize()))

def handle_intro():
    screen.fill(BLACK)
    draw_text("Welcome to Quantum Quest!", 100, 100, 800)
    draw_text("Press 1 to Start the Adventure", 100, 200, 800)
    draw_text("Did You Know?", 100, 300, 800)
    draw_text("Quantum mechanics explains the behavior of particles at the atomic level.", 100, 350, 800)

def handle_station1():
    screen.blit(coral_clusters_img, (0, 0))
    draw_text("Station 1: Coral Clusters", 100, 50, 800)
    draw_text("Puzzle: Fill in the corresponding density matrices for these states.", 100, 100, 800)
    draw_text("Press 1 for Cluster A, 2 for Cluster B, 3 for Cluster C", 100, 150, 800)
    draw_text("Did You Know?", 100, 250, 800)
    draw_text("Quantum superposition allows particles to be in multiple states at once.", 100, 300, 800)

def handle_station2():
    screen.blit(sunken_ship_img, (0, 0))
    draw_text("Station 2: The Sunken Ship", 100, 50, 800)
    draw_text("Puzzle: Decide which states to use to maximize security.", 100, 100, 800)
    draw_text("Did You Know?", 100, 200, 800)
    draw_text("Quantum entanglement means particles can be connected no matter the distance.", 100, 250, 800)

def handle_station3():
    screen.blit(seaweed_forest_img, (0, 0))
    draw_text("Station 3: The Entangled Seaweed Forest", 100, 50, 800)
    draw_text("Puzzle: Predict the state of the second qubit.", 100, 100, 800)
    draw_text("Did You Know?", 100, 200, 800)
    draw_text("A qubit is the basic unit of quantum information, similar to a bit in classical computing.", 100, 250, 800)

def handle_station4():
    screen.blit(echo_caves_img, (0, 0))
    draw_text("Station 4: The Echo Caves", 100, 50, 800)
    draw_text("Puzzle: Predict whether settings will violate Bell's inequality.", 100, 100, 800)
    draw_text("Did You Know?", 100, 200, 800)
    draw_text("Bell's theorem shows that quantum mechanics predictions can't be explained by local realism.", 100, 250, 800)

def handle_station5():
    screen.blit(teleportation_trench_img, (0, 0))
    draw_text("Station 5: The Teleportation Trench", 100, 50, 800)
    draw_text("Puzzle: Describe the steps to teleport a quantum state.", 100, 100, 800)
    draw_text("Did You Know?", 100, 200, 800)
    draw_text("Quantum teleportation transfers a particle's state to another particle at a distance.", 100, 250, 800)

def handle_station6():
    screen.blit(circuit_reef_img, (0, 0))
    draw_text("Station 6: The Circuit Reef", 100, 50, 800)
    draw_text("Puzzle: Create a quantum half-adder circuit.", 100, 100, 800)
    draw_text("Did You Know?", 100, 200, 800)
    draw_text("Quantum circuits use qubits and quantum gates to perform operations.", 100, 250, 800)

def handle_station7():
    screen.blit(bloch_sphere_img, (0, 0))
    draw_text("Station 7: The Bloch Sphere Bubble", 100, 50, 800)
    draw_text("Puzzle: Calculate the coordinates on the Bloch sphere.", 100, 100, 800)
    draw_text("Did You Know?", 100, 200, 800)
    draw_text("The Bloch sphere visually represents the state of a single qubit.", 100, 250, 800)

def run_quantum_circuit():
    # Create a quantum circuit with one qubit
    qc = QuantumCircuit(1, 1)
    qc.h(0)  # Apply a Hadamard gate to qubit 0
    qc.measure(0, 0)  # Measure qubit 0
    
    # Use the Aer simulator
    simulator = Aer.get_backend('qasm_simulator')
    
    # Execute the circuit on the simulator
    result = execute(qc, simulator).result()
    counts = result.get_counts(qc)
    
    return counts

# Main game loop with enhanced debugging
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("Game quit by user.")
        elif event.type == pygame.KEYDOWN:
            print(f"Key pressed: {pygame.key.name(event.key)}")
            if state == INTRO:
                if event.key == pygame.K_1:
                    state = STATION1
                    print("Transition to STATION1")
            elif state == STATION1:
                if event.key == pygame.K_1:
                    state = STATION2
                    print("Transition to STATION2 from Cluster A")
                elif event.key == pygame.K_2:
                    state = STATION2
                    print("Transition to STATION2 from Cluster B")
                elif event.key == pygame.K_3:
                    state = STATION2
                    print("Transition to STATION2 from Cluster C")
            elif state == STATION2:
                if event.key == pygame.K_1:
                    state = STATION3
                    print("Transition to STATION3")
            elif state == STATION3:
                if event.key == pygame.K_1:
                    state = STATION4
                    print("Transition to STATION4")
            elif state == STATION4:
                if event.key == pygame.K_1:
                    state = STATION5
                    print("Transition to STATION5")
            elif state == STATION5:
                if event.key == pygame.K_1:
                    state = STATION6
                    print("Transition to STATION6")
            elif state == STATION6:
                if event.key == pygame.K_1:
                    state = STATION7
                    print("Transition to STATION7")
            elif state == STATION7:
                if event.key == pygame.K_1:
                    state = INTRO
                    print("Transition to INTRO")

    if state == INTRO:
        handle_intro()
        print("Displaying INTRO")
    elif state == STATION1:
        handle_station1()
        print("Displaying STATION1")
    elif state == STATION2:
        handle_station2()
        print("Displaying STATION2")
    elif state == STATION3:
        handle_station3()
        print("Displaying STATION3")
    elif state == STATION4:
        handle_station4()
        print("Displaying STATION4")
    elif state == STATION5:
        handle_station5()
        print("Displaying STATION5")
    elif state == STATION6:
        handle_station6()
        print("Displaying STATION6")
    elif state == STATION7:
        handle_station7()
        print("Displaying STATION7")

    pygame.display.flip()

    # Run a quantum circuit when in STATION3 and display the results
    if state == STATION3:
        counts = run_quantum_circuit()
        print(f"Quantum Circuit Results: {counts}")
        draw_text(f"Quantum Results: {counts}", 100, 350, 800)

pygame.quit()
print("Pygame quit.")
