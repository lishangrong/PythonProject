"""
案例：演示Python的多态案例之 战斗平台。
需求：
1. 构建对战平台(公共的函数) object_play(), 接受：英雄机 和 敌机
2. 在不修改对战平台代码的情况下，完成多次战斗
3.规则：
    影响及，1代战斗力为60， 2代战斗力为80
    敌机：1代战斗力70
代码提示：
英雄机1代： HeroFighter
英雄机2代： AdvHeroFighter
敌机： EnemyFighter
"""
class HeroFighter:
    def power(self):
        return 60

class AdvHeroFighter(HeroFighter):
    def power(self):
        return 80

class EnemyFighter:
    def power(self):
        return 70

def object_play(hero, enemy):
    # 参1：英雄机， 参2：敌机
    if hero.power() >= enemy.power():
        print("英雄机 战胜了 敌机")
    else:
        print("英雄机 惜败 敌机")


#
if __name__ == '__main__':
    # 思路1：不使用多态，完成对战
    #场景1：英雄机1代 VS 敌机1代
    h1 = HeroFighter()
    e1 = EnemyFighter()
    if h1.power() >= e1.power():
        print("英雄机1代 战胜了 敌机1代")
    else:
        print("英雄机1代 惜败 敌机1代")

    print('-' * 23)
    #场景2：英雄机2代 VS 敌机1代
    h2 = AdvHeroFighter()
    e1 = EnemyFighter()
    if h2.power() >= e1.power():
        print("英雄机2代 战胜了 敌机1代")
    else:
        print("英雄机2代 惜败 敌机1代")

    print('-' * 23)

    # 思路2：使用多态，完成对战
    h1 = HeroFighter()
    h2 = AdvHeroFighter()
    e1 = EnemyFighter()
    # 场景1 ：英雄机1代 VS 敌机1代
    object_play(h1, e1)
    # 场景2 ：英雄机2代 VS 敌机1代
    object_play(h2, e1)

    print('-' * 23)
    # object_play(h2, h1) # object_play 参数添加类型后，该段代码出现警告

