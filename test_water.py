clear()
for i in range(get_world_size()):
	if get_water() <= 0.25 and num_items(Items.Water)>=5:
		use_item(Items.Water)
