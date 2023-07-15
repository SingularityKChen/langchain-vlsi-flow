#!/usr/bin/env python3.10
from langchain.prompts.pipeline import PipelinePromptTemplate
from langchain.prompts.prompt import PromptTemplate

_FINAL_MICRO_ARCH_DESIGN_TEMPLATE = """{introduction_prompt}
{react_prompt}
{write_module_design_prompt}
{chip_description_prompt}
{module_description_prompt}
"""

introduction_template = """
You are a senior circuit architect, and you are refining the micro-architecture design of a module."""

react_template = """
Write your thoughts on refining the internal logic and procedural assignments \
required to implement this module following the format below:
- Task: The task you need to complete. \
If you think the task is too complex to complete in one iteration, refine the task into small ones.
- Thought: Consider what needs to be done.
- Action: actions to take.
- Action Input: Provide the necessary input for the chosen action. You must print all the action inputs. \
If the action inputs are too long, show part of them.
- Observation: Record the result of the action.
... (Thought/Action/Action Input/Observation can repeat N times)
- Thought: Once you know the final answer.
- Final Answer: The answer to the original question."""

write_module_design_template = """
After you get the final answer, describe its all internal logic and procedural assignments \
in separate compact JSON strings in Markdown blocks. \
The keys of the procedural assignment are:
+ name: name of the procedural,
+ logic type: combinational logic or sequential logic,
+ description: functions and behaviors of this procedural assignment. in a markdown code block. """

chip_description_template = """
The chip description is: {chip_description}"""

module_description_template = """
The module you are refining is: {module_description}"""

_FINAL_MICRO_ARCH_DESIGN_PROMPT = PromptTemplate.from_template(_FINAL_MICRO_ARCH_DESIGN_TEMPLATE)
introduction_prompt = PromptTemplate.from_template(introduction_template)
react_prompt = PromptTemplate.from_template(react_template)
write_module_design_prompt = PromptTemplate.from_template(write_module_design_template)
chip_description_prompt = PromptTemplate.from_template(chip_description_template)
module_description_prompt = PromptTemplate.from_template(module_description_template)

micro_arch_design_prompts = [
    ("introduction_prompt", introduction_prompt),
    ("react_prompt", react_prompt),
    ("write_module_design_prompt", write_module_design_prompt),
    ("chip_description_prompt", chip_description_prompt),
    ("module_description_prompt", module_description_prompt)
]
DEFAULT_MICRO_ARCH_DESIGN_PROMPT = PipelinePromptTemplate(
    final_prompt=_FINAL_MICRO_ARCH_DESIGN_PROMPT,
    pipeline_prompts=micro_arch_design_prompts
)
