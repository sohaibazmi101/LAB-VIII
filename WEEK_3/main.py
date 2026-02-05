from Ques1 import Ques1
from Ques2 import Ques2
from Ques3 import Ques3
from Ques4 import Ques4
import http.server
import socketserver
import threading
import webbrowser
import os

def start_server(port=8000):
    # Serve the current directory (no chdir)
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), handler)
    print(f"Serving HTML files at http://localhost:{port}")
    httpd.serve_forever()

# Start server in background
server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

# ...rest of your menu code stays the same...


choice = 1
while choice != 0:
    print("\n------------------MENU------------------")
    print("All Questions: from WEEK_3")
    print("1. Ques 1: ")
    print("2. Ques 2: ")
    print("3. Ques 3: ")
    print("4. Ques 4: ")
    print("5. Ques 5: ")
    print("6. Ques 6: ")
    print("0. Exit")
    
    try:
        choice = int(input("---------------Enter your Choice--------------- : "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        a = int(input("Enter a number: "))
        obj = Ques1(a)
        print(obj.even_or_odd())
    elif choice == 2:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        c = int(input("Enter a third number: "))
        obj = Ques2(a, b, c)
        print(obj.largest())
    elif choice == 3:
        a = int(input("Enter the number of terms for Fibonacci sequence: "))
        obj = Ques3(a)
        print(obj.fibonacci())
    elif choice == 4:
        text = input("Enter a string: ")
        obj = Ques4(text)
        print(obj.count_vowels())
    elif choice == 5:
        # Open Ques5.html in the online preview
        url = "http://localhost:8000/Ques5.html"
        print(f"Opening Ques5.html in browser at {url}")
        webbrowser.open(url)
    elif choice == 0:
        print("Exiting...")
    else:
        print("Invalid choice. Please try again.")
