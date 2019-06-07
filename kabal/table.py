import sys
from pathlib import Path

import pygame

from .deck import Card, Deck

pygame.init()

size = (640, 480)
width, height = size
black = (0, 0, 0)

screen = pygame.display.set_mode(size)


def get_card_image(card: Card):
    folder = Path("boardgamePack_v2/PNG/Cards")
    shortrank = card.rank[0] if card.rank.isalpha() else card.rank
    filename = f"card{card.suit}{shortrank}.png"
    imagefile = folder / filename
    if not imagefile.is_file():
        raise FileNotFoundError(str(imagefile))
    return pygame.image.load(str(imagefile)).convert()


def main():
    screen.fill(black)

    deck = Deck()
    deck.shuffle()

    tl = (20, 20)
    w = 140 // 3
    h = 190 // 3
    corner_rect = pygame.Rect(tl, (w, h))

    for idx, card in enumerate(deck):
        row, col = divmod(idx, 10)
        print(f"{card} at ({row}, {col})")

        image = pygame.transform.scale(get_card_image(card), (w, h))

        target_rect = corner_rect.move(col * (w + 1), row * (h + 1))
        screen.blit(image, target_rect)

    pygame.display.flip()
    quitted = False
    while not quitted:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    main()
