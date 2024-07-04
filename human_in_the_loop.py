# 참조: https://microsoft.github.io/autogen/docs/tutorial/human-in-the-loop

import os

from autogen import ConversableAgent
from introduction import get_agent

agent_with_number = get_agent("agent_with_number", "You are playing a game of guess-my-number. You have the "
    "number 53 in your mind, and I will try to guess it. "
    "If I guess too high, say 'too high', if I guess too low, say 'too low'. ",
    is_termination_msg=lambda msg: "53" in msg["content"])

agent_guess_number = get_agent("agent_guess_number", "I have a number in my mind, and you will try to guess it. "
    "If I say 'too high', you should guess a lower number. If I say 'too low', "
    "you should guess a higher number. ")

result = agent_with_number.initiate_chat(
    agent_guess_number,
    message="I have a number between 1 and 100. Guess it!",
)

# 정답을 맞추면 대화가 종료되는데 종료될때 메시지를 보여줄 방법은?


human_proxy = ConversableAgent(
    "human_proxy",
    llm_config=False,  # no LLM used for human proxy
    human_input_mode="ALWAYS",  # always ask for human input
)

# Start a chat with the agent with number with an initial guess.
result = human_proxy.initiate_chat(
    agent_with_number,  # this is the same agent with the number as before
    message="10",
)



input("사람이 개입해서 종료시키는 조건..")
agent_with_number = get_agent("agent_with_number", "You are playing a game of guess-my-number. "
    "In the first game, you have the "
    "number 53 in your mind, and I will try to guess it. "
    "If I guess too high, say 'too high', if I guess too low, say 'too low'. ",
    max_consecutive_auto_reply=1,
    is_termination_msg=lambda msg: "53" in msg["content"],
    human_input_mode="TERMINATE")

agent_guess_number = get_agent("agent_guess_number", "I have a number in my mind, and you will try to guess it. "
    "If I say 'too high', you should guess a lower number. If I say 'too low', "
    "you should guess a higher number. ",
    human_input_mode="NEVER")

result = agent_with_number.initiate_chat(
    agent_guess_number,
    message="I have a number between 1 and 100. Guess it!",
)

# 사람이 정답을 맞춰도 끝나지 않고 `exit` 라는 메시지를 보내야 종료됨을 확인. 뭐지 ???