class problem :
    def __init__(self):
        self.pyramid = []
        self.steps = 0

    def create_pyramid(self, steps ):
        self.steps = steps
        counter = 1
        for i in range(1,steps+1):
            tl = []
            for j in range(i):
                tl.append(counter)
                counter+=1
            self.pyramid.append(tl)
            
    def print_pyramid(self):
        for line in range(self.steps):
            print(self.pyramid[line])

    def find_step_sum(self, step):
        print("Sum of Step {}".format(step), end = " : ")
        for i in range(self.steps):
            if i+1 == step:
                print(sum(self.pyramid[i]))
        return "Invalid Step"

p = problem()
p.create_pyramid(5)
p.print_pyramid()
p.find_step_sum(3)