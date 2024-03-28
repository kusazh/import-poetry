# Darkroom

me.darkroom.location = village.position[23]
you.darkroom.location = village.position[24]
moonlight.drop()
you.see('desire')

you.darkroom.items.append('grape')
shadow.dry(grape)
you.scent = 'fruity'

me.darkroom.item.append('secret')
secret.exposure().async()
village.see()

if you.darkroom.items == ['raisin'] and goat.name == 'scapegoat':
    secret.exposure()
