class Recording:
    def __init__(self, length: int):
        self.length = length

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        if length < 0:
            raise ValueError("The length must not be below zero")
        self.__length = length