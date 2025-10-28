#第1行种草，2~4行中灌木，5~6行种萝卜
clear()
#耕地
size = get_world_size()
for i in range(size - 2):
	move(North)
for j in range(2):
	for k in range(size):
		till()
		move(East)
	move(North)
while num_items(Items.Hay) >= 2000 and num_items(Items.Wood) >= 2000:
	for i in range(size):
		y = get_pos_y()
		water = get_water()
		for j in range(size):
			if y == 0 or y == 1:
				if can_harvest():
					harvest()
					if water <= 0.2 and num_items(Items.Water) >= 1000:
						use_item(Items.Water)
					move(East)
			elif y == 2 or y == 3:
				if  can_harvest():
					harvest()
					plant(Entities.Bush)
					if water <= 0.2 and num_items(Items.Water) >= 1000:
						use_item(Items.Water)
					move(East)
			else:
				if can_harvest():
					harvest()
					plant(Entities.Carrot)
					if water <= 0.2 and num_items(Items.Water) >= 1000:
						use_item(Items.Water)
					move(East)
				else:
					plant(Entities.Carrot)
					if water <= 0.2 and num_items(Items.Water) >= 1000:
						use_item(Items.Water)
					move(East)
				
		move(North)	
	#pet_the_piggy()

		