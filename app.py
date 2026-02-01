from taipy.gui import Gui, Icon
from taipy.gui.gui_actions import navigate
from llm import chat_with_llm

# App state
conversation = []
chat_messages: list[tuple[str, str, str]] = []
user_name = "Robert"
users = ["Assistant"]
max_interactions = 3
n_interaction = 0

def send_message(state, var_name, payload: dict):
    # state, varname and payload are default parameters in the call-back action
    (_, _, user_input, sender_id) = payload.get("args", [])

    msg_id = {len(chat_messages)}
    # as it's defined in users, sender_id will always be user_name (users[1][0])
    chat_messages.append((f"{msg_id}",user_input, sender_id))
    conversation.append({"role": "user", "content": user_input})

    # Call LLM
    assistant_reply = chat_with_llm(state.conversation)

    if(state.n_interaction>max_interactions):
        assistant_reply = "Max responses from the LLM reached!"

    # Add assistant message
    msg_id = {len(chat_messages)}
    assistant_id = users[0]
    chat_messages.append((f"{msg_id}",assistant_reply, assistant_id))
    conversation.append({"role": "assistant", "content": assistant_reply})

    state.chat_messages = chat_messages
    state.conversation = conversation
    state.n_interaction = state.n_interaction + 1

def signin(state):
    users.append(state.user_name)
    state.users = users
    navigate(state, "chat")

# Pages rendering
signin_page = """
Please enter your user name:

<|{user_name}|input|>

<|Submit|button|on_action=signin|>
"""

chat_page = """
# 🤖 OpenAI Chatbot Demo

<|{chat_messages}|chat|users = {users}|sender_id = {user_name}|height=400px|width=800px|on_action=send_message|>

"""


pages = {"sign_in": signin_page, "chat": chat_page}
gui = Gui(pages=pages).run(title="OpenAI Chatbot with Taipy", debug=True)