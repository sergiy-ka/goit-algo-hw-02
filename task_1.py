# Завдання 1

from queue import Queue
import random
import uuid
import time

def generate_request(queue):
    request_id = uuid.uuid4()
    queue.put(request_id)

def process_request(queue):
    if not queue.empty():
        start_time = time.time()
        request_id = queue.get()
        print(f'Processing request № {request_id}')
        time.sleep(random.randint(1, 5))
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'    Time of request processing: {elapsed_time:.2f} seconds')
    else:
        print('Queue is empty')

def parse_input(user_input):
    cmd = user_input.strip().lower()
    return cmd
    
def count_requests_in_queue(queue):
    print(f'Count requests in queue: {queue.qsize()}')

def main():
    queue = Queue()
    while True:
        try:
            user_input = input('Enter the number of requests to process (from 1 to 10) or "q" to exit: ')
            command = parse_input(user_input)
            if command == 'q':
                print('Exit from the programme.')
                break
            elif command.isdigit() and 1 <= int(command) <= 10:
                for i in range(int(command)):
                    generate_request(queue)
                count_requests_in_queue(queue)
                time.sleep(2)       
                for i in range(int(command)):
                    process_request(queue)
                count_requests_in_queue(queue)
            else:
                print('Invalid input.')
        except KeyboardInterrupt:
            print('\nProgram was stopped by user.')
            break
        except Exception as e:
            print(f'Error: {type(e).__name__}')
            break

if __name__ == '__main__':
    main()
