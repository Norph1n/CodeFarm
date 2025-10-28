clear()
while True:#种植
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
				plant(Entities.Bush)
				if get_water() <= 0.2 and num_items(Items.Water)>=5:#查询地块含水量
					use_item(Items.Water)
				move(East)
		move(North)
	do_a_flip()
	
