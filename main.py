def startLevel():
    global Bullet
    if level == 1:
        Bullet = 5
        tiles.set_current_tilemap(tilemap("""
            level1
        """))
Bullet = 0
level = 0
info.set_life(3)
level = 1
spriteutils.set_life_image(img("""
    . . . . . . . 
        . . . 4 . . . 
        4 4 . 4 . 4 4 
        f f . 4 . f f 
        4 4 4 4 4 4 4 
        f f 4 4 4 f f 
        4 4 4 4 4 4 4 
        f f . . . f f
"""))
startLevel()
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . e 4 . . . . . . . 
            . e e e e . . e 4 . . e e e e . 
            . 4 4 4 4 . . e 4 . . 4 4 4 4 . 
            . e e e e . e 4 4 4 . e e e e . 
            . 4 4 4 4 e 4 4 4 4 4 4 4 4 4 . 
            . e e e e 4 4 e 5 4 4 e e e e . 
            . 4 4 4 4 4 e 5 5 5 4 4 4 4 4 . 
            . e e e e 4 e 5 5 5 4 e e e e . 
            . 4 4 4 4 4 e 5 5 5 4 4 4 4 4 . 
            . e e e e 4 e 5 5 5 4 e e e e . 
            . 4 4 4 4 4 e e e e 4 4 4 4 4 . 
            . e e e e e 4 4 4 4 4 e e e e . 
            . 4 4 4 4 . e e e e . 4 4 4 4 . 
            . e e e e . . . . . . e e e e . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
textBullet = textsprite.create(convert_to_text(Bullet))
textBullet.set_icon(img("""
    . 4 5 . 
        . 4 5 . 
        4 5 5 5 
        4 5 5 5 
        4 5 5 5 
        4 5 5 5 
        4 5 5 5 
        4 4 4 4
"""))