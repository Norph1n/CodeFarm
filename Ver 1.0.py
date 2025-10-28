#实现了一行灌木，一行萝卜，并且检测水量进行浇水
clear()
for i in range(get_world_size()):
	if i%2 == 0:#在奇数行
		for j in range(get_world_size()):
			harvest()
			till()
			move(East)
		do_a_flip()#后空翻
		move(North)#运行完这一行，向上走一格
	else:#在偶数行
		pet_the_piggy()#摸摸小猪
		move(North)#向上走两格		
while True:#种植
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if i%2 == 0:#如果在奇数行
				if can_harvest():#如果能收获
					harvest()#收获
					plant(Entities.Carrot)#种植萝卜
					if get_water() <= 0.2 and num_items(Items.Water)>=5:#查询地块含水量
						use_item(Items.Water)
					move(East)
				elif get_entity_type() == None:#如果什么都没有
					plant(Entities.Carrot)#种萝卜
					if get_water() <= 0.2 and num_items(Items.Water)>=5:#查询地块含水量
						use_item(Items.Water)
					move(East)
				else:
					do_a_flip()#如果有作物，做一次翻转
			else:#如果在偶数行
				if can_harvest():
					harvest()#收获
					plant(Entities.Bush)#种植灌木
					if get_water() <= 0.2 and num_items(Items.Water)>=5:#查询地块含水量
						use_item(Items.Water)
					move(East)
				else:
					do_a_flip()
		move(North)
	do_a_flip()
	