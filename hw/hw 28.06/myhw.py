def connection(func,):
    def wrapper(ip, port):
        print("Connected to IP:")
        return wrapper()


@connection
def hp(ip="10.10.10.10",port=5555):
    print(f"Connected to IP:"+ ip +int(port))
    print("I am HP printer")

@connection
def canon(ip="10.10.10.20",port=5554):
    document = "My name Canon!"
    print(document)
    print("Connected to IP:" + ip + int(port))
    print("I am Canon printer")

@connection
def samsung(ip="10.10.10.30", port=5553):
    print("Connected to IP:" + ip + int(port))
    print("I am Samsung printer")


hp(ip="10.10.10.10", port=5555)
canon(ip="10.10.10.20", port=5554)
samsung(ip="10.10.10.30", port=5553)
