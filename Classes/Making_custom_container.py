class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0)+1

    # magic method to get item
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    # magic method to set item
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count
    # magic method to get length

    def __len__(self):
        return len(self.tags)
    # magin method to iterate

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud["python"] = 10
cloud.add("Python")
cloud.add("Python")
cloud.add("Python")
cloud.add("Java")
print(len(cloud.tags))
print(cloud.tags)
