#!/usr/bin/env python3.10
from langchain.prompts.pipeline import PipelinePromptTemplate
from langchain.prompts.prompt import PromptTemplate

_FINAL_ARCH_DESIGN_TEMPLATE = """{introduction_prompt}
{react_prompt}
{write_module_description_prompt}
{chip_description_prompt}
"""

introduction_template = """
You are a senior circuit architect, and you are designing a chip."""

react_template = """
Write your thoughts on designing all modules following the format below:
- Task: The task you need to complete. If you think the task is too complex to complete in one iteration, refine the task into small ones.
- Thought: Consider what needs to be done.
- Action: actions to take.
- Action Input: Provide the necessary input for the chosen action. You must print all the action inputs. If the action inputs are too long, show part of them.
- Observation: Record the result of the action.
... (Thought/Action/Action Input/Observation can repeat N times)
- Thought: Once you know the final answer.
- Final Answer: The answer to the original question."""

chip_description_template = """
The chip you are designing is: {chip_description}"""

write_module_description_template = """
After you get the final answer, describe the modules one by one, in separate compact JSON strings in Markdown blocks. \
For each module, the keys are module name, module function, module description, and all the module interfaces. \
All the required module interfaces, \
such as the clock and reset ports, data ports and control ports, etc, should be designed.
The keys of the module interface are the port name, port direction, port width, and port description."""

_FINAL_ARCH_DESIGN_PROMPT = PromptTemplate.from_template(_FINAL_ARCH_DESIGN_TEMPLATE)
introduction_prompt = PromptTemplate.from_template(introduction_template)
react_prompt = PromptTemplate.from_template(react_template)
chip_description_prompt = PromptTemplate.from_template(chip_description_template)
write_module_description_prompt = PromptTemplate.from_template(write_module_description_template)

arch_design_prompts = [
    ("introduction_prompt", introduction_prompt),
    ("react_prompt", react_prompt),
    ("chip_description_prompt", chip_description_prompt),
    ("write_module_description_prompt", write_module_description_prompt)
]
DEFAULT_ARCH_DESIGN_PROMPT = PipelinePromptTemplate(
    final_prompt=_FINAL_ARCH_DESIGN_PROMPT,
    pipeline_prompts=arch_design_prompts
)
