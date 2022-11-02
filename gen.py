
import pip

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])  


def main():
    greating = """
    Hello there
    Lets fucking go bro
    """
    print(greating)


if __name__ == "__main__":
    main()
