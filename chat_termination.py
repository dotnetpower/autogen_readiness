# 참조: https://microsoft.github.io/autogen/docs/tutorial/chat-termination

import os

from autogen import ConversableAgent
from introduction import get_agent

cathy = get_agent("Cathy", "Your name is Cathy and you are a part of a duo of comedians.", 0.9)
joe = get_agent("Joe", "Your name is Joe and you are a part of a duo of comedians.", 0.7)
result = joe.initiate_chat(cathy, message="Cathy, tell me a joke.", max_turns=2)

# max_turns=3 으로 설정하고, 한글로 바꿔보자
input("#1 Press Enter to continue...")
cathy = get_agent("Cathy", "너의 이름은 캐시이고, 너는 코미디언 듀오의 일원이야.", 0.9)
joe = get_agent("Joe", "너의 이름은 조이고, 너는 코미디언 듀오의 일원이야.", 0.7)
result = joe.initiate_chat(cathy, message="캐시야, 농담 좀 해줘.", max_turns=3)

# 그러므로 max_turns 인자는 initiate_chat 메서드에서 대화를 종료할 최대 턴 수를 설정하는 데 사용됨을 확인.


input("#2 Press Enter to continue...")
joe = get_agent("Joe", "Your name is Joe and you are a part of a duo of comedians.", 0.7, max_consecutive_auto_reply=1)
# joe.max_consecutive_auto_reply = 1 # 이렇게는 설정이 안되고 initiate_chat 메서드의 인자로 설정해야 함.
result = joe.initiate_chat(cathy, message="캐시야, 농담 좀 해줘.")


input("#3 Press Enter to continue...")
joe = get_agent("Joe", "Your name is Joe and you are a part of a duo of comedians.", 0.7, is_termination_msg=lambda msg: "good bye" in msg["content"].lower())
result = joe.initiate_chat(cathy, message="Cathy, tell me a joke and then say the words GOOD BYE.")

# 종료 메시지를 포함시켜서 종료 조건을 설정할 수 있음을 확인.


