# File receiving emulator
To emulate receiving a file, a client and a server were written to test the operation of the Observer. I don't know why I wrote them on sockets, but they are on sockets :)

## The result of the program
- Server
```text
[+] Listening...
[+] New connection from 172.22.0.3:53180
[+] File name and file size received from the client
Receiving data.csv: 100%|██████████| 34.8M/34.8M [00:16<00:00, 35.0MB/s]
```

- Client
```text
SERVER: Filename and filesize received
Sending data.csv: 100%|██████████| 34.8M/34.8M [00:10<00:00, 56.2MB/s]
```