import statistics
import random
print('Hello friend! This is a simple calculator created by Dankkuz')
print('')
def start(happy, sad):
    
    while True:
        try:
            print('Continue, press 1')
            print('Quit, press 2')
            print('')
            command = int(input('Command: '))
            if command == 1:
                choose_command()
            elif command == 2:
                print('You sure?')
                print('1: Yes, 2: No')
                command = int(input('-> '))
                if command == 1:
                    print(random.choice(sad))
                    break
                elif command == 2:
                    print(random.choice(happy))
            
        except ValueError:
            print(f"This calculator cannot recognize the command you tried to give.")
            print(f'Try again.')
            print(' ')
            
def choose_command():
    print('1: Addition, 2: Substraction, 3: Multiplication, 4: Division')
    command = int(input('-> '))
    if command == 1:
        addition()
    elif command == 2:
        substraction()
    elif command == 3:
        multiplication()
    elif command == 4:
        division()

def addition():
    answer = 0
    count = 0
    mean = []
    print('-Addition-')
    print('Give a number, enter "00" to calculate')
    while True:
        inputnumber = int(input('-> '))
        if inputnumber == 00:
            print(f'={answer}')
            print(' ')
            print('Show mean and mode? 1: Yes, 2: No')
            showmean = int(input('-> '))
            if showmean == 1:
                print(f'mean = {(answer/count)}')
                print(f'mode = {statistics.mode(mean)}')
                print(' ')
                break
            else:
                break
        else:
            answer += inputnumber
            count += 1
            mean.append(inputnumber)
        
def substraction():
    print('-Substraction-')
    print('Give a number, enter "00" to calculate')
    answer = int(input('-> '))
    while True:
        inputnumber = int(input('-> '))
        if inputnumber == 00:
            print(f'={answer}')
            print(' ')
            break
        else:
            answer -= inputnumber

def multiplication():
    mode = []
    print('-Multiplication-')
    print('Give a number, enter "00" to calculate')
    answer = int(input('-> '))
    while True:
        inputnumber = int(input('-> '))
        if inputnumber == 00:
            print(f'={answer}')
            print(' ')
            print('Show mode? 1: Yes, 2: No')
            showmode = int(input('-> '))
            if showmode == 1:
                print(f'mode = {statistics.mode(mode)}')
                print(' ')
                break
            else:
                break
        else:
            answer *= inputnumber
            mode.append(inputnumber)

def division():
    mode = []
    print('-Division-')
    print('Give a number, enter "00" to calculate')
    answer = int(input('-> '))
    while True:
        inputnumber = int(input('-> '))
        if inputnumber == 00:
            print(f'={answer}')
            print(' ')
            print('Show mode? 1: Yes, 2: No')
            showmode = int(input('-> '))
            if showmode == 1:
                print(f'mode = {statistics.mode(mode)}')
                print(' ')
                break
            else:
                break
        
        else:
            answer = (answer/inputnumber)
            mode.append(inputnumber)

if __name__=="__main__":
    happy = ["I'm so grateful..", "I appreciate it!", "Much obliged :D", "Cheers!", "Much appreciated!", "I sincerely applaud you :)", "It means the world to me :)", "<3"]
    sad = [":(", "Why leave? :(", "sadge", "*cries", "If u gotta go then u gotta go...", "Please come back"]
    start(happy, sad)
