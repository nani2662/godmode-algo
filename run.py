# Main script to start backend
from backend.app import main

if __name__ == "__main__":
    main()

    # Keep Render server alive
    import time
    while True:
        time.sleep(60)
