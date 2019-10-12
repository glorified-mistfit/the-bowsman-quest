import turtle
import random




game_running = False

name = input("hello what is your name?")
print(" would you like to have a sword or bow", name + "?")
question = input()




    







        

        #swordman
    

if question == "sword":
    print("ok")
    print("you are now a swordsman")
    while game_running == False:
        monster = { 'attack': random.randint(1,9), 'rangeattack': random.randint(1,9), 'defense': random.randint(1,9), 'health': random.randint(1,50)}
        game_running = True
        swordsman = {'name': name, 'attack': 5, 'rangeattack': 0, 'defense': 4, 'health': 20}
        player = swordsman
        while game_running == True:
            print('monster!!!!!!!')
            print('please choose one')
            print('1) attack')
            print('2)rangeattack')
            player_choice = input()
            if player_choice == "1":
                monster['health'] = monster['health'] - player['attack']
                player['health'] = player['health'] - monster['attack']
                print('monsters health')
                print(monster['health'])
                print('players health')
                print(player['health'])
            if player_choice == "2":
                monster['health'] = monster['health'] - player['rangeattack']
                player['health'] = player['health'] - monster['rangeattack']
                print('monsters health')
                print(monster['health'])
                print('players health')
                print(player['health'])
            if player ['health'] <= 0:
                print('you died do you want to restart')
                input('y/n')
                if ('y'):
                    game_running = False
                if ('n'):
                    print('game over')
                    game_running = 1
                else:
                    print('game over')
                    game_running = 1
            if monster ["health"] <= 0 and player ['health'] >= 0:
                print ('oh no!!!! a new')
                game_running = False







        #bowsman
        

if question == "bow":
    print("ok")
    print("you are now a bowsman")
    while game_running == False:
        monster = { 'attack': random.randint(1,9), 'rangeattack': random.randint(1,9), 'defense': random.randint(1,9), 'health': random.randint(1,50)}
        game_running = True
        bowsman = {'name': name, 'attack': 3, 'rangeattack': 8, 'defense': 3, 'health': 20}
        player = bowsman
        while game_running == True:
            print('monster!!!!!!!')
            print('please choose one')
            print('1) attack')
            print('2)rangeattack')
            player_choice = input()
            if player_choice == "1":
                monster['health'] = monster['health'] - player['attack']
                player['health'] = player['health'] - monster['attack']
                print('monsters health')
                print(monster['health'])
                print('players health')
                print(player['health'])
            if player_choice == "2":
                monster['health'] = monster['health'] - player['rangeattack']
                player['health'] = player['health'] - monster['rangeattack']
                print('monsters health')
                print(monster['health'])
                print('players health')
                print(player['health'])
            if player ['health'] <= 0:
                print('you died do you want to restart')
                input('y/n')
                if ('y'):
                    game_running = False
                if ('n'):
                  print('game over')
                  game_running = 1
                else:
                    print('game over')
                    game_running = 1
            if monster ["health"] <= 0 and player ['health'] >= 0:
                print ('oh no!!!! a new')
                game_running = False

