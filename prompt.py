from enum import Enum


class ChatRole(str, Enum):
    system = "system"
    user = "user"
    assistant = "assistant"


class Prompt:
    def __init__(self):
        self.SYSTEM_PROMPT = (
            "请尽力回答以下问题。您可以使用以下工具：\n"
            "CalculatorTool: 运行计算并返回数字 - 使用Python.\n"
            "GithubUserInfoTool: 返回Github用户信息，包括位置、个人简介、粉丝数、关注数、公共仓库数量、创建时间等，并以json格式呈现。操作输入为GitHub用户名（不带引号）。\n"
            "请按照以下格式编写每个步骤。您可以采取多个步骤，但不要给它们编号。如果上面提供的工具无法回答问题，请随意发挥并以“Final Answer:”开头开始回复。\n"
            "关于与上述工具无关的事情，您不需要思考和行动模式。\n"
            "Question: 你必须回答的输入问题\n"
            "Thought: 你应该时刻考虑要做什么。\n"
            "Action: 需要执行的操作，应该是 [CalculatorTool, GithubUserInfoTool] 中的一个（如果需要,不要同时出现多个Action）。\n"
            "Action Input: the input to the action\n"
            "Observation: the result of the action\n"
            "… (this Thought/Action/Action Input/Observation can repeat N times)\n"
            "Thought: 我现在知道Final Answer。\n"
            "Final Answer: the final answer to the original input question\n"
        )

    def system_prompt(self):
        return {"role": ChatRole.system.value, "content": self.SYSTEM_PROMPT}

    def ai_prompt(self, content):
        return {"role": ChatRole.assistant.value, "content": content}

    def user_prompt(self, content):
        return {"role": ChatRole.user.value, "content": content}
