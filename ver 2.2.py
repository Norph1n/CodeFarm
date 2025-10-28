#解决了11x11地块的种植问题，同时增加了向日葵的种植
#还没有解决胶水问题
clear()
pet_the_piggy()
size = get_world_size()
num = 0
while True:
	pumpkinharvest = True
	for i in range(size):
		for j in range(size):
			x = get_pos_x()
			y = get_pos_y()
			if x <= 5 and y <= 5:#在南瓜种植区
				if get_ground_type() != Grounds.Soil:
					till()
					plant(Entities.Pumpkin)
					pumpkinharvest = False
				if can_harvest() == False:#如果不可以收获
					plant(Entities.Pumpkin)
					pumpkinharvest = False
				move(East)
			elif x <= 15 and y >= 8:#在稻草种植区
				if can_harvest():
					harvest()
				move(East)
			elif x <= 5 and y > 5 and y < 8:#在太阳花种植区
				if get_ground_type() != Grounds.Soil:
					till()
					plant(Entities.Sunflower)
				if can_harvest():
					harvest()
					plant(Entities.Sunflower)
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
	if pumpkinharvest == True:
			harvest()