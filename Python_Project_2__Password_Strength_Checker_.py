
import string
import getpass
import tkinter as tk

window = tk.Tk()
window.geometry("1920x1080")
window.config(bg="#698B69")
window.resizable(width=False,height=False)
window.title('Password Strength Checker')

greeting = tk.Label(text="Welcome to a simple Password Strength Checker!",font=(12),foreground= "white",background="black")
Info = tk. Label(foreground= "white", font=(10),background="#698B69",text="Enter your password and click the done button! the application will check the strength of your password.")
entry_label = tk.Label(foreground= "white",font=(10),background="black",text="Enter your Password: ")
result_label = tk.Label(font=(10),foreground= "white",background="black",text="The results are as follows:")
empty_label0=tk.Label(background="#698B69")
empty_label1=tk.Label(background="#698B69")
empty_label2=tk.Label(background="#698B69")
empty_label3=tk.Label(background="#698B69")
empty_label4=tk.Label(background="#698B69")
empty_label5=tk.Label(background="#698B69")
def check_password_strength():
   password = getpass.getpass('Enter the password: ')
   strength = 0
   remarks = ''
   lower_count = upper_count = num_count = wspace_count = special_count = 0

   for char in list(password):
       if char in string.ascii_lowercase:
           lower_count += 1
       elif char in string.ascii_uppercase:
           upper_count += 1
       elif char in string.digits:
           num_count += 1
       elif char == ' ':
           wspace_count += 1
       else:
           special_count += 1

   if lower_count >= 1:
       strength += 1
   if upper_count >= 1:
       strength += 1
   if num_count >= 1:
       strength += 1
   if wspace_count >= 1:
       strength += 1
   if special_count >= 1:
       strength += 1

   if strength == 1:
       remarks = ('That\'s a very bad password.'
           ' Change it as soon as possible.')
   elif strength == 2:
       remarks = ('That\'s a weak password.'
           ' You should consider using a tougher password.')
   elif strength == 3:
       remarks = 'Your password is okay, but it can be improved.'
   elif strength == 4:
       remarks = ('Your password is hard to guess.'
           ' But you could make it even more secure.')
   elif strength == 5:
       remarks = ('Now that\'s one hell of a strong password!!!'
           ' Hackers don\'t have a chance guessing that password!')

   print('Your password has:-')
   print(f'{lower_count} lowercase letters')
   print(f'{upper_count} uppercase letters')
   print(f'{num_count} digits')
   print(f'{wspace_count} whitespaces')
   print(f'{special_count} special characters')
   print(f'Password Score: {strength / 5}')
   print(f'Remarks: {remarks}')


def check_pwd(another_pw=False):
   valid = False
   if another_pw:
       choice = input(
           'Do you want to check another password\'s strength (y/n) : ')
   else:
       choice = input(
           'Do you want to check your password\'s strength (y/n) : ')

   while not valid:
       if choice.lower() == 'y':
           return True
       elif choice.lower() == 'n':
           print('Exiting...')
           return False
       else:
           print('Invalid input...please try again. \n')


if __name__ == '__main__':
   print('===== Welcome to Password Strength Checker =====')
   check_pw = check_pwd()
   while check_pw:
       check_password_strength()
       check_pw = check_pwd(True)