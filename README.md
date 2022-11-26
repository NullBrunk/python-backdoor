# Python

This is a simple python3 backdoor that you can run on a target machine to get easy RCE.
By default, the shell is protected with a combinaison of a ``USERNAME`` and a ``PASSWORD``, and runs on the port ``6556``.

# Usage :

On the target machine, run the python file like this :

```bash
python3 server.py
```

By default, the server run on the port 6556, and the default credentials are :
```
username: admin
password: admin
```
But you can change all those parameters easely.

On the attacker machine :      

![good](https://user-images.githubusercontent.com/106782577/204087250-465f10dd-25ed-40a1-929e-10ce50dc8807.png)


Here i use telnet, it's just a personal preference. You can use netcat, or a python script or whatever you like. 

# Password authentication      
 
![invalid](https://user-images.githubusercontent.com/106782577/204087242-09f12bb7-0c40-4d0c-8d61-7d5b0fc97096.png)



If the username and password are inccorect, the server does not crash. He just respond with an error. This makes it easy to bruteforce, so make sure to use a really strong username and password.
