k= float(input())

total_c= int(k * 100)

garrafa_1L= 100
garrafa_1_2L= 50
garrafa_033L= 33
garrafa_020L= 20

num_1L= total_c // garrafa_1L
resto= total_c % garrafa_1L

num_1_2L= resto // garrafa_1_2L
resto= resto % garrafa_1_2L

num_033L= resto // garrafa_033L
resto= resto % garrafa_033L

num_020L= resto // garrafa_020L
resto= resto % garrafa_020L

print(f"Garrafas necessarias: {num_1L} de 1L, {num_1_2L} de 1/2L, {num_033L} de 0,33L e {num_020L} de 0,20L.")