# Multithreaded Math Server

A simple multithreaded math server created in LAHTP Advanced course that evaluates mathematical expressions using the `bc` command.

## Features

- Multithreaded server to handle multiple client connections simultaneously.
- Supports basic math expressions.
- Interactive help command for users.

## Getting Started

### Prerequisites

- Python 3.x
- colorama library (install using `pip install colorama`)

### Usage

1. Clone the repository:

   ```bash
   git clone https://git.selfmade.ninja:rocky/multithreaded_math_server.git
   ```

2. Navigate to the project directory:

   ```bash
   cd multithreaded-math-server
   ```
3. First instal `bc` tool in your PC

    ```
    $ sudo apt-get install bc
    ```

4. Then run using python 3

    ```
    $ python3 main.py
    ```

5. Follow the prompts to enter the host and port for the server.

6. Connect to the server using a client (e.g., telnet, netcat) 

7. Enter math expressions to get results. Use the `quit` command to exit.

