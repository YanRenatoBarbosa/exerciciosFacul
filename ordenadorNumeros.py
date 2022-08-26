#Ordena 3 números diferentes indicados pelo user

num_target_list = []
num_aux_list = []

print('Digite 3 números inteiros diferentes! \n\n')

while len(num_target_list) < 3:
    num_target = int(input("Digite um número: "))
    num_target_list.append(num_target)

cont = 0
while cont < len(num_target_list):
    if cont != 0:
        print('cont', cont)
        print(num_target_list[cont - 1])
        print(num_target_list)

        #if (num_aux_list[cont - 1]) <= num_target_list[cont]:
#            num_aux_list.insert((len(num_aux_list) - 1), num_target_list[cont])

        # 7,8,1

        print(num_aux_list)

    else:
        num_aux_list.append(num_target_list[cont])

    cont = cont + 1
