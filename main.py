import random

class Pokemon:
    def __init__(self, name, type, max_hp, moves):
        self.name = name
        self.type = type
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.moves = moves
    
    def take_damage(self, damage):
        self.current_hp -= damage
        if self.current_hp < 0:
            self.current_hp = 0
    
    def is_fainted(self):
        return self.current_hp <= 0

class Move:
    def __init__(self, name, type, damage):
        self.name = name
        self.type = type
        self.damage = damage

def battle(pokemon1, pokemon2):
    print(f"A wild {pokemon2.name} appears!")
    player_pokemon = pokemon1
    enemy_pokemon = pokemon2
    
    while True:
        print(f"\nYour {player_pokemon.name} - HP: {player_pokemon.current_hp}/{player_pokemon.max_hp}")
        print(f"Wild {enemy_pokemon.name} - HP: {enemy_pokemon.current_hp}/{enemy_pokemon.max_hp}")
        print("\nMoves:")
        for i, move in enumerate(player_pokemon.moves):
            print(f"{i + 1}. {move.name}")
        
        choice = int(input("Choose a move (1/2/3/4): "))
        player_move = player_pokemon.moves[choice - 1]
        enemy_move = random.choice(enemy_pokemon.moves)
        
        print(f"\nYour {player_pokemon.name} used {player_move.name}!")
        enemy_pokemon.take_damage(player_move.damage)
        
        if enemy_pokemon.is_fainted():
            print(f"Wild {enemy_pokemon.name} fainted!")
            break
        
        print(f"Wild {enemy_pokemon.name} used {enemy_move.name}!")
        player_pokemon.take_damage(enemy_move.damage)
        
        if player_pokemon.is_fainted():
            print(f"Your {player_pokemon.name} fainted!")
            break

if __name__ == "__main__":
    # Define moves
    tackle = Move("Tackle", "Normal", 10)
    ember = Move("Ember", "Fire", 15)
    vine_whip = Move("Vine Whip", "Grass", 12)
    water_gun = Move("Water Gun", "Water", 13)
    
    # Create Pokémon
    charmander = Pokemon("Charmander", "Fire", 50, [tackle, ember])
    bulbasaur = Pokemon("Bulbasaur", "Grass", 55, [tackle, vine_whip])
    squirtle = Pokemon("Squirtle", "Water", 45, [tackle, water_gun])
    
    # Start battle
    player_pokemon = charmander  # You can choose your starting Pokémon here
    wild_pokemon = random.choice([bulbasaur, squirtle])
    
    battle(player_pokemon, wild_pokemon)
