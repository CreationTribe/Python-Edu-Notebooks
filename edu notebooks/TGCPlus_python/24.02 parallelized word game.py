from multiprocessing import Process, Queue


def find_links(words, q, starti, endi):
    for i in range(starti,endi):
        for j in range(i+1, len(words)):
            #compare word i and j
            if compare_words(word[i].get_word(), words[j].get_word()):
                q.put((i, j))   #add_link(words, i, j)


if __name__ == '__main__':
    # Read words in from a dictionary

    q = Queue()
    process_list = []
    for i in range(0, len(words)-100, 100):
        p = Process(target=find_links, args=(words, q, i, i+100))
        process_list.append(p)
    p = Process(target=find_links, args=(words, q, i+100, len(words)))
    process_list.append(p)
    for p in process_list:
        p.start() #starts the individual processes
    while not q.empty():
        i, j = q.get()
        add_link(words, i, j)
    for p in process_list:
        p.join() # brings all the processes back, ie: "waits" for them to all finish

    while not q.empty():
        i, j = q.get()
        add_link(words, i, j)
