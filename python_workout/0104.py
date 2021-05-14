print('Chapter 01 - Exercise 04')
print('Hex to Decimal converter')
# Enter a hex number (0x50)
# Return the decimal equivalent (80)
# Don't use `int()` on the whole input
# But can use `int()` on one digit at a time

def hex_output():
   while True:
      try:
         hex_in = input('Enter a hexidecimal number (without the 0x): ')
         if hex_in == '':
            raise ValueError
         dec_out = 0
         for power,digit in enumerate(reversed(hex_in)):
            dec_out += int(digit, 16) * (16 ** power)
         print(f'The decimal value of Ox{hex_in} is: {dec_out}')
      except ValueError as e:
         print('Goodbye.')
         break

if __name__ == '__main__':
    hex_output()