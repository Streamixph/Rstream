# main.py (Final and Simplest Version)
import asyncio
import uvicorn
from pyrogram import idle
from bot import bot, initialize_clients
from webserver import app

async def main():
    print("Starting application...")

    # Bot ko start karo
    await bot.start()
    print("Main bot started.")

    # Baaki clients ko initialize karo
    await initialize_clients(bot)
    print("All clients initialized.")

    # Web server ko start karo
    server_config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="info")
    server = uvicorn.Server(server_config)
    
    # Dono ko ek saath chalao
    # server.serve() background me chalega
    # idle() bot ko zinda rakhega
    await asyncio.gather(
        server.serve(),
        idle() 
    )
    print("Application is shutting down...")
    await bot.stop()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nManually shutting down...")
