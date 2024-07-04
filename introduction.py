# 참고 문서: https://microsoft.github.io/autogen/docs/tutorial/introduction

import copy
import os

from autogen import ConversableAgent

# api key 는 환경변수로 설정(powershell 기준)
# $Env:OPENAI_API_KEY="your_openai_api_key"

agent = ConversableAgent(
    "chatbot",
    # llm_config={"config_list": [{"model": "gpt-4o", "api_key": os.environ.get("OPENAI_API_KEY")}]},
    llm_config={"config_list": [{
        "model": "gpt-4o", 
        "api_key": os.environ.get("OPENAI_API_KEY"), 
        "base_url": "https://aoai-swedn.openai.azure.com",
        "api_type": "azure",
        "api_version": "2024-02-01"
        }]},
    code_execution_config=False,  # Turn off code execution, by default it is off.
    function_map=None,  # No registered functions, by default it is None.
    human_input_mode="NEVER",  # Never ask for human input.
)

reply = agent.generate_reply(messages=[{"content": "Tell me a joke.", "role": "user"}])
print(reply)

# 결과는 다음과 같이 나옴.
# Sure, here's a classic for you:

# Why don’t scientists trust atoms?

# Because they make up everything!


def get_agent(name: str, system_message: str, temperature: float = 0.7, **kwargs) -> ConversableAgent:
    agent = ConversableAgent(
        name,
        system_message=system_message,
        llm_config={"config_list": [{
            "model": "gpt-4o", 
            "api_key": os.environ.get("OPENAI_API_KEY"), 
            "base_url": "https://aoai-swedn.openai.azure.com",
            "api_type": "azure",
            "api_version": "2024-02-01",
            "temperature": temperature
            }]},
        code_execution_config=kwargs.get("code_execution_config", False),  # Turn off code execution, by default it is off.
        function_map=None,  # No registered functions, by default it is None.
        human_input_mode=kwargs.get("human_input_mode", "NEVER"),  # Never ask for human input.
        max_consecutive_auto_reply=kwargs.get("max_consecutive_auto_reply", 100),
        is_termination_msg=kwargs.get("is_termination_msg", None),
        
    )
    return agent

cathy = get_agent("Cathy", "Your name is Cathy and you are a part of a duo of comedians.", 0.9)

joe = get_agent("Joe", "Your name is Joe and you are a part of a duo of comedians.", 0.7)

result = joe.initiate_chat(cathy, message="Cathy, tell me a joke.", max_turns=2)

