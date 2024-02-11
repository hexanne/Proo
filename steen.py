import requests

api_url = "https://chatgpt.apinepdev.workers.dev/"


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def ask_question():
    print(colors.HEADER + "🚀 Welcome to STEEN AI Chat Interface 🤖" + colors.ENDC)
    print(colors.OKBLUE + "Ask me anything! To exit, press Ctrl + C." + colors.ENDC)
    
    while True:
        question = input(colors.OKBLUE + "\nEnter your question: " + colors.ENDC)
        
        response = requests.get(f"{api_url}?question={question}")

        if response.status_code == 200:
            json_response = response.json()
            answer = json_response.get("answer")
            print("\n" + colors.OKGREEN + "🤖 AI Response: " + colors.ENDC + colors.BOLD + answer + colors.ENDC)
        else:
            print(colors.FAIL + "Failed to get a response. Status code:", response.status_code + colors.ENDC)


ask_question()
