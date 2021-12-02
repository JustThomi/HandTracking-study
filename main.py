import pygame
import cv2
from hand_detector import Hand_detector

pygame.init()

FPS = 60
WIDTH, HIGHT = (600, 600)
WIN = pygame.display.set_mode((WIDTH, HIGHT))


def draw(nodes):
    WIN.fill("black")
    for n in nodes:
        pygame.draw.rect(WIN, (255, 255, 255), n)
    pygame.display.update()

def init_nodes(nodes):
    for i in range(21):
        node = pygame.Rect(WIDTH/2, WIDTH/2, 20, 20)
        nodes.append(node)

def main():
    run = True
    clock = pygame.time.Clock()

    detector = Hand_detector()
    cap = cv2.VideoCapture(0)
    nodes = []

    init_nodes(nodes)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        success, img = cap.read()
        
        try:
            coordonates = detector.get_landmarks(img)
            for index, coords in enumerate(coordonates):
                nodes[index].x = abs(coords[0] - WIDTH)
                nodes[index].y = coords[1]
        except: 
            print("Capture failed")

        draw(nodes)

    pygame.quit()


if __name__ == "__main__":
    main()