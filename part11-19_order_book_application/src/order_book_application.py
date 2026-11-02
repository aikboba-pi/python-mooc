class Task:
    id_counter = 0

    def __init__(self, description: str, programmer: str, workload: int):
        Task.id_counter += 1
        self.id = Task.id_counter
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self._finished = False

    def is_finished(self) -> bool:
        return self._finished

    def mark_finished(self):
        self._finished = True

    def __str__(self):
        status = "FINISHED" if self._finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"


class OrderBook:
    def __init__(self):
        self._orders = []

    def add_order(self, description: str, programmer: str, workload: int):
        task = Task(description, programmer, workload)
        self._orders.append(task)

    def all_orders(self) -> list:
        return self._orders

    def programmers(self) -> list:
        # Сохраняем исходный порядок добавления программистов без дубликатов
        seen = []
        for task in self._orders:
            if task.programmer not in seen:
                seen.append(task.programmer)
        return seen

    def mark_finished(self, id: int):
        for task in self._orders:
            if task.id == id:
                task.mark_finished()
                return
        raise ValueError(f"No task with id {id}")

    def finished_orders(self) -> list:
        return [task for task in self._orders if task.is_finished()]

    def unfinished_orders(self) -> list:
        return [task for task in self._orders if not task.is_finished()]

    def status_of_programmer(self, programmer: str) -> tuple:
        programmer_tasks = [task for task in self._orders if task.programmer == programmer]

        if not programmer_tasks:
            raise ValueError(f"No programmer named {programmer}")

        finished_tasks = [task for task in programmer_tasks if task.is_finished()]
        unfinished_tasks = [task for task in programmer_tasks if not task.is_finished()]

        finished_count = len(finished_tasks)
        unfinished_count = len(unfinished_tasks)

        finished_hours = sum(task.workload for task in finished_tasks)
        unfinished_hours = sum(task.workload for task in unfinished_tasks)

        return (finished_count, unfinished_count, finished_hours, unfinished_hours)


class OrderBookApplication:
    def __init__(self):
        self.__orders = OrderBook()

    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add_order(self):
        description = input("description: ")
        programmer_and_workload = input("programmer and workload estimate: ")
        
        parts = programmer_and_workload.split()
        if len(parts) != 2:
            print("erroneous input")
            return
        
        programmer = parts[0]
        try:
            workload = int(parts[1])
        except ValueError:
            print("erroneous input")
            return

        self.__orders.add_order(description, programmer, workload)
        print("added!")

    def list_finished(self):
        finished = self.__orders.finished_orders()
        if not finished:
            print("no finished tasks")
        else:
            for task in finished:
                print(task)

    def list_unfinished(self):
        unfinished = self.__orders.unfinished_orders()
        if not unfinished:
            print("no unfinished tasks")
        else:
            for task in unfinished:
                print(task)

    def mark_finished(self):
        id_str = input("id: ")
        try:
            task_id = int(id_str)
            self.__orders.mark_finished(task_id)
            print("marked as finished")
        except ValueError:
            print("erroneous input")

    def list_programmers(self):
        for programmer in self.__orders.programmers():
            print(programmer)

    def programmer_status(self):
        programmer = input("programmer: ")
        try:
            status = self.__orders.status_of_programmer(programmer)
            finished_count, unfinished_count, finished_hours, unfinished_hours = status
            print(f"tasks: finished {finished_count} not finished {unfinished_count}, hours: done {finished_hours} scheduled {unfinished_hours}")
        except ValueError:
            print("erroneous input")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.list_finished()
            elif command == "3":
                self.list_unfinished()
            elif command == "4":
                self.mark_finished()
            elif command == "5":
                self.list_programmers()
            elif command == "6":
                self.programmer_status()
            else:
                print("erroneous input")


application = OrderBookApplication()
application.execute()