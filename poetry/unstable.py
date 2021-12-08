# Unstable

states = {'solid' : 'brick', 'liquid' : 'sea', 'gas' : 'alkane'}

if time.state == states['solid']:
    me.carry(time)

if time.state == states['liquid']:
    me.remind('happy days')

if time.state == states['gas']:
    room.state = 'flammable'
