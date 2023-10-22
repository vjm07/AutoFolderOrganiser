from modules.scheduler import scheduler



print("Starting organiser...")
scheduler.start()

try:
    while True:
        pass
except (KeyboardInterrupt, SystemExit):
    # Shut down the scheduler gracefully
    scheduler.shutdown()

