import asyncio
from bot import start_services

if __name__ == "__main__":
    try:
        asyncio.run(start_services())
    except KeyboardInterrupt:
        print("\nShutting down...")
