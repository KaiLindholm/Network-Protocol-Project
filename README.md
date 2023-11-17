# Custom Network Protocol for Client-Server Connection

The objective of this project involves establishing a client-server connection using a tailored network protocol. This connection relies on TCP, ensuring a robust link between the two entities. The protocol facilitates seamless messaging between the client and server until either party opts to terminate communication, which concludes the program.

## Protocol Overview

The handshake protocol operates as follows: upon establishing the TCP socket connection, the client initiates by sending a REQ to the server. Subsequently, the server responds with an ACK to acknowledge the REQ. The client then verifies the success of the handshake through the received ACK. Once the handshake is confirmed, the client gains the ability to transmit messages to the server, which in turn echoes the same response back.

This foundational structure can be expanded upon to introduce additional functionalities akin to TELNET. These enhancements can include establishing a secure connection to facilitate remote CLI commands to the server.
