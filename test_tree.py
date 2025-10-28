#找格子
clear()
do_a_flip()
size = get_world_size()
type = get_ground_type()
while True:
	for i in range(size):
		for j in range(size):
			x = get_pos_x()
			y = get_pos_y()
			if (x+y)%2 == 0:#如果在的格子编号之和为偶数
				#print(x,y)
				if can_harvest():
					harvest()
				#else:
					#do_a_flip()
				plant(Entities.Tree)#种一棵树
				move(East)#向右走一格
			else:
				move(East)#向右走一格
		move(North)#循环结束，向上走一格
	pet_the_piggy()