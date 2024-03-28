# iFruit Ru2Guo3

if ifruit_tree.fruit(ifruit):
    if you in ifruit_garden and me in ifruit_garden:
        if ifruit.hit(you) or ifruit.hit(me):
            if ifruit.taste == 'bitter':
                if you.collect(ifruit):
                    pass
                elif me.eat(ifruit):
                    you.collect(ifruit.core)
