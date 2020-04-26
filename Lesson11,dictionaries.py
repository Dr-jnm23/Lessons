## list of students from previous lesson
students = {'Alice':26, 'Bob':27, 'Claire':17, 'Dan':21 , 'Emma':22}

# Now two named elements
students2 = {'name':{'John','Paul','George','Ringo'},'age': {'22', '23', '24', '25'}}

# get age
students2.get('age')

##Cinema

films = {
    'Finding Dory':[3,5],
    'Bourne':[18,5],
    'Tarzan':[15,5],
    'Ghostbusters':[12,5]
    }

while True:
    choice = input('what film would you like to watch? ').strip()

    if choice in films:
        # check user age
        age = int(input('how old are you? ').strip())

        if age >=films[choice][0]:

        # check seats
            num_seats = films[choice][1]

            if num_seats>0:
                print('enjoy the film!')
                films[choice][1] = films [choice][1]-1
            else:
                print('sorry we are sold out')
        else:
            print('you are too young to see that film')
    else:
        print('we dont have that film...')