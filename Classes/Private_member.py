class TagCloud:
    def __init__(self):
        # puting two "_" before variable we can define privte member
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0)+1

    # magic method to get item
    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    # magic method to set item
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count
    # magic method to get length

    def __len__(self):
        return len(self.__tags)
    # magin method to iterate

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()

print(cloud._TagCloud__tags)
