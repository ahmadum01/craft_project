from objects import ELEMENTS_FOR_RENDER, INGREDIENTS, SLOTS
from items import Ingredient
from objects import crafting_button
import config
from tools import group_ingredients
from helpers import check_move_to_back, check_affiliation_ingredient

hold = None
blocked = False


def setup():
    size(config.screen_w, config.screen_h)
    # rectMode(CENTER)
    strokeWeight(5)
    frameRate(60)
    
    
def draw():
    global blocked, hold
    background(255)
    
    for element in ELEMENTS_FOR_RENDER:
        element.draw()
        if not isinstance(element, Ingredient):
            continue
        for slot in SLOTS:
            if element.intersects(slot) and not check_affiliation_ingredient(element, slot):
                element.move_to_back()
            
            elif element.intersects(slot):
                element.slot = slot
                if element not in slot.items:
                    slot.items.append(element)
                element.move_to_slot()
                
            elif not check_move_to_back(element):
                element.move_to_back()
                try:
                    slot.items.remove(element)
                except:
                    pass

    if hold:
        hold.x = mouseX
        hold.y = mouseY
        
        
def mousePressed():
    global hold, blocked
    
    if crafting_button.cur_collision(mouseX, mouseY):
        crafting_button.run()
        crafting_button.set_pressed_color()
    
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
    
    crafting_button.set_default_color()

    
    
    
