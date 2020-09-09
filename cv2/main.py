from features import show_webcam, resize, mirroring, rotating

print('Hi! Welcome')
counter = 0
while True:
    print('Do you want a mirror image?')
    g = input('Press 1 for yes, 0 for no. Enter: ')
    if g == '1':
        mirror = True
    else:
        mirror = False

    show_webcam(mirror,counter)

    print('Functions on the picture')
    print('Press 1 for resizing')
    print('Press 2 for mirroring')
    print('Press 3 for rotating')
    answer = int(input('Enter choice: '))

    if answer==1:
        # resize
        resize(counter)
    elif answer==2:
        # mirror
        mirroring(counter)
    elif answer==3:
        # rotate
        rotating(counter)
    else:
        print('wrong choice')

    counter += 1

    print('Do you want another picture?')
    m = input('Enter y for yes and n for no. Enter: ')
    if m == 'y':
        continue
    elif m == 'n':
        break