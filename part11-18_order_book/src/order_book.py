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
        return list(set(task.programmer for task in self._orders))

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