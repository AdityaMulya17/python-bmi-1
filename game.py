from hero import Hero
import hero_module

hero1 = Hero("Wira",100,100,100,100)
print(hero1.greeting())
print(hero1.get_info())
print(hero1.get_attack())

# hero2_info = hero_module.get_info_module("Wira",100,100,100,100)
# print(hero2_info)
# hero2_greeting = hero_module.greeting_module("Wira",100,100,100,100)
# print(hero2_greeting)
# hero2_get_attack = hero_module.get_attack_module("Wira",100,100,100,100)
# print(hero2_get_attack)