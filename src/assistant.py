#import openai
# import json
# from datetime import datetime
# import os
#
#
# class Assistant:
#     def __init__(self, config, client):
#         self.api_key = config["api_key"]
#         self.model_name = config["model_name"]
#         self.client_name = config["client_name"]
#         self.tonality = config["tonality"]
#         self.services = config["services"]
#         self.special_information = config["special_information"]
#         self.welcome_messages = config["welcome_messages"]
#         self.end_message = config["end_message"]
#         self.client_info = config["client_info"]
#         self.prompt_history = []
#
#         openai.api_key = self.api_key
#
#     def update_historic(self, user_identifier, data):
#         # Generate a unique filename for the user's conversation log
#         log_filename = f"{user_identifier}_log.txt"
#
#         # Check if the log file exists, and create it if it doesn't
#         if not os.path.isfile(log_filename):
#             # Create the log file and write initial information
#             current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             with open(log_filename, "w") as log_file:
#                 log_file.write(f"{current_datetime} - Client: {self.client_name}\n")
#                 log_file.write(f"Caller Information: {user_identifier}\n\n")
#
#         # Get the current date and time
#         current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#
#         # Open the log file in append mode
#         with open(log_filename, "a") as log_file:
#             # Write assistant or user information based on the sender
#             if data.startswith("assistant"):
#                 log_file.write(f"assistant [{current_datetime}]: {data}\n")
#             else:
#                 log_file.write(f"user [{current_datetime}]: {data}\n")
#
#         # Append the conversation history
#         self.prompt_history.append(data)
#
#     def generate_response(self, user_input):
#         # Construct the prompt for the API call
#         prompt = f"You are a {self.tonality} telephonic assistant who works for {self.client_name}. "
#         prompt += "Your role is to redirect callers to one of the following services: "
#         prompt += ", ".join(self.services.keys()) + ". "
#         prompt += "The current historical conversation with the client is: " + self.get_historic() + ". "
#         prompt += f"You need to notify callers that: {self.special_information}. "
#         prompt += "This is additional information about your client: " + self.get_client_info() + ". "
#         prompt += "You need to always answer in the language of the user input." #todo: add this to the prompt config file
#
#         # Add user input to the conversation history
#         self.prompt_history.append(user_input)
#
#         # Make the API call
#         response = openai.Completion.create(
#             engine=self.model_name,
#             messages=[
#                 {"role": "system", "content": prompt},
#                 {"role": "user", "content": user_input}
#             ],
#             max_tokens=1000
#         )
#
#         # Extract and return the assistant's reply
#         assistant_reply = response.choices[0].message["content"]
#         self.prompt_history.append(assistant_reply)
#         return assistant_reply
#
#
#
#     def get_historic(self):
#         # Function to fetch and return the historical conversation
#         # You can implement this based on how you store and manage conversation history
#         return "Historical conversation here..."
#
#     def get_client_info(self):
#         # Function to fetch and return additional client information
#         return "Client information here..."
#
# # Load the client-specific configuration from a JSON file
# with open("client_config.json", "r") as config_file:
#     client_config = json.load(config_file)
#
# # Initialize the Assistant
# assistant = Assistant(client_config)
#
# # Example usage:
# user_input = "I want to speak to a banker."
# response = assistant.generate_response(user_input)
# print(response)
#
# ####reste du code
#
# def initialize_assistant(json_config):
#     try:
#         # Load the JSON configuration
#         with open(json_config, 'r') as config_file:
#             config_data = json.load(config_file)
#
#         # Extract relevant information from the JSON config
#         client = config_data["client"]
#         tonality = config_data["tonality"]
#         styling = config_data["styling"]
#         services = config_data["services"]
#         special_information = config_data["special_information"]
#         welcome_messages = config_data["welcome_messages"]
#         end_message = config_data["end_message"]
#         client_info = config_data["client_info"]
#
#         # Initialize and configure the assistant based on the extracted information
#         assistant = Assistant()
#         assistant.set_client_info(client)
#         assistant.set_tonality(tonality)
#         assistant.set_styling(styling)
#         assistant.set_special_information(special_information)
#         assistant.set_welcome_messages(welcome_messages)
#         assistant.set_end_message(end_message)
#         assistant.set_client_info(client_info)
#
#         # Define prompts and responses for services
#         for service_name, service_info in services.items():
#             criteria = service_info["criteria"]
#             prompt = service_info["prompt"]
#             assistant.add_prompt(criteria, prompt)
#
#         return assistant
#
#     except FileNotFoundError:
#         print("Error: Configuration file not found.")
#         return None
#
# # Example usage
# config_file_path = "client_config.json"  # Replace with the path to your JSON config file
# assistant = initialize_assistant(config_file_path)
#
# if assistant:
#     print("Assistant configured successfully!")
#     # Now you can use the assistant to handle interactions based on the configuration.
#     # For example, responding to user input and providing appropriate prompts.
# else:
#     print("Assistant configuration failed.")
#
#


import openai
from datetime import datetime


class Assistant:
    def __init__(self, config):
        self.api_key = config["api_key"]
        self.model_name = config["model_name"] # todo: change it to inherite it from the json file
        self.prompt = config["prompt"] #todo : change it for a fucntion receive from json
        # Add other configuration attributes here
        self.prompt_history = []
        self.conversation = []
        self.menu = config["menu"]

        openai.api_key = self.api_key



    def update_historic(self, user_identifier, data): # Update the conversation history log
        return "update historic_succeed"

    def generate_answer(self, customer_input):
        # Create a message for the user's input
        user_message = {"role": "user", "content": customer_input}

        # Append the user's message to the conversation
        self.conversation.append(user_message)

        # Create a completion with the entire conversation
        completion = openai.ChatCompletion.create(
            model=self.model_name,
            messages=[
                {"role": "system",
                 "content": self.prompt},
                     ] + self.conversation,
            temperature=1
        )

        # Extract the assistant's reply
        assistant_reply = completion['choices'][0]['message']['content']

        # Append the assistant's reply to the conversation
        self.conversation.append({"role": "assistant", "content": assistant_reply})
        self.extract_menu_option(assistant_reply)
        return assistant_reply

    def extract_menu_option(self, response):
        # Iterate through each menu option
        for index, option in enumerate(self.menu):
            # Check if the option text exists in the response
            if option in response:
                print('\nService found #',index,": " ,option)
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

