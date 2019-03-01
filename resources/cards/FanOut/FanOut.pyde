"""
 * Load and Display 
 * 
 * Images can be loaded and displayed to the screen at their actual size
 * or any other size. 
 """

cards = []

def setup():
    size(1024, 576)
    #global bg
    #bg = loadImage('course-image-bg.png')
    img = loadImage('2S.png')    # Load the image into the program
    cards.append(img)
    #noLoop()


def draw():
    #background(bg)
    img = cards[0]
    image(img, 0, height / 2, img.width / 2, img.height / 2)
