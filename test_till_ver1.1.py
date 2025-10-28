#只翻耕最上面行地块
clear()
size = get_world_size()
for i in range(size - 2):
	move(North)
for j in range(2):
	for k in range(size):
		till()
		move(East)
	move(North)
		


		
