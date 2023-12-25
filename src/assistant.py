import openai
from openai import OpenAI

client = OpenAI(api_key="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")


class Assistant:
    def __init__(self, config):
        self.api_key = config["api_key"]
        self.model_name = config["model_name"]  # todo: change it to inherite it from the json file
        self.assistantID = config["assistantID"]  # todo : change it for a fucntion receive from json
        # Add other configuration attributes here
        self.prompt_history = ""
        self.conversation = []
        self.menu = config["menu"]
        self.menu_option = config["menu_option"]

        openai.api_key = self.api_key
        self.assistantID = ''.join(self.assistantID)

    def update_historic(self, user_identifier, data):  # Update the conversation history log
        return "update historic_succeed"

    def generate_answer(self, customer_input):

        completion = client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system",
                 "content": (self.assistantID + "This is your conversation so far: " + self.prompt_history)
                 },
                {"role": "user", "content": customer_input}
            ],
            temperature=1
        )
        assistant_reply = completion.choices[0].message.content

        self.prompt_history += ("user:" + customer_input + "system:" + assistant_reply)
        self.conversation.append({"role": "system", "content": assistant_reply})
        self.conversation.append({"role": "user", "content": customer_input})
        self.extract_menu_option(assistant_reply)

        return assistant_reply

    def extract_menu_option(self, response):
        # Iterate through each menu option
        for index, option in enumerate(self.menu_option):
            # Check if the option text exists in the response
            if option in response:
                print('\nService found #', index, ": ", option)
                return str(index)  # Return the index of the matched option
        return None  # Return None if no menu option is found

    def get_historic(self):
        # Fetch historical conversation data
        return "get_historic succeed"

    def get_client_info(self):
        # Fetch additional client information
        return "get_client_info succeed"

    def set_tonality(self, tonality):
        # Set the tonality attribute
        return "set_tonality succeed"

    def set_styling(self, styling):
        # Set the styling attribute
        return "set_styling succeed"

    def set_special_information(self, special_information):
        # Set the special_information attribute
        return "set_special_information succeed"

    def set_welcome_messages(self, welcome_messages):
        # Set the welcome_messages attribute
        return "set_welcome_messages succeed"

    def set_end_message(self, end_message):
        # Set the end_message attribute
        return "set_end_message succeed"

    def add_prompt(self, criteria, prompt):
        # Add a prompt for a specific service
        return "add_prompt succeed"


#
# class User:
#     def __init__(self, user_identifier):
#         self.user_identifier = user_identifier
#
#     def send_input(self, user_input):
#         # Send user input to the assistant
#         return "send_input succeed"
#
#     def receive_response(self, response):
#         # Receive and process the assistant's response
#         return "receive_response succeed"
#

# # Load the client-specific configuration from a JSON file
# with open("client_config.json", "r") as config_file:
#     client_config = json.load(config_file)

# # Initialize the Assistant
# assistant = Assistant(client_config)
#
# # Example usage:
# user = User("user123")
# user_input = "I want to speak to a banker."
# response = assistant.generate_response(user_input)
# print(response)
