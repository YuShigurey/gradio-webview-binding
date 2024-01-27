import app
import view

from concurrent.futures import ProcessPoolExecutor


def main():
    with ProcessPoolExecutor(max_workers=2) as executor:
        executor.submit(app.main)
        executor.submit(view.main)
        
        
        
if __name__ == '__main__':
    main()