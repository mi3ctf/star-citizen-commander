import buttonHandler
import buttonActions

try:
    print("Starting Program execution - MAIN")
    with buttonHandler.ButtonHandler() as buttonDictionary:
        while True:
            buttonActions.scanButtons(buttonDictionary)
finally:
    print("Finished Excuting MAIN")