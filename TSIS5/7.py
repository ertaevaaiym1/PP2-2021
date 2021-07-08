def file_read(fname):
        content_arr = []
        with open(fname) as f: 
                for line in f:
                        content_arr.append(line)
                print(content_arr)

file_read('test.txt')
