# Darkroom

my_darkroom.location = village.position[23]
your_darkroom.location = village.position[24]
moonlight.drop()
you.see('desire')

your_darkroom.item.append('grape')
shadow.dry(grape)
you.scent = 'fruity'

my_darkroom.item.append('secret')
secret.exposure().async()
village.see()

if your_darkroom.item == ['raisin'] and goat == 'scapegoat':
    secret.exposure()
