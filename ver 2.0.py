#实现了分区块种植南瓜，稻草，树木，萝卜
#无法解决南瓜收获过快问题，收益太小
#还未解决浇水，施肥问题
clear()
pet_the_piggy()
size = get_world_size()
while True:
	for i in range(size):
		for j in range(size):
			x = get_pos_x()
			y = get_pos_y()
			if x <= 3 and y <= 3:#在南瓜种植区
				if get_ground_type() != Grounds.Soil:
					till()
					plant(Entities.Pumpkin)
				if can_harvest():#如果可以收获
					harvest()#收获
					plant(Entities.Pumpkin)
				else:
					plant(Entities.Pumpkin)
				move(East)
			elif x <= 3 and y >= 3:#在稻草种植区
				if can_harvest():
					harvest()
				move(East)
			else:#在萝卜树混种区
				if (x+y)%2 == 0:#该种树了老乡
					if can_harvest():
						harvest()
						plant(Entities.Tree)
					move(East)
				else:#不是种树？那就种胡萝卜
					if get_ground_type() != Grounds.Soil:
						till()#耕地
						plant(Entities.Carrot)
					if can_harvest():
						harvest()
						plant(Entities.Carrot)
					move(East)
		move(North)
	pet_the_piggy()