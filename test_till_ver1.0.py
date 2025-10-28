clear()
for i in range(get_world_size()):
	if i%2 == 0:#在奇数行
		for j in range(get_world_size()):
			harvest()
			till()
			move(East)
		do_a_flip()
		move(North)#运行完这一行，向上走一格
	else:#在偶数行
		pet_the_piggy()
		move(North)#向上走两格
			