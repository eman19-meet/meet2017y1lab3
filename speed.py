speed=50
is_birthday=True
if speed<31:
    print('no ticket')
elif speed>30 and speed<51:
    print('small ticket')
    if is_birthday:
        print('small ticket'*5)
elif speed>50:
    print('big ticket')
    if is_birthday:
        print('big birthday'*5)
