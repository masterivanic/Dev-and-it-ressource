import string
from collections import Counter, deque, namedtuple
import csv

"""
 this function return an Counter object,
 count element of an iterable argument
"""
def count_word(paragraph: str):
    paragraph = paragraph.lower()
    paragraph = paragraph.translate(str.maketrans('', '', string.punctuation))
    word_list = paragraph.split()
    counter = Counter(word_list)
    return counter


def get_popular_items(items):
    counter_element = Counter(items)
    most_element = counter_element.most_common(None)
    return most_element


def doing_inventory():
    inventory = Counter(STA001=10, SAL002=20, ENT003=13)
    sales = Counter(STA001=5, SAL002=5, ENT003=3)
    inventory = inventory - sales
    print(inventory, end='Before\n')

    # UPDATE INVENTORY
    shipping = {"STA001": 9, "ENT003": 3}
    inventory.update(shipping)
    print(inventory, end='After')


def palindrome(text):
    return text[::-1] == text


def palindrome_2(word):
    d = deque(word)
    while len(d) > 1:
        if d.pop() != d.popleft():
            return False
    return True


def can_take_order(driver, num_packages):
    return driver.car_capacity >= num_packages


def driver_creation():
    Driver = namedtuple('driver', ['name', 'car_type', 'car_capacity'])
    iris = Driver('Leo', 'Renault', 12)
    nattan = Driver('Nathan', 'Prius', 90)
    print(can_take_order(iris, 20))
    print(can_take_order(nattan, 20))
    print(nattan.__doc__)


class Task(object):
    def __init__(self, task_desc, has_priority=False):
        self.task_desc = task_desc
        self.has_priority = has_priority

    def __str__(self):
        return "Task: {0}, Priorit:{1}".format(self.task_desc, self.has_priority)


task_queue = deque()


def add_task(task: Task):
    if task.has_priority:
        task_queue.appendleft(task)
    else:
        task_queue.append(task)


def do_task():
    return task_queue.popleft()


def print_task():
    for t in task_queue:
        print(t.task_desc)


def to_do_task():
    add_task(Task("writing code"))
    add_task(Task("Buy a pet"))
    add_task(Task("Coding algorithm", True))
    print_task()
    print(do_task())


def read_csv():
    with open('data/Customer.csv', 'r') as file:
        read = csv.reader(file)
        # get first line as nametuple to define an object
        Person = namedtuple("Person", next(read))
        for line in read:
            # *line because line is a list, so *list get as many args unless a list
            person = Person(*line)
            print(person, end='\n')

# ----------------- execute our functions -----------------------------


if __name__ == '__main__':
    paragraph = """ If you're looking for random paragraphs, you've come to the right place. 
        When a random word or a random sentence isn't quite enough, the next logical step is to 
        find a random paragraph. We created the Random Paragraph Generator with you in mind. 
        The process is quite simple. Choose the number of random paragraphs you'd like to see 
        and click the button. Your chosen number of paragraphs will instantly appear """
    read_csv()
