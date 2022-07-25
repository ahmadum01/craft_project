from objects import ELEMENTS_FOR_RENDER, INGREDIENTS, SLOTS
from items import Ingredient
import config

hold = None
blocked = False



    

def setup():
    size(config.screen_w, config.screen_h)
    # rectMode(CENTER)
    strokeWeight(5)
    # frameRate(30)
    
    
def draw():
    global blocked, hold
    background(255)
    
    for element in ELEMENTS_FOR_RENDER:
        element.draw()
        if element not in INGREDIENTS:
            continue
        for slot in SLOTS:
            if isinstance(element, Ingredient) and element.intersects(slot):
                element.slot = slot
                element.move_to_slot()

    

    if hold:
        hold.x = mouseX
        hold.y = mouseY
        
        
def mousePressed():
    global hold, blocked
    if blocked:
        return
    for ingredient in INGREDIENTS:
        if ingredient.cur_collision(mouseX, mouseY):
            hold = ingredient
            blocked = True


def mouseReleased():
    global blocked, hold
    hold = None
    blocked = False
