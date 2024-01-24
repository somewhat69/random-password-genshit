import random
length = int(input("Enter number how much you want your password to be :\n"))
choice = int(input("Press 1 to make your password only have numbers .\nPress 2 to make your password only have alphabets .\nPress 3 to make your password have numbers and alphabets . \nPress 4 to make your password have numbers , alphabets and symbols .\n"))
arr_sym = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-"]
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
i = 0
passidk = []
for i in range(length):
    rand_no_sym = random.randint(0, len(arr_sym)-1)
    rand_no_alpha = random.randint(0, len(alpha)-1)
    rand_no_num = random.randint(0, len(num)-1)
    rand_upper_or_not_in_this_iter = random.randint(0, 2)
    main_alpha = alpha[rand_no_alpha].lower(
    ) if rand_upper_or_not_in_this_iter < 1 else alpha[rand_no_alpha]
    main_num = num[rand_no_num]
    another_rand_cus_too_retarded = random.randint(0, 2)
    main_sym = arr_sym[rand_no_sym]
    if (choice == 1):
        passidk.append(str(rand_no_num))
    elif (choice == 2):
        passidk.append(main_alpha)
    elif (choice == 3):
        passidk.append(
            num[rand_no_num] if rand_upper_or_not_in_this_iter > 1 else main_alpha)
    else:
        passidk.append(main_sym if rand_upper_or_not_in_this_iter > 1 else (
            num[rand_no_num] if another_rand_cus_too_retarded > 1 else main_alpha))
print(''.join(passidk))
