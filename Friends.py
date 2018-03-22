class Friends():
    def __init__(self, connections):
        self.connections = connections

    def add(self, data):
        if data in self.connections:
            return False
        else:
            self.connections.append(data)
            return True

    def remove(self, data):
        if data in self.connections:
            self.connections.remove(data)
            return True
        else:
            return False

# test add (self.connection append data + Tru when set or reversed set not in self.connections )
f = Friends([{'1', '2'}, {'3', '1'}])
print(f.add({'2', '1'}))
print(f.add({'5', '1'}), end='\n\n')

# test (self.connections.remove(i) when data in self.connections)

s = Friends([{'1', '2'}, {'3', '1'}])
print(s.remove({'1', '3'}))
print(s.remove({'4', '5'}))

# test 3
