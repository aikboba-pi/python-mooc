class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        if not my_list:
            return None

        # Count occurrences of each item
        counts = {}
        for item in my_list:
            counts[item] = counts.get(item, 0) + 1

        # Return the item with the highest count
        return max(counts, key=counts.get)

    @classmethod
    def doubles(cls, my_list: list) -> int:
        counts = {}
        for item in my_list:
            counts[item] = counts.get(item, 0) + 1

        # Count how many unique items appear at least twice
        return sum(1 for count in counts.values() if count >= 2)