# Project Advancement

_This document outlines the progress and tasks for the development of the Eva Voice Assistant project. It serves as a guide to keep track of what needs to be done and how the project is evolving._

## `main.py`
- Refactor `main.py` to organize code into modular functions or classes, enhancing maintainability.
- Modify `main.py` to accept JSON files as command-line arguments, making it more flexible and adaptable.

## `config`
- Design a generic `prompts.json` file that includes a well-documented structure for prompts, rules, and restrictions. This will facilitate customization and clarity.

## `data`
- Implement the storage and processing of conversation history in the `data` directory. Analyzing interactions, debugging, and enhancing the assistant's performance may benefit from this data.

## `frontend`
- Consider building a user-friendly frontend or platform for running the voice assistant. However, prioritize this as a later phase, focusing on core functionality initially.

## `models`
- Post-MVP, enhance the models used for processing. This could involve fine-tuning, optimization, and expanding capabilities for a broader range of conversations.

## `src`
- `assistant.py`
  - Review and enhance the logic in `assistant.py` as needed.
- `voice_input.py`
  - Continuously refine voice input processing.
- `voice_output.py`
  - Maintain and optimize text-to-voice conversion.

## `templates`
- Investigate ways to improve user experience during wait times. Consider implementing progress indicators or informative messages to keep users engaged.
- Analyze the average response time to optimize the user experience further.

## `tests`
- Develop comprehensive unit tests for various components of the code, especially critical functions, to ensure reliability and correctness.

## **Todo** 
- think about how/where to store the recorded_audio.wav


### Additional Suggestions
- Implement robust error handling and informative error messages for unexpected situations.
- Document code and functions thoroughly using comments or docstrings to enhance understanding.
- Incorporate logging to track important events and errors in the application.
- Ensure contingency plans for external API or service dependencies in case of unavailability.

