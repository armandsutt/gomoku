import pygame

class Sounds:
    
    def play_move_sound():
        pygame.mixer.music.load("PUNCH.mp3")
        pygame.mixer.music.play()