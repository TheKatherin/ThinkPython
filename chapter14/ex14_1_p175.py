def sed(pattern, replace_str, source, dest):

    """Reads a source file and writes the destination file.

    In each line, replaces pattern with replace.

    pattern: string
    replace: string
    source: string filename
    dest: string filename """

    try:
        fin = open(source, 'r')
        fout = open(dest, 'w')
        for line in fin:
            line = line.replace(pattern,replace_str)
            fout.write(line)
        fin.close()
        fout.close()
    except:
        print('Something went wrong.')

sed('sdf', '123', 'test1.txt', 'test2.txt')




