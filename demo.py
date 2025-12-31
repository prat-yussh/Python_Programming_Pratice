game_running = True

while game_running:
    print("Game running...")
    user = input("Type quit to stop: ")
    if user == "quit":
        game_running = False
