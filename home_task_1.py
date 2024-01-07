from random import randint
from queue import Queue

# task 1
queue = Queue(maxsize=10)

generate_request_const = "Generate request"
process_request_const = "Process all requests"
exit_const = "Exit"

choice_mapping = {
    1: generate_request_const,
    2: process_request_const,
    3: exit_const,
}


def generate_request():
    if queue.full():
        print("Queue is full. Request ignored, please process existing requests first.")
        return None
    request_num = randint(1, 5)
    if request_num in queue.queue:
        print(f"Request # {request_num} already generated. Request ignored.")
        return None
    queue.put(request_num)
    print(f"Request generated: # {request_num}")


def process_request():
    if not queue.empty():
        for _ in range(len(queue.queue)):
            print(f"Request processed: # {queue.get()}")
    else:
        print("Queue is empty")


while True:
    try:
        for key, value in choice_mapping.items():
            print(f"{key}. {value}")
        choice = int(input("Enter your choice: "))
        if choice_mapping.get(choice) == exit_const:
            break
        elif choice_mapping.get(choice) == generate_request_const:
            generate_request()
        elif choice_mapping.get(choice) == process_request_const:
            process_request()
    except ValueError:
        print("Invalid input. Please enter a command number from 1 to 3.")
