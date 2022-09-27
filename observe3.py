
class Employee:
    def __init__(self, name, working_on_task, status):
        self.name = name
        self.working_on_task = working_on_task
        self.status = status

        for task in working_on_task:
            print(f'registered task that {self.name} work, to Subscriber',task)
            pub.register(task)
            pub.dispatch(self.status)
            # each task that updated must be unregister
            pub.unregister(task)


class Task:
    def __init__(self, name, status=None):
        self.name = name
        self.status = status

    def update_status(self, status):
        print(f'changed status {self.name}', status)
        self.status = status


class Subscriber:

    def __init__(self, object):
        self.object = object

    def update_status(self, status):
        self.object.update_status(status)


class Publisher:
    def __init__(self):
        self.subscribers = set()

    def register(self, who):
        self.subscribers.add(who)

    def unregister(self, who):
        print('unregister task')
        self.subscribers.discard(who)

    def dispatch(self, status):
        print('dispatch message')
        for subscriber in self.subscribers:
            subscriber.update_status(status)


if __name__ == '__main__':
    pub = Publisher()

    first_task = Subscriber(Task)

    task1 = Task(name='task1')
    task2 = Task(name='task2')

    working_on_task = [task1, task2]

    sara = Employee(
        name='sara', working_on_task=working_on_task, status='To-Do'
    )

    saman = Employee(
        name='saman', working_on_task=[task1], status='In-Progress'
    )