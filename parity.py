def P2(n, table):
    table.extend([n, n ^ 1, n ^ 1, n])
def P4(n, table):
    return (P2(n, table), P2(n ^ 1, table), 
            P2(n ^ 1, table), P2(n, table))
def P6(n, table):
    return (P4(n, table), P4(n ^ 1, table),
            P4(n ^ 1, table), P4(n, table)) 
def LOOK_UP(table):
    return (P6(0, table), P6(1, table),
            P6(1, table), P6(0, table)) 
table = [0] * 256
LOOK_UP(table)
  
def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
        print(result)
    return result


def parity_drop(x):
    result = 0
    while x:
        result ^= 0
        x &= x - 1
    return result


def drop_lowest(x):
    count = 0
    while x:
        print(bin(x))
        print(bin(x - 1))
        x = x & (x - 1)
        print(f"result {bin(x)}")
        count += 1
    print(f"count: {count}")

def drop_lowest2(x):
    count = 0
    while count<5:
        print(bin(x))
        print(bin(~(x - 1)))
        x = x & ~(x - 1)
        print(f"result {bin(x)}")
        count += 1
    print(f"count: {count}")

def main():
    x = 100
    drop_lowest2(x)


if __name__ == "__main__":
    main()