def connect(ip, port):
    def printer(func):
        def inner(doc):
            print(f"Подключение IP: {ip}:{port}")
            print(f"Принтер {func.__name__}")
            func(doc)
            print(f"Подключение завершено")

        return inner

    return printer


@connect(ip="11.11.11.11", port="7777")
def xerox(document):
    print(f"Печать документа: {document}")


@connect(ip="22.22.22.22", port="8888")
def hp(document):
    print(f"Печать документа: {document}")


xerox("Lesson_10.doc")
hp("Lesson_11.doc")

# Вывод
# Подключение IP: 11.11.11.11:7777
# Принтер xerox
# Печать документа: Lesson_10.doc
# Подключение завершено
# Подключение IP: 22.22.22.22:8888
# Принтер hp
# Печать документа: Lesson_11.doc
# Подключение завершено