from modules.voice import take_command
from modules.speak import speak
from modules.actions import perform_action
from modules.ai import chat_with_ai, decide_action


def run_saqib():
    speak("Hello, I am SAQIB. How can I help you?")

    while True:
        command = take_command()

        if not command:
             continue

        if any(word in command for word in ["exit", "bye", "goodbye", "bye bye", "ok bye", "stop"]):
         speak("Goodbye!")
         break

        decision = decide_action(command)
        print("🧠 Decision:", decision)

        if "action" in decision:
            perform_action(command, command)
        else:
            reply = chat_with_ai(command)
            speak(reply)


if __name__ == "__main__":
    run_saqib()
