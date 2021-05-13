print('Chapter 01 - Exercise 03')
print('Run Timing')
# - Asks you how long to run 10KM
# - Asks how long it took
# - Event to calculate average: Press enter
runs = []

def run_timing():
   while True:
      try:
         time_taken = float(input('Enter 10 km run time: '))
         runs.append(time_taken)
      except ValueError as e:
         average = sum(runs) / len(runs)
         print(f'The average was {average:.2f} over {len(runs)} runs')
         break

if __name__ == '__main__':
    run_timing()