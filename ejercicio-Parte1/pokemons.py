pokemons = ["audino","bagon","baltoy","banette","bidoof","braviary","bronzor","carracosta","charmeleon","cresselia","croagunk","darmanitan","deino","emboar","emolga","exeggcute","gabite","girafarig","gulpin","haxorus","heatmor","heatran","ivysaur","jellicent","jumpluff","kangaskhan","kricketune","landorus","ledyba","loudred","lumineon","lunatone","machamp","magnezone","mamoswine","nosepass","petilil","pidgeotto","pikachu","pinsir","poliwrath","poochyena","porygon2","porygonz","registeel","relicanth","remoraid","rufflet","sableye","scolipede","scrafty","seaking","sealeo","silcoon","simisear","snivy","snorlax","spoink","starly","tirtouga","trapinch","treecko","tyrogue","vigoroth","vulpix","wailord","wartortle","whismur","wingull","yamask"]

max_pokemons = []
current_pokemon = []

def get_next_pokemon(lPokemons, lastLetter):
	for index, pokemon in enumerate(lPokemons):
		if pokemon[0] == lastLetter:
			return index	
	return False

for pokemon in pokemons:
	current_pokemon.append(pokemon)
 
	copy_pokemons = pokemons[:]
	copy_pokemons.pop(pokemons.index(pokemon))

	index_next_pokemon = get_next_pokemon(copy_pokemons, pokemon[-1])
 
	while index_next_pokemon is not False:		
		current_pkm = copy_pokemons[index_next_pokemon]
		current_pokemon.append(current_pkm)
		copy_pokemons.pop(index_next_pokemon)
 
		index_next_pokemon = get_next_pokemon(copy_pokemons, current_pkm[-1])
 
 	if len(current_pokemon) > len(max_pokemons):
		max_pokemons = current_pokemon
	current_pokemon = []

print(max_pokemons)