# Global Scope

player_health = 10

# TODO: 1 Global Scope
def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

game()

# There is no Block Scope

if 3 > 2:
    a_variable = 10


# Modifying Global Scope

enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"Inside Enemies: {enemies}")

increase_enemies()
print(f"Outside  Enemies: {enemies}")

enemies = 1

def increase_enemies():
    print(f"Inside Enemies {enemies}")
    return enemies + 10

enemies = increase_enemies()

print(f"Outside Enemies: {enemies}")
