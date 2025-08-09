import pygame

print('Janela Iniciada')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Janela Termino')

print('Loop Start')
while True:
    # Check all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Close window
            quit()
