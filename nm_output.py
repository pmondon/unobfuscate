class Nm_output:
    def __init__(self, init_string):
        if ' ' in init_string[:16]:
            self.address = 0
        else:
            self.address = int(init_string[:16], 16)
        self.name = init_string[19:]
