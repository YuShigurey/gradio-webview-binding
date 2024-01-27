from concurrent.futures import ProcessPoolExecutor

import app
import view


def main():
    with ProcessPoolExecutor(max_workers=2) as executor:
        executor.submit(app.main)
        executor.submit(view.main)


if __name__ == '__main__':
    main()
