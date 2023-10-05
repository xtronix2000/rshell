import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.0.1', 8888))  # your server address and free port
s.listen(5)
client, addr = s.accept()
while True:
  command = str(input('Enter a command: '))
  client.send(command.encode())
  if command.lower() == 'exit':
    print('Bye!')
    break
  result_output = client.recv(1024).decode()
  print(result_output)
client.close()
s.close()
  
