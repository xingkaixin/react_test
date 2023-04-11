from logger import logger
from prompt import Prompt
from utils import ask_ai, calculator_tool, get_github_user_info


def main(question: str):
    messages = []
    prompt = Prompt()
    messages.append(prompt.system_prompt())
    messages.append(prompt.user_prompt(content=question))
    output = ask_ai(messages)
    logger.info(f"{messages=}")
    logger.info(f"{output=}")

    while "Action" in output:
        action = output.split("Action: ")[1].split("\n")[0]
        action_input = output.split("Action Input: ")[1].split("\n")[0]
        logger.info(f"{action=}")
        logger.info(f"{action_input=}")

        if "GithubUserInfoTool" in action:
            user_info = get_github_user_info(action_input)
            messages.append(prompt.ai_prompt(content=output))
            messages.append(
                prompt.ai_prompt(
                    content=f"Observation: followers:{user_info['followers']}"
                )
            )
        if "CalculatorTool" in action:
            calc_result = calculator_tool(action_input)
            messages.append(prompt.ai_prompt(content=output))
            messages.append(prompt.ai_prompt(content=f"Observation: {calc_result}"))
        logger.info(f"{messages=}")
        output = ask_ai(messages)
        logger.info(f"{output=}")
    final_answer = output.split("Final Answer: ")[1].split("\n")[0]
    logger.success(f"{question=}")
    logger.success(f"{final_answer=}")


if __name__ == "__main__":
    main("What is the result of dividing mckaywrigley’s GitHub followers by 2?")
