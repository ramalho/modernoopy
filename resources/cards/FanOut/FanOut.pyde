"""
 * Load and Display 
 * 
 * Images can be loaded and displayed to the screen at their actual size
 * or any other size. 
 """

cards = []

def setup():
    size(1024, 576, P3D)
    global bg
    bg = loadImage('course-image-bg.png')
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    names = [r+s+'.png' for s in 'SDCH' for r in ranks]
    for name in names:
        img = loadImage(name)
        print(img.width)
        cards.append(img)
    noLoop()


def draw():
    background(bg)
    rot_step = PI/2/len(cards)
    translate(30, 490, 0)
    rotate(-rot_step * 40)
    for i, card in enumerate(cards):
        rotate(rot_step)
        translate(19, 0, 0)
        image(card, 0, 0, card.width*.66, card.height*.66)
    save('course-image.png')
