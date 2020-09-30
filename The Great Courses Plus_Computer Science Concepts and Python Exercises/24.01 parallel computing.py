# Amdahl's Law: How much of a speedup can be expected from problems that are
#   partially parallelizable, no matter how many processors you throw at it.
#   ie: 50% - double
#       75% - 4x
#       90% - 10x
#       95% - 20x

# Gustafson's Law: Helps determine how much larger of a problem can be handled
#   given more processors

# RPC (Remote Procedure Calls): basically parallel processing, but across computers
#   and servers, not just on one machine

# Python's Pyro module allows for RPC calls
from multiprocessing import Process


def first_run():

    def print_function(name):
        print("Hello, ", name)

    if __name__ == '__main__':
        p = Process(target=print_function, args=("John",))
        p.start()


def second_run():

    def print_process(proc_num):
        print("Printing from process: ", proc_num)

    if __name__ == '__main__':
        process_list = []
        for i in range(20):
            p = Process(target=print_process, args=(i,))
            process_list.append(p)

        for p in process_list:
            p.start()


second_run()
