def revision():
    try:
        with open('/proc/cpuinfo','r') as f:
            for line in f:
                if line.startswith('Revision'):
                    return 1 if line.rstrip()[-1] in ['1','2'] else 2
    except:
        return 0
