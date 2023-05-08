import os

if __name__ == '__main__':
    print("Welcome to my world")
    while True:
        x = input("Enter your Name:")
        if x == "q":
            os.system('PowerShell -Command "Add-Type -AssemblyName System.speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'Bye Bye gandu log\')"')
            break
        command = f'PowerShell -Command "Add-Type -AssemblyName System.speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"'
        os.system(command)
