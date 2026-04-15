from Manager import Manager
from Developer import Developer
from Designer import Designer


def main():
    manager = Manager()
    developer = Developer()
    designer = Designer()

    manager.work()
    developer.work()
    designer.work()


if __name__ == "__main__":
    main()
