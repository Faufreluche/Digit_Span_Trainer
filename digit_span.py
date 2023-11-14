# Import necessary libraries
import random
import time
import pygame
import os
import pandas as pd
import keyboard

# Set working directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Define functions

def generate_numbers_list(n):
    numbers_list = []
    for i in range(n):
        numbers_list.append(random.randint(0, 9))
    return numbers_list


def play_audio(number, sound_model):
    pygame.mixer.init()
    # set file path
    path = 'Soundmodels/' + str(sound_model) + '/'
    # get file name
    if number == 0:
        pygame.mixer.music.load(path + 'null.mp3')
    elif number == 1:
        pygame.mixer.music.load(path + 'yks.mp3')
    elif number == 2:
        pygame.mixer.music.load(path + 'kaks.mp3')
    elif number == 3:
        pygame.mixer.music.load(path + 'kolm.mp3')
    elif number == 4:
        pygame.mixer.music.load(path + 'neli.mp3')
    elif number == 5:
        pygame.mixer.music.load(path + 'viis.mp3')
    elif number == 6:
        pygame.mixer.music.load(path + 'kuus.mp3')
    elif number == 7:
        pygame.mixer.music.load(path + 'seitse.mp3')
    elif number == 8:
        pygame.mixer.music.load(path + 'kaheksa.mp3')
    elif number == 9:
        pygame.mixer.music.load(path + 'yheksa.mp3')
    
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)


# Predefine variables
os.system('cls')
status = True
mistakes_in_a_row = 0
loop_nr = 0

# Start the game
print('Welcome to digit span!')
print()

# Ask for user's name
name = input('Please enter your name ---> ')
os.system('cls')

# Get current date
current_date = time.strftime("%d/%m/%Y")

# ask for user's conditions

# Practice or testing mode, practice 1, test 2
while True:
    print('Please choose mode:')
    print()
    print('1. Practice')
    print('2. Test')
    print('3. Baastest (Benchmark)')
    print()
    print('* enter a number *')
    mode = input('---> ')
    if mode in {'1', '2', '3'}:
        break
    else:
        print("Please enter a valid option.")
        os.system('cls')
os.system('cls')

# how comfortable is the environment, 1 - not comfortable, 10 - very comfortable
while True:
    print('NOT COMFORTABLE  1--2--3--4--5--6--7--8--9--10    VERY COMFORTABLE')
    print()
    print('* enter a number *')
    location = input('How comfortable is the environment right now? ---> ')
    if location in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}:
        break
    else:
        print("Please enter a valid option.")
        os.system('cls')
os.system('cls')

# tiredness level, 1 - not tired, 10 - tired
while True:
    print('NOT TIRED  1--2--3--4--5--6--7--8--9--10    VERY TIRED')
    print()
    print('* enter a number *')
    tiredness = input('How tired are you right now? ---> ')
    if tiredness in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}:
        break
    else:
        print("Please enter a valid option.")
        os.system('cls')
os.system('cls')

# physical activity minutes
while True:
    physical_activity = input('Enter your active minutes for today ---> ')
    if physical_activity.isdigit():
        break
    else:
        print("Please enter a valid number.")
        os.system('cls')
os.system('cls')

# mental state, 1 - not focused, 10- focused
while True:
    print('NOT FOCUSED  1--2--3--4--5--6--7--8--9--10    VERY FOCUSED')
    print()
    print('* enter a number *')
    mental_state = input('How focused are you right now? ---> ')
    if mental_state in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}:
        break
    else:
        print("Please enter a valid option.")
        os.system('cls')
os.system('cls')

# motivation level, 1 - not motivated, 10 - very motivated
while True:
    print('NOT MOTIVATED  1--2--3--4--5--6--7--8--9--10    VERY MOTIVATED')
    print()
    print('* enter a number *')
    motivation = input('How motivated are you right now? ---> ')
    if motivation in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}:
        break
    else:
        print("Please enter a valid option.")
        os.system('cls')
os.system('cls')

# Ask for starting n and ensure it is a number
if mode == '3':
    n = 3
else:
    while True:
        print('Please enter starting point for digit span test.')
        print()
        print('Press ENTER for default 3 digits')
        n_input = input('...or enter a custom starting point for digit span test ---> ')
        if n_input.isdigit():
            n = int(n_input)
            break
        elif n_input == '':
            n = 3
            break
        else:
            print("Please enter a valid number.")
            os.system('cls')
        os.system('cls')
os.system('cls')    

# Ask for sound model and ensure it is a valid option
while True:
    print('Please enter sound model number:')
    print()
    print('1. Kaarel')
    print('2. Pille')
    print('3. Bot')
    print()
    print('* enter a number *')
    sound_model = input(' ---> ')
    if sound_model in {'1', '2', '3'}:
        break
    else:
        print("Please enter a valid option.")
        os.system('cls')
os.system('cls')

# ask for wait time between numbers'
if mode == '1':
    wait_time = float(input('Please enter wait time between numbers in seconds ---> '))
elif mode == '2' or mode == '3':
    wait_time = 0
os.system('cls')

# ask for memory method, 1 - no method, 2 - memory palace
if mode == '3':
    memory_method = '11'
else:
    while True:
        print('Please choose memory method that you practiced today.')
        print()
        print('Examples: 4, 7, 10 or 6')
        print()
        print('1. Repeating the audio')
        print('2. Visualizing the digits')
        print('3. Rhyming words with numbers to visualize images')
        print('4. Translating number shape to images')
        print('5. Phonetic number system to create images (1 digit at a time)')
        print('6. Phonetic number system to create images (2 digits at a time)')
        print('7. Method of Loci')
        print('8. Using absurd connections')
        print('9. Number chunking')
        print('10. Using personal connections')
        print('11. No method')
        print()
        print('* enter a number *')
        memory_method = input(' ---> ')
        break

os.system('cls')

# Display game rules
print('Rules:')
print()
print('1. You will hear a series of numbers')
print('2. After hearing the full sequence of numbers, recall the full sequence in the same order')
print('3. If you repeat the numbers correctly, the series will get longer by one digit')
print('4. If you make a mistake the first time, the digit length will stay the same. Additional mistakes will shorten the series by one digit')
print()
print('________________________')
print('Press ENTER to start')
input()
os.system('cls')

# Check if log file exists
if os.path.isfile('Logs/' + name + '_digit_span_log.csv'):
    df = pd.read_csv('Logs/' + name + '_digit_span_log.csv')
    session_nr = df['session_nr'].iloc[-1] + 1
else:
    df = pd.DataFrame(columns=['user_name', 'date', 'time', 'session_nr', 'loop_nr', 'presented_sequence', 'recalled_sequence', 'outcome', 'mistakes_in_a_row',
                               'recall_time_in_s', 'sound_model', 'digit_length', 'session_time', 'time_between_digits', 'memory_method', 'tiredness',
                               'physical_activity', 'mental_state', 'motivation', 'location', 'session_mode'])
    session_nr = 1
    
# start whole game timer
total_time_start = time.time()

# Benchmark test params
benchmark_test_loop_nr = 0

# Game loop
while status:
    loop_nr += 1
    current_loop_n = n
    benchmark_test_loop_nr += 1
    
    # Generate list of numbers
    numbers_list = generate_numbers_list(n)
    presented_sequence = ''.join(str(number) for number in numbers_list)
    presented_sequence = str(presented_sequence)

    # Disable keyboard using import keyboard
    for i in range(150):
        keyboard.block_key(i)
    
    # Play audio for all numbers in the list
    for number in numbers_list:
        play_audio(number, sound_model)
        time.sleep(wait_time)

    # Measure time
    loop_input_start_time = time.time()

    # Enable keyboard
    for i in range(150):
        keyboard.unblock_key(i)
    
    # Ask user to repeat numbers
    print('Current number length is ' + str(current_loop_n) + ' numbers.')
    print()
    print('Please repeat the numbers in one line')
    print()
    recalled_sequence = str(input(' ---> '))
    os.system('cls')
    

    # Stop time measurement
    loop_input_end_time = time.time()
    time_taken_loop_input = loop_input_end_time - loop_input_start_time

    # Check if user repeated numbers correctly
    if recalled_sequence == presented_sequence:
        outcome = 'correct'
        print('Correct!')
        n += 1
        mistakes_in_a_row = 0
    else:
        outcome = 'incorrect'
        print('Incorrect!')
        mistakes_in_a_row += 1
        if mistakes_in_a_row > 1:
            n -= 1

    # calculate total session time in hours, minutes and seconds
    session_time = time.strftime("%H:%M:%S", time.gmtime(time.time() - total_time_start))
    
    # Compose data
    data = {'user_name': name, 'date': current_date, 'time': time.strftime("%H:%M:%S"), 'session_nr': session_nr, 'loop_nr': loop_nr, 'presented_sequence': presented_sequence,
            'recalled_sequence': recalled_sequence, 'outcome': outcome, 'mistakes_in_a_row': mistakes_in_a_row, 'recall_time_in_s': time_taken_loop_input, 'sound_model': sound_model,
            'digit_length': current_loop_n, 'session_time': session_time, 'time_between_digits': wait_time, 'memory_method': memory_method, 'tiredness': tiredness,
            'physical_activity': physical_activity, 'mental_state': mental_state, 'location': location, 'motivation': motivation, 'session_mode': mode}

    # Add data to dataframe
    df = pd.concat([df, pd.DataFrame(data, index=[0])], ignore_index=True)
    
    # print elapsed time in hours, miutes and seconds
    print('__________________________')
    print('Total time elapsed from start: ' + time.strftime("%H:%M:%S", time.gmtime(time.time() - total_time_start)))
    # print current loop number and length of series
    print()
    print('This was round number ' + str(loop_nr))
    print('Next digit length: ' + str(n))
    print('__________________________')

    # Clear screen and wait for user input
    
    # if benchmark mode
    if mode == '3':
        if benchmark_test_loop_nr == 14:
            os.system('cls')
            print('You have reached the end of benchmark test.')
            print()
            print('Press ENTER to continue')
            input()
            os.system('cls')
            status = False
            df.to_csv('Logs/' + name + '_digit_span_log.csv', index=False)
        else:
            print('Press ENTER to continue')
            input()
            os.system('cls')

    # if not benchmark mode
    else:
        print('Press ENTER to continue')
        print()
        print()
        print('...or type "quit" to quit and save your results to a csv file')
        user_input = input(' ---> ')
        os.system('cls')
        if user_input.lower() == 'quit':
            print('Please summarize your experience!')
            print()
            print('(ENTER for skip)')
            print()
            feedback = input(' ---> ')
            # save feedback as a text file with session number, user name and date and time as object
            if feedback != '':
                #generate datetime parameter yyyymmdd_hhmmss
                feedback_datetime = time.strftime("%Y%m%d_%H%M%S")
                with open('Feedback/feedback_' + name + '_' + str(feedback_datetime) + '.txt', 'w') as f:
                    f.write(feedback)
            status = False
            print('Thank you for playing!')
            # print elapsed time in hours, miutes and seconds
            print('Total time elapsed: ' + time.strftime("%H:%M:%S", time.gmtime(time.time() - total_time_start)))
            df.to_csv('Logs/' + name + '_digit_span_log.csv', index=False)