import json
import random

# Get recent messages
def get_recent_messages():
    # Define the file name and learn instruction
    file_name = "stored_data.json"
    learn_instruction = {
        "role": "system",
        "content": "You are a digital research assistant specializing in organic chemistry reactions. Your name is ReactBot, respond with some charisma and keep your responses to 100 words or less."
    }

    # Initialize messages
    messages = []

    # # Add a random element
    # x = random.uniform(0, 1)
    # if x < 0.5:
    #     learn_instruction["content"] = learn_instruction["content"] + " Your response will include some light humor"
    # else:
    #     learn_instruction["content"] = learn_instruction["content"] + " Your response will include in depth chemistry knowledge"

    # Append instruction to message
    messages.append(learn_instruction)

    # Get last messages
    try:
        with open(file_name) as user_file:
            data = json.load(user_file)

            # Append last 5 items of data
            if len(data) < 5:
                for item in data:
                    messages.append(item)
            else:
                for item in data[-5:]:
                    messages.append(item)

    except Exception as e:
        print(e)
        pass

    # Return
    return messages

# Store Message History
def store_messages(request_message, response_message):
    # Define filename
    file_name = "stored_data.json"

    # Get recent messages
    messages = get_recent_messages()[1:]

    # Add messages to data
    user_message = {"role": "user", "content": request_message}
    assistant_message = {"role": "assistant", "content": response_message}
    messages.append(user_message)
    messages.append(assistant_message)

    # Save Changes to Json
    with open(file_name, "w") as f:
        json.dump(messages, f)


# Reset Messages
def reset_messages():
    # Overwrite current file with nothing
    open("stored_data.json", "w")