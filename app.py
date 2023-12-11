import sidebar
from state import init_state

def main():
    init_state()
    page = sidebar.app()
    page.app()

if __name__ == "__main__":
    main()
